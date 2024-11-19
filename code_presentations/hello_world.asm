section .data
    hello db 'Hello, World!', 0x0A  ; Cadena a imprimir con salto de línea al final
    hello_len equ $ - hello          ; Longitud de la cadena

section .text
    global _start                    ; Punto de entrada del programa

_start:
    ; Llamada al sistema write (sys_write)
    mov rax, 1                       ; Código de sys_write (1)
    mov rdi, 1                       ; Descriptor de archivo para salida estándar (stdout)
    mov rsi, hello                   ; Dirección de la cadena a imprimir
    mov rdx, hello_len               ; Longitud de la cadena
    syscall                          ; Llamada al sistema

    ; Llamada al sistema exit (sys_exit)
    mov rax, 60                      ; Código de sys_exit (60)
    xor rdi, rdi                     ; Código de salida 0
    syscall                          ; Llamada al sistema
