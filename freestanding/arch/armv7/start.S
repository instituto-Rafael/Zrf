.syntax unified
.section .bss.zrf_stack,"aw",%nobits
.balign 8
zrf_stack_bottom:
    .skip 4096
zrf_stack_top:

.section .text.boot,"ax",%progbits
.global _start
.type _start,%function
_start:
    ldr sp, =zrf_stack_top
    bl zrf_boot
1:
    wfi
    b 1b
.size _start, .-_start
