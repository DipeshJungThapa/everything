Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: C:/python/comprehensions.py =====================
Squares : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> square = []
>>> for num in range(10):
...     squares.append(num**2)
... 
>>> print("Squares :", squares)
Squares : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> square = []
>>> [x**2 for x in range (20)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
>>> even_comp = [x for x in range(10) if x % 2 == 0]
... print("[x for x in range(10) if x % 2 == 0] >> ",even_comp) 
... #[0, 2, 4, 6, 8]
... 
... cube_squares = [x**2 if x % 2 == 0 else x**3 for x in range(10)]
SyntaxError: multiple statements found while compiling a single statement
>>> even_comp = [x for x in range(10) if x % 2 == 0]
... print("[x for x in range(10) if x % 2 == 0] >> ",even_comp)
SyntaxError: multiple statements found while compiling a single statement
>>> print("p[x for x in range(10) if x % 2 == 0] >> ",even_comp)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("p[x for x in range(10) if x % 2 == 0] >> ",even_comp)
NameError: name 'even_comp' is not defined
>>> print("\nDict CUBES : ",{x: x**3 for x in range(10)})
... print("Dict CUBES EVEN: ",{x: x**3 for x in range(10) if x**3 % 2 == 0})
... 
SyntaxError: multiple statements found while compiling a single statement
>>> print(Dict cube: ",{x " x ** 3 for x in range (10)})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> print(Dict cube: ",{x  x ** 3 for x in range (10)})
...       
SyntaxError: unterminated string literal (detected at line 1)

=============================================================== RESTART: C:/python/comprehensions.py ==============================================================
0  ::  1
1  ::  5
2  ::  9
3  ::  13
4  ::  17
5  ::  21
6  ::  25
7  ::  29
8  ::  33
9  ::  37
10  ::  41
11  ::  45
12  ::  49
13  ::  53
14  ::  57
15  ::  61
16  ::  65
17  ::  69
18  ::  73
19  ::  77
20  ::  81
21  ::  85
22  ::  89
23  ::  93
24  ::  97

==================== RESTART: C:/python/comprehensions.py ===================
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print([str(i) for i in range(10)])

['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(i for i in range(10)])

SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print(i for i in range(10))
<generator object <genexpr> at 0x00000273AF2EFAC0>
print([i for i in range(10])
      
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print([i for i in range(10)])
      
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(i for i in range(10)])
print(i for i in range(10)])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print([str(i) for i in range(10)])
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
i = map(str,range(10))

print(list(i))

['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(i for i in range(10))
<generator object <genexpr> at 0x00000273AF2EFAC0>
print[i for i in range(10)]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
