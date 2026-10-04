# ZRF Nibble Machine V1

## Purpose

A deliberately small execution model for studying how bits become state transitions and control-flow decisions without importing a legacy VM or runner implementation.

Each instruction is exactly one byte:

```text
bits 7..4 = opcode
bits 3..0 = operand nibble
```

Machine state:

```text
A       4-bit accumulator
B       4-bit secondary register
ZERO    1-bit zero flag
PC      instruction index
MEM     16 × 4-bit cells stored in bytes
TICKS   executed-instruction counter
HALTED  terminal state flag
```

All register and memory values are masked to the low nibble after operations that can widen.

## Instruction table

| High nibble | Mnemonic | Semantics |
|---:|---|---|
| `0` | `NOP` | no state change except `PC/TICKS` |
| `1` | `LDA i` | `A ← i` |
| `2` | `LDB i` | `B ← i` |
| `3` | `XOR` | `A ← A xor B` |
| `4` | `AND` | `A ← A and B` |
| `5` | `OR` | `A ← A or B` |
| `6` | `NOT` | `A ← not A` in 4 bits |
| `7` | `ADD` | `A ← (A + B) mod 16` |
| `8` | `SUB` | `A ← (A - B) mod 16` |
| `9` | `CMPZ` | `ZERO ← (A = 0)` |
| `A` | `JZ t` | if `ZERO=1`, `PC ← t` |
| `B` | `JNZ t` | if `ZERO=0`, `PC ← t` |
| `C` | `STA m` | `MEM[m] ← A` |
| `D` | `LDA m` | `A ← MEM[m]` |
| `E` | `SWAP` | exchange `A` and `B` |
| `F` | `HALT` | terminal state |

`JZ/JNZ` intentionally use a 4-bit absolute target. V1 therefore has a directly addressable control-flow window of 16 instruction positions. Expansion requires a new version, not silent reinterpretation.

## Deterministic self-test program

```text
0: 15   A=5
1: 23   B=3
2: 30   A=5 xor 3 = 6
3: C2   MEM[2]=6
4: 18   A=8
5: 28   B=8
6: 80   A=0
7: 90   ZERO=1
8: AA   jump to 10
9: 1F   must be skipped
A: D2   A=MEM[2]=6
B: F0   HALT
```

Acceptance conditions:

```text
status      = HALTED
A           = 6
MEM[2]      = 6
TICKS       = 11
```

## Failure states

```text
BAD_INPUT
PC_OOB
STEP_LIMIT
```

The step limit is mandatory so a malformed program cannot convert a test into an unbounded execution claim.
