Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========================== RESTART: C:/python/tuple.py =========================
d={'a':"apple",'b':"banana"}
d
{'a': 'apple', 'b': 'banana'}
d(1)=orangaes
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d.(1)=oranges
SyntaxError: invalid syntax
d.{1}=oranges
SyntaxError: invalid syntax
d={'a':"apple",'b':"banana"}
dir
<built-in function dir>
dir(d)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
d[b]=appale
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d[b]=appale
NameError: name 'appale' is not defined
d[b]=appale"
SyntaxError: incomplete input
d[b]="appale"
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d[b]="appale"
NameError: name 'b' is not defined
d["b"]="appale"
d
{'a': 'apple', 'b': 'appale'}
d["c"]=1000
d
{'a': 'apple', 'b': 'appale', 'c': 1000}
d[10]="ten"
d
{'a': 'apple', 'b': 'appale', 'c': 1000, 10: 'ten'}
d[1]=
SyntaxError: incomplete input
{'a': 'apple', 'b': 'appale', 'c': 1000, 10: 'ten'}d[1]=
SyntaxError: invalid syntax
help(d.pop)
Help on built-in function pop:

pop(...) method of builtins.dict instance
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    
    If the key is not found, return the default if given; otherwise,
    raise a KeyError.

d.pop()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.append()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d.append()
AttributeError: 'dict' object has no attribute 'append'
d.pop(10)
'ten'
d
{'a': 'apple', 'b': 'appale', 'c': 1000}
d.pop("apple")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d.pop("apple")
KeyError: 'apple'
d.pop('appple"
      
SyntaxError: incomplete input
KeyError: 'apple')
SyntaxError: unmatched ')'
d.pop('appple")
      
SyntaxError: incomplete input
for x in d :
      print(x)

      
a
b
c


for x,d(x):
      
SyntaxError: incomplete input
for x in d :
      print(x,"--",d[x])

      
a -- apple
b -- appale
c -- 1000







s=
      
SyntaxError: incomplete input
s="python programming"
      
l=list(s)
      
un =set(l)
      
mew s = list(un)
      
SyntaxError: invalid syntax
new s = list(un)
      
SyntaxError: invalid syntax
news = list(un)
      
s
...       
'python programming'
>>> l
...       
['p', 'y', 't', 'h', 'o', 'n', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
>>> un
...       
{'g', 'a', ' ', 'i', 'h', 'n', 'p', 'y', 'm', 'r', 'o', 't'}
>>> news
...       
['g', 'a', ' ', 'i', 'h', 'n', 'p', 'y', 'm', 'r', 'o', 't']
>>> s
...       
'python programming'
>>> k
...       
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    k
NameError: name 'k' is not defined
>>> en
...       
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    en
NameError: name 'en' is not defined. Did you mean: 'un'?
>>> news
...       
['g', 'a', ' ', 'i', 'h', 'n', 'p', 'y', 'm', 'r', 'o', 't']
>>> l
...       
['p', 'y', 't', 'h', 'o', 'n', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
s
>>> 
>>> un
...       
{'g', 'a', ' ', 'i', 'h', 'n', 'p', 'y', 'm', 'r', 'o', 't'}
>>> news
...       
['g', 'a', ' ', 'i', 'h', 'n', 'p', 'y', 'm', 'r', 'o', 't']
