ENTRY(_start)
SECTIONS
{
    . = 0x00010000;
    .text : ALIGN(16) { *(.text.boot) *(.text*) }
    .rodata : ALIGN(16) { *(.rodata*) }
    .data : ALIGN(16) { *(.data*) }
    .bss (NOLOAD) : ALIGN(16) { *(.bss*) *(COMMON) }
    /DISCARD/ : { *(.comment*) *(.note*) *(.eh_frame*) *(.ARM.exidx*) *(.ARM.extab*) }
}
