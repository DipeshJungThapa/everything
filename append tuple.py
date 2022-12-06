Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========================== RESTART: C:/python/tuple.py =========================
t=("apple",3.14,75)
a,b,c=t
print("a")
a
a
'apple'
b
3.14
c
75
a.upper
<built-in method upper of str object at 0x000001C946549A30>
a.upper()
'APPLE'
a.lower()
'apple'
a.title()\
a.title()
SyntaxError: invalid syntax
a.title()
'Apple'
del t
a.title()
'Apple'
del t
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    del t
NameError: name 't' is not defined
a.title()
'Apple'
del t
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    del t
NameError: name 't' is not defined
t=("ball",f,34)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t=("ball",f,34)
NameError: name 'f' is not defined
t=("ball",f,34)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t=("ball",f,34)
NameError: name 'f' is not defined
del t
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    del t
NameError: name 't' is not defined
t=("ball",3,34)
del t
a.title()
'Apple'
del a
a
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a
NameError: name 'a' is not defined
a.title()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.title()
NameError: name 'a' is not defined
l=(2,4,5,6,7,35)
min(l)
2
l.append(20)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l.append(20)
AttributeError: 'tuple' object has no attribute 'append'
dir l
SyntaxError: incomplete input
dirl
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dirl
NameError: name 'dirl' is not defined. Did you mean: 'dir'?
dir l
SyntaxError: incomplete input
l.append(20)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l.append(20)
AttributeError: 'tuple' object has no attribute 'append'
l=(2,4,5,6,7,35)
l.append(20)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l.append(20)
AttributeError: 'tuple' object has no attribute 'append'
l=[2,4,5,6,7,35]
l.append(20)

l.pop(20)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l.pop(20)
IndexError: pop index out of range
l=[2,4,5,6,7,35]
l.append(20)
l
[2, 4, 5, 6, 7, 35, 20]
l.pop()
20
l.remove()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l.remove()
TypeError: list.remove() takes exactly one argument (0 given)
l.remove(2)
l
[4, 5, 6, 7, 35]
help(l.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

l.remove(4)
l
[5, 6, 7, 35]
l.remove(5,6,7)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    l.remove(5,6,7)
TypeError: list.remove() takes exactly one argument (3 given)
\
>>> l.insert(69)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    l.insert(69)
TypeError: insert expected 2 arguments, got 1
>>> l.insert(1,29)
>>> l
[5, 29, 6, 7, 35]
>>> l.pop()
35
>>> l
[5, 29, 6, 7]
>>> l.append()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    l.append()
TypeError: list.append() takes exactly one argument (0 given)
>>> l.append(5)
>>> l
[5, 29, 6, 7, 5]
>>> l.insert(1,29)
>>> l
[5, 29, 29, 6, 7, 5]
>>> l.insert(1,29)
>>> l.insert(1,29)
>>> l
[5, 29, 29, 29, 29, 6, 7, 5]
>>> a.append(29)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.append(29)
NameError: name 'a' is not defined
>>> l.append(29)
>>> 
>>> l
[5, 29, 29, 29, 29, 6, 7, 5, 29]
