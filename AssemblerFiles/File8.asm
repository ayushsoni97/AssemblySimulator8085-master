ORIGIN:
MOV A, a
MOV B, c
ADD B
MOV d, A
MOV A, d
LI D, 2
MOV C, d
SYSCALL
MOV A, y
MOV B, r
SUB B
MOV y, A
a DB  5
c DB  8
d DB  0
r DB  4
y DB  3
END:
