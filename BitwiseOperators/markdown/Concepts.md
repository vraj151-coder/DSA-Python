# Bitwise Operators

![bitwise operator tables](https://www.xsharp.eu/help/images/bitwise-operations.png "bitwise operator tables")

#### Left Shift

$x<<2$ => shifted by 2 bits to left
$x<<y$ => $x*2^y$

#### Right Shift

$x>>y$ => $\lfloor{}x/2^y\rfloor{}$

Rest of the digits in left shift and right shift are padded with 0

### Brian Kerningham's algorithm

&nbsp;&nbsp;&nbsp;n=40 &nbsp;&nbsp;&nbsp;&nbsp; ....101000
n-1=39 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;....100111

When you substract 1 from a number last bit set become 0 and all  the bits which are 0 after last set bit become 1

>n=n&(n-1) removes last set bit of the number

### Power of 2

power of 2 have only 1 bit set

### XOR properties 

x^0 = x
x^y = y^x
x^(y^z)=(x^y)^z
x^x=0

**if there is only 1 odd times occuring element in a list we can xor all of them and the value of xor will be the answer as the even elements cancel each other**