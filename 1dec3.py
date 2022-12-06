Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
nums=[1,1,5,8,9,5,10,2,3]
type(nums)
<class 'list'>
print(nums)
[1, 1, 5, 8, 9, 5, 10, 2, 3]
for num in nums:
    print(nub)

    
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    print(nub)
NameError: name 'nub' is not defined. Did you mean: 'num'?
for num in nums:
    print(num)

    
1
1
5
8
9
5
10
2
3
dir(nums)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
nums.count(1)
2
help(num.index)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    help(num.index)
AttributeError: 'int' object has no attribute 'index'
nums=[1,1,5,8,9,5,10,2,3,"pyt","a",3.11,"true"]
for num in nums:
    print(num)

    
1
1
5
8
9
5
10
2
3
pyt
a
3.11
true
>>> len(nums)
13
>>> for num in nums:
...     print(0)
... 
...     
0
0
0
0
0
0
0
0
0
0
0
0
0
>>> nums(0)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    nums(0)
TypeError: 'list' object is not callable
>>> nums[0]
1
>>> nums[-1]
'true'
