.section .bss.zrf_stack,"aw",%nobits
.balign 16
zrf_stack_bottom:
    .skip 4096
zrf_stack_top:

.section .text.boot,"ax",%progbits
.global _start
.type _start,%function
_start:
    adr x0, zrf_stack_top
    mov sp, x0
    bl zrf_boot
1:
    wfe
    b 1b
.size _start, .-_start
