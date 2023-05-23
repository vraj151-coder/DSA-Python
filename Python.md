# Python

> - print('hello')
> - print(2)

> string => ' ' or " "

> "hello "world"" ❌  
> "hello \"world\"" ✅  
> "hello 'world'" ✅

> Primitive data types:  
> 1.int  
> 2.float  
> 3.boolean (True False)  
> 4.String  
> 5.None

> ### escape sequence
>
> 1.\\'  
> 2.\\"  
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

> String concatenation :  
> full_name="vraj"+" "+"parikh"  
> print(full_name+21) ❌  
> print(full_name+"21") ✅

> Input function :  
> Always takes input in the form of string  
> name=input("Enter your name")  
> age=int(input("Enter your age"))

> Multiple variable declaration :  
> name,age="vraj",20  
> x=y=z=1

> Two or more input one line :  
> name,age=input("enter name and age").split()

> ### **string formatting =>**
>
> name="vraj"  
> age=20  
> print(f"Hello {name} your age is {age+1}")

> ### **String indexing =>**
>
> name="vraj"  
> print(name[2])  
> print(name[-1])

> String is immutable

> ## **String slicing**
>
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

> ## **String methods:**
>
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
> -"vraj".center(8,"\*") #\*\*vraj\*\*  
> find(value,start,end)  
> start and end are optional  
> print("vraj".find("a",3))

> ### **Assignment operators :**
>
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

> ## while loop:
>
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

> we cannot use multiply expression in for loop so for that we have to use while loop

## **looping trough iterables using for loop:**

```python
name="vraj"
for ch in name:
    print(ch)
```

## Function

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

# **List**

- ordered collection of items and can store anything
- slicing can also be used here
- List are mutable unlike string

```python
mixed=[1,2.1,"Hello",None]
print(mixed[:3])
print(mixed[1:])
```

```python
arr=[]
arr[:]="xyz"  # 0->x,1->y,2->z
arr[1:]=['three','four'] # 0->x,1->'three',2->'four'
```

- ## Methods

append  
insert  
concatenation  
extend  
pop  
del keyword  
remove  
count  
sort  
sorted function  
clear  
copy  
reverse

```python
nums=[1,2,3,4,5]

nums.append(4) # add element at last

nums.insert(0,"Hola")

fruits1=['mango','orange']
fruits2=['grapes','apple']
fruits=fruits1+fruits2

fruits1.extend(fruits2) #if we do append it will add list in list,extend will append items of fruits2 in fruit1

fruits.pop() #removes last element and returns it
fruits.pop(1) #removes element at index 1

del fruits[1]

fruits.remove('apple')

fruits.count('apple')

fruits.sort() #sorts alphabetically or numerically

sorted(nums) #does not modify original

nums.clear() #empties the list

nums.copy() #returns copy of list

nums.reverse() #modifies original list
```

### **index method**

syntax : (value,start,stop)

```python
list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
print(list2.index(''cat,3,14))
```

### **Split method**

converts string to list

```python
name,age=input("enter your name and age").split(",")
```

### **Join method**

converts list to string

```python
user_info=['vraj','21']
print(','.join(user_info))   # vraj,21
```

### **Compare List**

== V/s is

```python
    list1=[1,2,3]
    list2=[1,2,3]
    print(list1==list2) #True
    print(list1 is list2) #False
```

### **generate list with range**

```python
numbers=list(range(1,11))
```

### **min and max functions**

```python
print(min(numbers))
print(max(numbers))
```

# **Tuple**

- ordered collection of data
- can store any data
- tuples are immutable,once created it cannot be changed
- tuple is faster than list
- It is used when we know that contents inside it will not change like days of week etc.

- tuple with one element

```python
    nums1=(1)
    nums2=(1,)
    print(type(nums)) #int
    print(type(nums2)) #tuple
```

- tuple without parenthesis

```python
    guitars='yamaha','taylor'
    print(type(guitars)) #tuple
```

- tuple unpacking

```python
    nums=(1,2,3)
    num1,num2,num3=nums  ✅
    num1,num2=nums       ❌
```

- list inside tuple can be modified

- min(),max()and sum() function

- count() and index() methods

- function returning two values

```python
    def fun(a,b):
        return a,b #tuple
```

---

```python
    nums=tuple(range(1,11))
```

# **Dictionary**

- unordered collection of data in key value pair

- no indexing in dictionary

- can store number,string,list,dictionary etc.

- key=> string or int

```python
    user={
        'name':'Vraj',
        'age':20
        }
    print(user['name'])

    user_info={}       # adding data to empty dict
    unser_info['name']='vraj'
```

- adding data to dictionary :

```python
    user_info2={}
    user_info2['age']=21
```

- check if key exist :

```python
    if 'age' in user_info2:
        print("Present")
    else:
        print("absent")
```

- check if value exist :

```python
    if 21 in user_info2.values():
        print("Present")
    else:
        print("absent")
```

- looping through dictionary :

```python
    for key in user_info:
        print(key)                       # print keys
    for key in user_info:
        print(user_info[key])           # print values
    for val in user_info.values():
        print(val)                      # print values
```

- values() method return object of dict_values.It is similar to list but you can not add or delete data , we can only iterate

- similarly keys() method return object of dict_keys

### **items method**

items() method contain list of tuples which are key value pair and returns object of dict_items  
[(),(),()...]

```python
    for key,value in user_info.items():
        print(key,value)
```

### **pop method**

```python
    popped_item=usr.pop('fav_music') # removes and return the value of key deleted
```

### **update method**

```python
    user_info={
        'name':'vraj',
        'age':21,
        'college':'PIT'
    }
    more_info={
        'sports':['cricket','football'],
        'name':'Vraj'
    }
    user_info.update(more_info)
```

if the key already exists, it updates the value of key

### **get method**

does not give error if key does not exist

```python
    print(user_info.get('name')) # returns None if not found
    print(user_info.get('lname','not found')) #return 'not found' if not found
```

### **clear and copy method**

```python
    usr_cpy=user_info.copy()
    user_info.clear()
```

### **two same keys in dictionary**

```python
    user={'name':'vraj','age':20,'age':21} #age with 21 value will be stored
```

# **Sets**

- unordered collection of unique items
- no index based access
- cannot store list and dictionary
- declared as {}

### **To get unique items from list**

```python
    l=[1,2,3,2,2,3,4,3,3,2,2,4]
    unique_list=list(set(l))
```

### **Set methods:**

1. add()
1. remove() #throws error if element not present
1. discard() #does not throw error if element not present
1. clear()
1. copy()

> for loop and 'in' keyword can be used like in list

### **Set Maths**

```python
    s1={1,2,3,4}
    s2={3,4,5,6}

    set_union= s1|s2

    set_intersection= s1&s2
```

## **List Comprehension**

With the help of list Comprehension we can generate list in one line

```python
    list_square=[i**2 for i in range(1,11)] #1,4,16,25,36,49,64,81,100
```

## **List Comprehension with if statement**

```python
    even_nums=[i for i in range(1,11) if i%2==0]
```

## **List Comprehension with if else statement**

```python
    nums=[i**2 if i%2==0 else -i for i in range(1,7)]
    # -1,4,-3,16,-5,36
```

## **List Comprehension with nested list**

```python
    nested_list=[[i for i in range(1,4)] for j in range(3)]
```

# **Dictionary Comprehension**

```python
    square={num:num**2 for num in range(1,11)}

    name='alpana'
    count_characters={char:name.count(char) for char in name}
```

## **Dictionary Comprehension with if else statement**

```python
    odd_even={i:('even' if i%2==0 else 'odd') for i in range(11)}
```

# \* args

We can pass multiple argument and the \* operator will convert them into tuple

```python
    def sum_nums(*args):
        sum=0
        for val in args:
            sum+=val
        return sum
    print(sum_nums(1,2,3,4,5))
```

> \*args should be the last parameter if used with normal parameter

### **list as parameter to \*args**

> we can use \* to unpack contents of list,tuple

```python
    def sum_num(*args):
        sum=0
        for val in args:
            sum+=val
        return
    array=[1,8,4,6]
    print(sum_num(*array)) #unpack
```

## \*\*kwargs (keyword argument)

1. **kwargs as parameter**

```python
    def func(**kwargs):
        print(kwargs)
    func(fname='vraj',lname='parikh')
```

Like in args, here we can use \*\* to unpack dictionary

**the order of normal paramater,default parameter,\*args,kwargs should be like**

```python
def fun(name,*args,last_name='unknown',**kwargs)
```

## Lambda Expression (anonymous function)

Used with built in functions like map,filter,reduce etc.

```python
    add=lambda a,b : a*b

    #lamda wth if else
    even_odd = lambda num : 'even' if num%2==0 else 'odd'
```

## **Enumerate Function**

```python
    for pos,name in enumerate(names):
        prinnt(f"{pos}---->{name}")
```

## **Map Function**

```python
    nums=[1,2,3,4]
    square_num=list(map(lambda x:x**2,nums)) #returns map object which is iterator
```

> **_Map is generally used with built in function. Otherwise comprehension is used_**

```python
    names=['abc','vraj','demo']
    name_len=list(map(len,names))
```

## **_Filter function_**

function passed should return True or False and if True item is added

```python
    even_nums=list(filter(lambda x:x%2==0,nums))
```

## **_Iterator v/s Iterable_**

```python
    numbers=[1,2,3,4] #iterables
    squares=map(lambda n:n**2,numbers) #iterators
```

> When for loop is run iter() method is called on list which returns iterator and then next() method is called repeatedly to extract items in list.  
> However in case of map object it is already iterator so next() method is called repeatedly.

> **We can loop through iterators only once after that it will not work**

## **_Zip function_**

- combines two lists into lists of tuples

- list containg tuple of size 2 can be converted into dictionary

```python
    usr_id=['user1','user2']
    name=['vraj','parikh']

    print(dict(zip(usr_id,name))) #{'user1': 'vraj', 'user2': 'parikh'}
```

## **_Zip function Part2_**

## **_Any and All function_**

All function returns **_True_** if every element of list contains **_True_**  
Any function returns **_True_** if atleast 1 element of list contains **_True_**

```python
    nums=[1,2,5,3,19,23]

    print(all([i%2==0 for i in nums]))  #False

    print(any([i%2==0 for i in nums]))  #True
```

## **_Advanced Min And Max Function_**

```python
    names=['vraj','harsh','rudra']
    print(max(names, key=lambda name:len(name))) #maximum name length item

    students=[
        {'name':'vraj',
        'score':80
        },
        {'name':'harsh',
        'score':80
        },
        {'name':'rudra',
        'score':90
        },
    ]
    print(max(students,key=lambda item:item.get('score')).get('name')) #maximum score student name
```

**_when looping though object we will get value of key_**

```python
    students={
        'vraj':{'score':90 ,'age':21},
        'rudra':{'score': 85,'age':20},
        'harsh':{'score': 84,'age':20}
    }
    print(max(students,key=lambda item:students[item].get('score')))
    #item will get printed
```

## **_Sorted Function_**

- The sort method is not available in tuple .In tuple we have to use sorted function

- The sorted function does not change the object .It returns new one

```python
    noodles=[
        {'name':'maggi',
        'price':14
        },
        {'name':'gippi',
        'price':10
        },
        {'name':'yippi',
        'price':10
        }
    ]
    print(sorted(noodles,lambda d:d.get('price'))) #returns list in sorted order
    print(sorted(noodles,lambda d:d.get('price'),reverse=True))
```

## **_Docstring_**

- We use triple single quote or double quote for docstring

```python
    def add(a,b):
        '''this function takes 2 numbers and returns their sum'''
        return a+b

    print(add.__doc__)

    print(help(sum))
```

### **_function returning function_ (Closure)**

- Function declared can be assigned to a variable as variable will also point to exact memory location where function is stored

```python
    def outer_func(msg):
        def inner_func():
            print(f"message is {msg}")
        return inner_func

    var=outer_func('Hello')
    var()
```

```python
    def to_power(x):
        def calc_power(n):
            return n**x
        return calc_power

    cube=to_power(3)
    print(cube(5))

    square=to_power(2)
    print(square(5))
```

## **_Decorator_**

- enhance the functionality of other functions

```python
def decorator_fun(any_function):
    def inner():
        any_function()
        print("this is cool")
    return inner

def func1():
    print("hello there")

func1=decorator_fun(func1)
func1()

@decorator_fun     #shortcut for func2=decorator_fun(func2)
def func2():
    print("Good ebening")

func2()
```

- This decorator function is still not complete

```python
    def decorator_fun(any_function):
        def inner(*args,**kwargs):
            print("this is cool")
            return any_function(*args,**kwargs)
        return inner

    @decorator_fun
    def add(a,b):
        return a+b

    @decorator_fun
    def func(a):
        return f'this is func function with argument {a}'

```

## **_Generator_**

- generators are iterators

> list=[1,2,3,4]  
> memory ----> [...............................]  
> &nbsp;&nbsp;&nbsp;&nbsp;in case of list all element stored in memory  
> memory ----> 1  
> &nbsp;&nbsp;&nbsp;&nbsp;while in case of generator only single element is stored which it returns when next() is called

- so if we want to use a sequence only 1 time use generator as it saves memory

```python
    def nums(n):
        for i in range(1,n+1):
            yield(i)

    numbers=nums(10)

    for num in numbers:
        print(num)

    for num in numbers:
        print(num)          #nothing will be printed

    for num in nums(15):
        print(num)          #1 to 15 will be printed
```

### **_Generator Comprehension_**

square=(i\*\*2 for i in range(11)) #iterator

## **_OOP_**

- It is convention to keep start class name as capital in user defined classes.

- The classes by python start with small letter

- init method is the constructor of python

```python
    def Person:
        def __init__(self,first_name,last_name,age):
            #here instance variable is initialized
            self.first_name=first_name
            self.last_name=last_name
            self.Age=age
    p1=Person('vraj','parikh',21)
```

### **_Instance method_**

- in any function inside class first parameter is self
- we dont need to pass self argument.Python does it for us

```python
    class Person:
        def __init__(self,first_name,last_name,age):
            #here instance variable is initialized
            self.first_name=first_name
            self.last_name=last_name
            self.Age=age

        def full_name(self):    #instance method
            return f"{self.first_name} {self.last_name}"

    p1=Person('vraj','parikh',21)

    print(p1.full_name())
    #Internally Person.full_name(p1) this happens
```

### **_Class variable_**

```python
    class Circle:
        pi=3.14
        def __init__(self,radius):
            self.radius=radius
        def circumference(self):
            return 2*Circle.pi*self.radius
```

**IMP**

```python
    class Laptop:
        discount=10
        def __init__(self,brand,price):
            self.brand=brand
            self.price=price
        def get_discount_price(self):
            off_price=(price*self.discount)/100
            #if discount instance variable is present then that value will be taken else class variable value will be taken
            return price-off_price

    l1=Laptop('asus',70000)
    l2=Laptop('hp',60000)

    l1.discount=30
    print(l1.get_discount_price()) #here discount will be 30
    print(l2.get_discount_price()) #here discount will be 10
```

### **_Class Methods_**

```python
    class Demo:
        def __init__(self):
            pass
        @classmethod
        def fun(cls):
            print('You have called a class method of {cls.__name__} class')
```

### **static method**

- static method has no relation with class or instance but might have logical connection

```python
    def Demo:
        def __init__(self):
            pass
        @staticmethod
        def fun():
            print('Hello from static method')
```

### **_naming convention_**

> In python every thing is public  
> But however we can start the name with \_ to tell other developers to consider this is as private (do not change) property/method

> \_name -> private  
> \_\_name\_\_ -> dunder methods or magic methods

### **_Name mangling_**

- Not a convention
- \_\_name -> name mangling

```python
    def Demo:
        def __init__(self,name):
            self.__name=name
```

- this just changes the name of property/method to \_className\_\_propertyOrMethodName

## **_property and setter decorator_**

```python
    def Demo:
        def __init__(self,price):
            self._price=price
        @property
        def price(self):
            print(f'The price is {self._price}')
        @price.setter
        def price(self,new_price):
            self._price=max(new_price,0)

    d=Demo(100)
    d.price=300
    print(d.price)
```

## **_Inheritance_**

```python
   class Person:
       def __init__(self,name,age):
           self.name=name
           self.age=age
       def display_name(self):
           print(f'Name is {self.name}')
    class Student(Person):
       def __init__(self,eid,name,age):
           super().__init__(name,age)
           self.eid=eid
```

- Python supports multiple and multilevel inheritance as well

### **_Method resolution order_**

- It is the order in which python searches for methods or instance variable

- It can be seen by

1. print(help(class_name))
1. print(class_name.mro())
1. print(class_name.\_\_mro\_\_)

### **_Method Overriding_**

```python
    class Animal:
        def __init__(self,name):
           self.name=name
        def display_name(self):
           print(f'Name is {self.name}')
        def sound(self):
            print('...')

    class Dog(Animal):
        def __init__(self,eid,name,age):
           super().__init__(name,age)
           self.eid=eid
        def sound(self):
            print('Boww..Boww')
```

### **_isinstance() and issubclass() method_**

```python
    print(isinstance(oneplus,Smartphone))
    print(issubclass(Smartphone,Phone))  #To check if smartphone is subclass of phone
```

## **_Magic / Dunder Methods_**

- Syntax -> \_\_name\_\_

- str and repr are used to print user defined object

- str has higher priority

```python
    class Person:
        def __init__(self,fname,lname,age):
            self.fname=fname
            self.lname=lname
            self.age=age
        #for users
        def __str__(self):
            return f"{self.fname} {self.lname}"
        #for developers
        def __repr__(self):
        #generally used to represent the object so that one can copy and get entire object
            return f"Person('{self.fname}','{self.lname}',{self.age})"

    p1=Person('vraj','parikh',21)
    print(p1)  #str will be called
    print(str(p1))
    print(repr(p1))
```

- \_\_len\_\_ method can be used to return length

```python
    class Person:
        def __init__(self,fname,lname,age):
            self.fname=fname
            self.lname=lname
            self.age=age
        def __len__(self):
            return len(self.fname)

    p1=Person('vraj','parikh',21)
    print(len(p1))
```

### **_operator overloading by dunder methods_**

![operator overloading](https://www.codespeedy.com/wp-content/uploads/2019/08/Table.jpg)

## **_Exception Handling_**

- **Types of Error:**

![Python Error Types](https://2.bp.blogspot.com/-jH5MCdfa8Zo/Vb5Mg_pD-nI/AAAAAAAAInU/mJ0hTsRKGjc/s1600/exception.PNG "Types of error in python")

- To throw an error use raise keyword

```python
    def add(a,b):
        if type(a) != int or type(b) != int:
            raise TypeError('Wrong Data Type Passed')
        return a+b
```

```python
    class Animal:
        def __init__(self,name):
           self.name=name
        def sound(self):  # python version of abstract method
            raise NotImplementedError('you have to define this method in subclass')
        # Forces subclass to implement this method

    class Dog(Animal):
        def __init__(self):
           super().__init__(name)
        def sound(self):
            print('Boww..Boww')
```

### **_try except else finally_**

```python
    while True:
        try:
            age=int(input('Enter your age: '))
            break
        except ValueError as err: #only runs when error is of type ValueError
            print(f'You did not enter integer. {err}')
        except:
            print('Unexpected error ...')
        else: # runs if no exception occurs
            if age>18:
                print('you can play this game')
            else:
                print('you can\'t play this game')
        finally: #always runs whether exception occurs or not
            print('Program Over')
```

### **_custom exception_**

- We do this to increase readability of code

```python
    class NameTooShortError(ValueError):
        pass

    def validate(name):
        if len(name) < 8:
            raise NameTooShortError('name is too short')

    usr_name=input('Enter your name : ')
    validate(usr_name)
    printf(f'Hello {usr_name}')

```

## **_File Handling_**

- open function
- read method
- seek method
- tell method
- readline method
- readlines method
- close method

```python
    f=open('file.txt','r')  #by default it is read mode
    #provide absolute or relative path of file
    print(f'cursor position is at {f.tell()}')
    print(f.read())
    print(f'cursor position is at {f.tell()}')
    print(f.read())   #Nothing will be printed
    f.seek(0)  #sets value of cursor position
    print(f.read()) #now outputs entire content of file
    f.seek(0)
    print(f.readline())  #outputs single line
    f.seek(0)
    lines=f.readlines() #returns list of lines of type string
    f.close()
    print(f.name) #returns file names
    print(f.closed) #returns bool if file is closed or not
    for line in f:
        print(line,end="")
```

### **_with block_**

```python
    with open('file.txt') as f:  #auto close after block
        print(f.read())
```

### **_modes in file handling_**

1. r -> read
1. w -> write
1. a -> append
1. r+ -> read and write

If file not present it creates it in w,a mode

```python
    with open('file.txt','w') as f:
        f.write('hello') #overrides the whole content

    with open('file.txt','a') as f:  #append
        f.write('Bye')

    with open('file.txt','r+') as f:
        f.seek(len(f.read()))
        f.write('Bye')
```

```python
    with open('file1.txt','r') as rf:
        with open('file2.txt','w') as wf:
            wf.write(rf.read())
```

## **_Function Annotation_**

- just a way to add additional notes or comments to the code that would help others know what is going on and understand your code

- It does not affect the actual code

```python
    def sum(a:list[int],b:list[int])->list[int]:
    return a+b

    print(sum.__annotations__)
```

## **_Import statement_**

A module is a file containing written code that can be imported and used in our program.

### Types of module:

1. Built modules: Pre-installed in Python

1. External modules: Need to be installed

- Using import statement :

```python
    import import_file

    import_file.func1()
    import_file.func2()
```

- Using from import statement :

```python
    from import_file import func1
    from import_file import func2

    func1()  # here we can call functions without referencing module name
    func2()
```

### **_To import module not in same directory_**

```python
    import sys
    sys.path.append(/home/vraj/documents/module_name)
    import module_name
```

## **\_\_\_main\_\_\_**

- When python runs a file it initializes special variables.\_\_name\_\_ is one of them

- The current file which is running has \_\_name\_\_ set to \_\_main\_\_ else it has value of the file_name

- Whenever we import a module, python first runs the code

```python
    if __name__ == '__main__':
        #code
```

**_By doing this if the module has this inside it and then the code inside it will not run if it is ran from import statement from another file_**
