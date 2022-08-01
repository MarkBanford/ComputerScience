A bit shift is a bitwise operation where the order of several bits is moved, either to the left or right,
to efficiently perform a mathematical operation. Bit shifts help with optimization in low-level programming because
they require fewer calculations for the CPU than conventional math

AND             &
OR              |
XOR             ^
NOT             ~
LEFT SHIFT      <<
RIGHT SHIFT     >>


AND - Only if both are True

0 & 0 = 0
1 & 0 = 0
0 & 1 = 0
1 & 1 = 1

OR - True if any bit is true

0 | 0 = 0
1 | 0 = 1
0 | 1 = 1
1 | 1 = 1

XOR - True if only 1 bit is true, i.e ensuring both are different

0 ^ 0 = 0
1 ^ 0 = 1
0 ^ 1 = 1
1 ^ 1 = 0


LEFT SHIFT

Each shift left is multiplying by 2

00010110  #Must be even number as there is a zero in the 1's column
<<
01011000


BIT Manipulation
We want to take a string of binary digits and we want to set one of them to true


