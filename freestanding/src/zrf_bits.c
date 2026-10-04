#include "zrf_bits.h"

#define ZRF_NIBBLE(v) ((zrf_u8)((v) & 0x0Fu))
#define ZRF_OPCODE(v) ((zrf_u8)(((v) >> 4) & 0x0Fu))
#define ZRF_OPERAND(v) ZRF_NIBBLE(v)

volatile zrf_u32 zrf_boot_receipt = 0xFFFFFFFFu;

void zrf_reset(zrf_state *state) {
    zrf_u8 i;
    state->a = 0u;
    state->b = 0u;
    state->zero = 1u;
    state->halted = 0u;
    state->pc = 0u;
    state->ticks = 0u;
    for (i = 0u; i < 16u; ++i) {
        state->memory[i] = 0u;
    }
}

static void zrf_refresh_zero(zrf_state *state) {
    state->zero = (zrf_u8)(state->a == 0u);
}

zrf_u32 zrf_run(zrf_state *state, const zrf_u8 *code, zrf_u8 code_size, zrf_u32 max_steps) {
    if ((state == (zrf_state *)0) || (code == (const zrf_u8 *)0) || (code_size == 0u)) {
        return ZRF_STATUS_BAD_INPUT;
    }

    while ((state->halted == 0u) && (state->ticks < max_steps)) {
        zrf_u8 instruction;
        zrf_u8 opcode;
        zrf_u8 operand;

        if (state->pc >= code_size) {
            return ZRF_STATUS_PC_OOB;
        }

        instruction = code[state->pc];
        opcode = ZRF_OPCODE(instruction);
        operand = ZRF_OPERAND(instruction);
        state->pc = (zrf_u8)(state->pc + 1u);
        state->ticks = state->ticks + 1u;

        switch (opcode) {
            case 0x0u:
                break;
            case 0x1u:
                state->a = operand;
                zrf_refresh_zero(state);
                break;
            case 0x2u:
                state->b = operand;
                break;
            case 0x3u:
                state->a = ZRF_NIBBLE(state->a ^ state->b);
                zrf_refresh_zero(state);
                break;
            case 0x4u:
                state->a = ZRF_NIBBLE(state->a & state->b);
                zrf_refresh_zero(state);
                break;
            case 0x5u:
                state->a = ZRF_NIBBLE(state->a | state->b);
                zrf_refresh_zero(state);
                break;
            case 0x6u:
                state->a = ZRF_NIBBLE(~state->a);
                zrf_refresh_zero(state);
                break;
            case 0x7u:
                state->a = ZRF_NIBBLE((zrf_u8)(state->a + state->b));
                zrf_refresh_zero(state);
                break;
            case 0x8u:
                state->a = ZRF_NIBBLE((zrf_u8)(state->a - state->b));
                zrf_refresh_zero(state);
                break;
            case 0x9u:
                zrf_refresh_zero(state);
                break;
            case 0xAu:
                if (state->zero != 0u) {
                    state->pc = operand;
                }
                break;
            case 0xBu:
                if (state->zero == 0u) {
                    state->pc = operand;
                }
                break;
            case 0xCu:
                state->memory[operand] = ZRF_NIBBLE(state->a);
                break;
            case 0xDu:
                state->a = ZRF_NIBBLE(state->memory[operand]);
                zrf_refresh_zero(state);
                break;
            case 0xEu: {
                zrf_u8 temporary = state->a;
                state->a = ZRF_NIBBLE(state->b);
                state->b = ZRF_NIBBLE(temporary);
                zrf_refresh_zero(state);
                break;
            }
            case 0xFu:
                state->halted = 1u;
                break;
            default:
                return ZRF_STATUS_BAD_INPUT;
        }
    }

    if (state->halted != 0u) {
        return ZRF_STATUS_HALTED;
    }
    return ZRF_STATUS_STEP_LIMIT;
}

zrf_u32 zrf_selftest(void) {
    static const zrf_u8 program[] = {
        0x15u,
        0x23u,
        0x30u,
        0xC2u,
        0x18u,
        0x28u,
        0x80u,
        0x90u,
        0xAAu,
        0x1Fu,
        0xD2u,
        0xF0u
    };
    zrf_state state;
    zrf_u32 status;

    zrf_reset(&state);
    status = zrf_run(&state, program, (zrf_u8)(sizeof(program) / sizeof(program[0])), 32u);

    if (status != ZRF_STATUS_HALTED) return 0xE001u;
    if (state.a != 6u) return 0xE002u;
    if (state.memory[2] != 6u) return 0xE003u;
    if (state.ticks != 11u) return 0xE004u;
    return 0u;
}

void zrf_boot(void) {
    zrf_boot_receipt = zrf_selftest();
}
