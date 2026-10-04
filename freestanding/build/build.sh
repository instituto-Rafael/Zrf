#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
OUT="$ROOT/out"
rm -rf "$OUT"
mkdir -p "$OUT/x86_64" "$OUT/aarch64" "$OUT/armv7" "$OUT/host"

CC_HOST=${CC_HOST:-cc}
CLANG=${CLANG:-clang}

resolve_lld() {
  if [ -n "${LD_LLD:-}" ]; then
    if [ -x "$LD_LLD" ]; then
      printf '%s\n' "$LD_LLD"
      return 0
    fi
    if command -v "$LD_LLD" >/dev/null 2>&1; then
      command -v "$LD_LLD"
      return 0
    fi
  fi

  if command -v ld.lld >/dev/null 2>&1; then
    command -v ld.lld
    return 0
  fi

  for ndk_root in "${ANDROID_NDK:-}" "${ANDROID_NDK_HOME:-}" "${ANDROID_NDK_LATEST_HOME:-}" "${ANDROID_NDK_ROOT:-}"; do
    if [ -n "$ndk_root" ]; then
      candidate="$ndk_root/toolchains/llvm/prebuilt/linux-x86_64/bin/ld.lld"
      if [ -x "$candidate" ]; then
        printf '%s\n' "$candidate"
        return 0
      fi
    fi
  done

  for candidate in /usr/lib/llvm-*/bin/ld.lld; do
    if [ -x "$candidate" ]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done

  return 1
}

LD_LLD=$(resolve_lld) || {
  echo "factory linker unavailable: no executable ld.lld found in PATH, Android NDK roots, or /usr/lib/llvm-*" >&2
  exit 127
}

echo "factory.clang=$(command -v "$CLANG")"
echo "factory.ld_lld=$LD_LLD"
"$LD_LLD" --version | sed -n '1p'

"$CC_HOST" -std=c11 -Wall -Wextra -Werror -I"$ROOT/include" \
  "$ROOT/src/zrf_bits.c" "$ROOT/tests/host_selftest.c" -o "$OUT/host/zrf_host_selftest"
"$OUT/host/zrf_host_selftest"

build_target() {
  name=$1
  target=$2
  emulation=$3
  extra=$4

  "$CLANG" --target="$target" -std=c11 -Oz -Wall -Wextra -Werror \
    -ffreestanding -fno-builtin -fno-stack-protector -fno-pic $extra \
    -I"$ROOT/include" -c "$ROOT/src/zrf_bits.c" -o "$OUT/$name/zrf_bits.o"
  "$CLANG" --target="$target" -c $extra "$ROOT/arch/$name/start.S" -o "$OUT/$name/start.o"

  "$LD_LLD" -m "$emulation" -T "$ROOT/linker/$name.ld" --build-id=none \
    -o "$OUT/$name/zrf-$name.elf" "$OUT/$name/start.o" "$OUT/$name/zrf_bits.o"

  "$LD_LLD" -m "$emulation" -T "$ROOT/linker/$name.ld" --build-id=none \
    --oformat=binary -o "$OUT/$name/zrf-$name.bin" \
    "$OUT/$name/start.o" "$OUT/$name/zrf_bits.o"
}

build_target x86_64 x86_64-none-elf elf_x86_64 "-mno-red-zone"
build_target aarch64 aarch64-none-elf aarch64elf ""
build_target armv7 armv7a-none-eabi armelf "-mfloat-abi=soft"

RECEIPT="$OUT/FREESTANDING_RECEIPT.txt"
{
  echo "format=ZRF_FREESTANDING_RECEIPT_V1"
  echo "host_semantic_selftest=PASS"
  echo "raw_image_emitter=ld.lld"
  echo "physical_boot=TOKEN_VAZIO"
} > "$RECEIPT"

for arch in x86_64 aarch64 armv7; do
  elf="$OUT/$arch/zrf-$arch.elf"
  bin="$OUT/$arch/zrf-$arch.bin"
  test -s "$elf"
  test -s "$bin"

  if readelf -l "$elf" 2>/dev/null | grep -q 'INTERP'; then
    echo "unexpected interpreter in $arch" >&2
    exit 1
  fi
  if readelf -d "$elf" 2>/dev/null | grep -q 'NEEDED'; then
    echo "unexpected dynamic dependency in $arch" >&2
    exit 1
  fi
  if nm -u "$elf" | grep -q .; then
    echo "undefined symbol in $arch" >&2
    nm -u "$elf" >&2
    exit 1
  fi

  bytes=$(wc -c < "$bin" | tr -d ' ')
  digest=$(sha256sum "$bin" | awk '{print $1}')
  {
    echo "arch.$arch.elf=PASS"
    echo "arch.$arch.interpreter=NONE"
    echo "arch.$arch.needed=NONE"
    echo "arch.$arch.undefined_symbols=0"
    echo "arch.$arch.bin_bytes=$bytes"
    echo "arch.$arch.bin_sha256=$digest"
  } >> "$RECEIPT"
  printf '%s %s bytes %s\n' "$arch" "$bytes" "$digest"
done

cat "$RECEIPT"
