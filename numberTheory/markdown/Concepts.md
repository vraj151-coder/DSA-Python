# Number Theory Concepts

## Trailing Zeroes

Trailing zeroes can also be calculated by calulated by knowing number of pairs of 2 and 5
The number of 5's are less than number of 2's so we simply need to count number of 5's in prime factorization

>$Trailing zero count = \lfloor(n/5)\rfloor + \lfloor(n/25)\rfloor + \lfloor(n/125)\rfloor + .... \lfloor(n/i)\rfloor$

Initially=5 then i*=5 till i<=n

## GCD

GCD also has relation with tiling problem.
If a rectangle is of size a*b then largest square filling all rectangle is of size GCD(a,b)

#### Euclid Algorithm

$if a>b gcd(a,b)=gcd(a-b,b)$

$gcd(a,b)=gcd(b,a\%b)$

### LCM

$ LCM(a,b) = a*b/GCD(a,b)$

### Divisors of Number

Divisors always appear in pair

if $(x,y)$ is a pair 

$30: (1,30) ,(2,15) ,(3,10),(5,6)$
$65: (1,65) ,(5,13)$

$x*y=n$

And if x<y  
x*x<=n  
x<=$\sqrt{n}$  

**So $x<=\sqrt{n}$ and $y>=\sqrt{n}$**

#### Prime Numbers

>So if we have to check for prime numbers we dont have to check for divisors till $n$ we have to check only till $\sqrt{n}$

### <a href="https://www.geeksforgeeks.org/sieve-of-eratosthenes/" target="_blank" title="GFG article">Seive of Eratosthenes</a>

