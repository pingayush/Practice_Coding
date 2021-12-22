import math
a = math.ceil(1.03)  #the ceil() function returns the smallest integer not less than 1.03
print(a)
b =  math.sqrt(4.0) #the sqrt() function returns the square root  of 4.0
print(b)
c = math.exp(2.0) # the exp() function returns the natural log e  raised  to the 2.0
math.fabs(1.0) # the fabs() function returns the absolute valule of 1.0
math.floor(1.03) #the floor() function returns the largest integer not greater than  1.03
math.pow(2,2) #the pow(base,exp) function returns  base raised to the exp power
math.log()Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> math.ceil(2.9)
3
>>> math.sqrt(256)
16.0
>>> math.exp(10)
22026.465794806718
>>> math.exp(2)
7.38905609893065
>>> math.fabs(-11112)
11112.0
>>> math.floor(2.9)
2
>>> math.log(2[10])
<stdin>:1: SyntaxWarning: 'int' object is not subscriptable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> math.log(2,[10])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be real number, not list
>>> math.log(2,4)
0.5
>>> math(2,8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> math.log10(10)
1.0
>>> math.log10(2)
0.3010299956639812
>>> math.log10(3)
0.47712125471966244
>>> math.log10(4)
0.6020599913279624
>>> math.sin(30)
-0.9880316240928618
>>> maths.sin(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'maths' is not defined
>>> math.sin(0)
0.0
>>> math.sin(45)
0.8509035245341184
>>> math.cos(45)
0.5253219888177297
>>> math.tan(45)
1.6197751905438615
>>> math.radians(45)
0.7853981633974483
>>> math.tan(0.785)
0.9992039901050427
>>> math.tan(0.7853981633974483)
0.9999999999999999
>>> math.pow(2,5)
32.0
>>> import random
>>> print(random.random())
0.49921147077752936
>>> print(random.random())
0.37563049065030696
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> random.range(45)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'random' has no attribute 'range'
>>> random.randrange(45)
37
>>> random.randrange(45)
19
>>> random.randrange(21,23)
21
>>> random.randrange(21,23)
22
>>> random.randrange(21,23)
21
>>> random.randrange(21,23)
22
>>> random.randrange(20,40,2)
26
>>>
>>> random.randrange(20,40,2)
36
>>> random.range(20,40,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'random' has no attribute 'range'
>>> random.randrange(20,40,2)
24
>>> print(random.randint(3,10))
7
>>> random.randint(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: randint() missing 1 required positional argument: 'b'
>>> random.randint(3,10)
5
>>> random.randint(3,100)-3)
  File "<stdin>", line 1
    random.randint(3,100)-3)
                           ^
SyntaxError: unmatched ')'
>>> print(random.randint((3,10)-3)
...
...
... import statistics
  File "<stdin>", line 4
    import statistics
    ^
SyntaxError: invalid syntax
>>> import statistics
>>> a=[1,2,3,4,5]
>>> statistics.mean(a)
3
>>> statistics.median(a)
3
>>> statistics.mode(a)
1
