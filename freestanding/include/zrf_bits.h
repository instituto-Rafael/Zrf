#ifndef ZRF_BITS_H
#define ZRF_BITS_H

typedef unsigned char zrf_u8;
typedef unsigned int zrf_u32;

enum zrf_status {
    ZRF_STATUS_HALTED = 0u,
    ZRF_STATUS_BAD_INPUT = 1u,
    ZRF_STATUS_PC_OOB = 2u,
    ZRF_STATUS_STEP_LIMIT = 3u
};

typedef struct zrf_state {
    zrf_u8 a;
    zrf_u8 b;
    zrf_u8 zero;
    zrf_u8 halted;
    zrf_u8 pc;
    zrf_u8 memory[16];
    zrf_u32 ticks;
} zrf_state;

void zrf_reset(zrf_state *state);
zrf_u32 zrf_run(zrf_state *state, const zrf_u8 *code, zrf_u8 code_size, zrf_u32 max_steps);
zrf_u32 zrf_selftest(void);
void zrf_boot(void);
extern volatile zrf_u32 zrf_boot_receipt;

#endif
