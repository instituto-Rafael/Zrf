.section .bss.zrf_stack,"aw",@nobits
.balign 16
zrf_stack_bottom:
    .skip 4096
zrf_stack_top:

.section .text.boot,"ax",@progbits
.global _start
.type _start,@function
_start:
    lea zrf_stack_top(%rip), %rsp
    xor %rbp, %rbp
    call zrf_boot
1:
    hlt
    jmp 1b
.size _start, .-_start
