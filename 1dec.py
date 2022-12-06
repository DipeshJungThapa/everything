Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
y="aakarshak"
y
'aakarshak'
dir(y)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(aakarshak)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    help(aakarshak)
NameError: name 'aakarshak' is not defined
help(y.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.
    
      sep
        The separator used to split the string.
    
        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.
    
    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

x="my name is aakarshak rijal"
dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(y.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.
    
      sep
        The separator used to split the string.
    
        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.
    
    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

x.count(y)
1
x.split( )
['my', 'name', 'is', 'aakarshak', 'rijal']
#country= "france"
y.spllit( )
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    y.spllit( )
AttributeError: 'str' object has no attribute 'spllit'. Did you mean: 'split'?
X.split( )
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    X.split( )
NameError: name 'X' is not defined. Did you mean: 'x'?
x="my name is aakarshak rijal"
x.split( )
['my', 'name', 'is', 'aakarshak', 'rijal']
#chopping
w = "i like watching football games\i like to play basketball"
print(w)
i like watching football games\i like to play basketball
w= "i like watching football\ni like to play basketball"
print(w)
i like watching football
i like to play basketball
a="hello\n how are you\n what are you doing"
print(a)
hello
 how are you
 what are you doing
w= "i like watching football\t i like to play basketball"
w.split( )
['i', 'like', 'watching', 'football', 'i', 'like', 'to', 'play', 'basketball']
print(w)
i like watching football	 i like to play basketball
w.count( )
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    w.count( )
TypeError: count() takes at least 1 argument (0 given)
w.count(" ")
8
w.count("\t")
1
name="xy\sz"
print(name)
xy\sz
name="xy\Sz"
print(name)
xy\Sz
letters="wht hello wht are you doing what are you doing what are you doing ehat are doing ahat are you doing what are you doing what are you doing ahat are you doing what are you doing what ae you doing "
print(letters)
wht hello wht are you doing what are you doing what are you doing ehat are doing ahat are you doing what are you doing what are you doing ahat are you doing what are you doing what ae you doing 
letters="""wht hello wht are you doing what are you doing what are you doing ehat are doing ahat are you doing what are you doing what are you doing ahat are you doing what are you doing what ae you doing hello world hello world hello world"""
print(letters)
wht hello wht are you doing what are you doing what are you doing ehat are doing ahat are you doing what are you doing what are you doing ahat are you doing what are you doing what ae you doing hello world hello world hello world
"""lksfh ;jhf;FH ;UOHF DS GFSF YIFDGSH IYD F GFI DH Uy riegr aeiro gye ia ufghay8o iau  iag  arku fgharh iyhw gaeyh iah ergoiauerhgirue aergiu aweuirh e iuawr ga hui rgsepiupua ihpuo giua paurghauire haugioarg pargaipurg poaurgp aoegr
r aogu  awrpugharg ahrapuiorgh aoregwijarg uio aowurhgag arghoaieg argoijgesp aergoharge ag erahpoireg aorgp go arguhaegouh oprhgpoarig oiaegr ogpog ij oiar ghaerg  oaerg pogre"""
'lksfh ;jhf;FH ;UOHF DS GFSF YIFDGSH IYD F GFI DH Uy riegr aeiro gye ia ufghay8o iau  iag  arku fgharh iyhw gaeyh iah ergoiauerhgirue aergiu aweuirh e iuawr ga hui rgsepiupua ihpuo giua paurghauire haugioarg pargaipurg poaurgp aoegr\nr aogu  awrpugharg ahrapuiorgh aoregwijarg uio aowurhgag arghoaieg argoijgesp aergoharge ag erahpoireg aorgp go arguhaegouh oprhgpoarig oiaegr ogpog ij oiar ghaerg  oaerg pogre'
letter.count(" ")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    letter.count(" ")
NameError: name 'letter' is not defined. Did you mean: 'letters'?
letters="wht hello wht are you doing what are you doing what are you doing ehat are doing ahat are you doing what are you doing what are you doing ahat are you doing what are you doing what ae you doing "
letter.count(" ")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    letter.count(" ")
NameError: name 'letter' is not defined. Did you mean: 'letters'?
letters.count(" " )
41
age= 20
if > 30:
    
SyntaxError: invalid syntax
if <:30
SyntaxError: invalid syntax
age=20
if<:30
SyntaxError: invalid syntax
if age<30:
if age<30:
    
SyntaxError: expected an indented block after 'if' statement on line 1
age =20
if age<30:
    print("done")

    
done

age=30
if age>20:
    print("okay")

    
okay
if age<20:
    print("okay")

    
else
SyntaxError: incomplete input
if age<20:
    print("okay")
    else
    
SyntaxError: incomplete input
if age<20:
    print("okay")
    else:
        
SyntaxError: invalid syntax
if age<20:
    print("okay")
else:
    print("fine")

    
fine
a=5
if a==10:
    print("yes")
else:
    print("no")

    
no
a==10
False
a==10||a<=4
SyntaxError: invalid syntax
a==10 || a<=4
SyntaxError: invalid syntax
a==10 | a<=4
False
a==10 & a<=8
False
a==10 or a<=4
False
a==10 and a<=8
False
a==10 and a<=8:
    
SyntaxError: incomplete input
if a==10 and a<=8:
    print("yes")
else:
    print("no")
... 
...     
no
>>> 
>>> if a==10 or a<=4:
...     print("yes")
... else:
...     print("no")
... 
...     
no
>>> if a==10 or a<=4 or a>4:
...     print("yes")
... else:
...     print("no")
... 
...     
yes
>>> if a==10 or a<=4 or a>4:
...     print("yes")
... elif a==13 and a>=15:
...     print(" its ok ")
... elif a==15 or a<=12:
...     print("true")
... else:
...     print("false")
... 
...     
yes
>>> if a==10 and a<=4:
...     print("yes")
... elif a==13 and a>=15:
...     print(" its ok ")
... elif a==15 or a<=12:
...     print("true")
... else:
...     print("false")
... 
...     
true
