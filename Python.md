# Python

> - print('hello')
> - print(2)

> string => ' ' or " "

> "hello "world"" ❌  
> "hello \"world\"" ✅  
> "hello 'world'" ✅

> ### escape sequence

> 1.\'  
> 2.\"  
> 3.\\\\
> 4.\n  
> 5.\t

> #this is how to comment

> raw string => print(r"line A \n line B")  
> this will trest escape sequence as normal text

> arithmetic operator:  
> $+ ,- ,*,/,//,**$,%

> print(round(2\*\*0.5,4))

> variable:  
> x=5  
> y='xyz'

> variable naming rules:  
> 1.can use alphanumeric character and \_  
> 2.cannot start with number

> Naming converntion : use snake case

> String concatenation =>  
> full_name="vraj"+" "+"parikh"
> print(full_name+21) ❌
> print(full_name+"21") ✅

> Input =>  
> Always takes input in the form of string  
> name=input("Enter your name")  
> age=int(input("Enter your age"))

> Multiple variable declaration =>  
> name,age="vraj",20
> x=y=z=1

> Two or more input one line =>  
> name,age=input("enter name and age").split()

> string formatting =>  
> name="vraj"  
> age=20  
> print(f"Hello {name} your age is {age+1}")

> String indexing =>  
> name="vraj"  
> print(name[2])  
> print(name[-1])

> String is immutable

> String slicing  
> syntax=> [start:stop:step]  
> lang="python"  
> print(lang[0:2]) #py  
> print(lang[-3:6]) #hon  
> print(lang[:]) #full string  
> print(lang[2:]) #thon  
> print(lang[:3]) #pyt  
> print("Vraj"[1::2]) #rj  
> print("maut"[2::-1]) #uam
> print(lang[::-1]) #reverse string

> len() function can be used on any iterable

> String methods:  
> upper()  
> lower()  
> title() -> first letter capital rest small  
> count()  
> -print("vraj".count("v"))  
> lstrip()  
> rstrip()  
> strip()  
> replace()  
> -name="vraj".replace("v","V")  
> -can also pass extra argument about how many maximum to be replaced
> -str.replace("is","was",1)  
> center()  
> find(value,start,end)  
> start and end are optional  
> print("vraj".find("a",3))

> assignment operator  
> =  
> +=  
> -=  
> \*=  
> /=  
> %=  
> //=  
> \*\*=  
> &=  
> |=  
> ^=  
> &gt;&gt;=  
> <<=

> if (condition1):  
> &nbsp;&nbsp;&nbsp;&nbsp;#code  
> elif (condition2):  
> &nbsp;&nbsp;&nbsp;&nbsp;#code  
> else:  
> &nbsp;&nbsp;&nbsp;&nbsp;#code

> == to check equality

> if you do not want to write code inside a block use pass statement  
> x=18  
> if x>18:  
> &nbsp;&nbsp;pass

> 'and' 'or' operator for conditional checking

## 'in' keyword:

```python
clg="Parul"
if "a" in clg:
    print("a is present in clg")
```

> 'in' can be used on any iterable like string,list,set etc.

## Check empty or not:

```python
name="abc"
if name:
    print("Nice name")
else:
    print("You have no name")
```

> while(condition)  
> &nbsp;&nbsp;&nbsp;&nbsp;#code

## **range function :**

**syntax => range(start,stop,step)**

```python
for i in range(11)
    print(i) #0 to 10
for i in range(2,21)
    print(i) #2 to 20
for i in range(0,11,2)
    print(i) #0,2,4,6,8,10
for i in range(1,-11,-1)
    print(i) #1 to -10
```

> we cannot have multiply expression in for loop so for that we have to use while loop

> looping trough iterables using for loop:

```python
name="vraj"
for ch in name:
    print(ch)
```

## Functon

```python
    def add_two(a,b):
        return a+b
    def print_num(a=10,b=20): #default argument
        print(a,b)
```

## Type of variable:

```python
x=5               #global variale
def func():
    x=7           #local variable
    return x
```
