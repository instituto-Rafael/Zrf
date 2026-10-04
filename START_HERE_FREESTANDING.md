# START HERE — ZRF clean-room freestanding bit image V1

Status: `IMPLEMENTED_LOCAL_PREFLIGHT_PASS / REMOTE_CI_PENDING / PHYSICAL_BOOT_TOKEN_VAZIO`

## Intention

Create an authorial low-level ZRF lane whose runtime does not depend on Python, libc, an operating system, a heap, a dynamic loader, or copied runner/action code.

This lane is intentionally separate from the historical Python mathematics core. The Python core remains a valid higher-level implementation; this directory is the lower-level execution experiment.

## Authority and route

```text
INTENT
→ this START HERE
→ freestanding/provenance/CLEANROOM_MANIFEST.json
→ freestanding/spec/ZRF_NIBBLE_MACHINE_V1.md
→ freestanding/include/zrf_bits.h + freestanding/src/zrf_bits.c
→ freestanding/arch/<isa>/start.S + freestanding/linker/<isa>.ld
→ freestanding/build/build.sh
→ freestanding/tests/host_selftest.c
→ CI receipt
```

Producer authority: `instituto-Rafael/Zrf`.

Observation-only references:

- `rafaelmeloreisnovo/runner-images_RAFCODE`: image/build/release concepts only; no source code imported.
- `rafaelmeloreisnovo/actions`: orchestration/provenance concepts only; inherited code remains third-party.
- `rafaelmeloreisnovo/Est-dio-de-udio`: consumer/use-case reference only; no source code imported.

## Runtime contract

The freestanding artifact is built with:

- `-ffreestanding`
- `-fno-builtin`
- `-fno-stack-protector`
- no libc
- no heap
- no syscalls
- no dynamic loader
- no undefined runtime symbols

Targets materialized in V1:

```text
x86_64-none-elf
aarch64-none-elf
armv7a-none-eabi
```

The architecture adapters provide only `_start`, a private 4 KiB stack, a call into the common ZRF core, and an idle instruction loop.

## What “independent” means here

`runtime_independent_from_host_OS = true` is allowed only when ELF inspection shows no interpreter, no `NEEDED` entries and no undefined symbols.

It does **not** mean independence from physical ISA rules or from the hardware/firmware mechanism that places the image in memory and transfers control to its entry point. A physical boot receipt is still `TOKEN_VAZIO` until an actual target executes it.

## Evidence states

```text
SOURCE        = repository files and declared observation references
ARTIFACT      = ELF + raw BIN produced from this lane
EXECUTION     = hosted semantic self-test; physical bare-metal execution pending
EVIDENCE      = build log + ELF inspection + hashes + future physical receipt
CLAIM         = bounded by the evidence above
```

`IMPLEMENTED_UNTESTED != PASS` and `TOKEN_VAZIO != 0` remain mandatory.

## Local verification

```sh
./freestanding/build/build.sh
```

Expected high-level result:

```text
host semantic self-test = PASS
x86_64 artifact         = no dynamic dependency / no undefined symbol
aarch64 artifact        = no dynamic dependency / no undefined symbol
armv7 artifact          = no dynamic dependency / no undefined symbol
```

The build toolchain is a **factory dependency**, not a runtime dependency. Compiler/linker provenance must remain recorded separately from the produced image.
