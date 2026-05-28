Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
float(a)
10.0
double(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    double(a)
NameError: name 'double' is not defined
bool(a)
True
complex(a)
(10+0j)
str9a)
SyntaxError: unmatched ')'
str(a)
'10'
b=7.5
int(b)
7
complex(b)
(7.5+0j)
str(b)
'7.5'
bool(b)
True
o=6+5j
str(o)
'(6+5j)'
bool(o)
True
g="vhxh"
int(g)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(g)
ValueError: invalid literal for int() with base 10: 'vhxh'
list(g)
['v', 'h', 'x', 'h']
tuple(g)
('v', 'h', 'x', 'h')
set(g)
{'v', 'x', 'h'}
bool(g)
True
y=["kelk","jkj","iek"]

type(y)
<class 'list'>
int(y)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(y)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> bool(y)
True
>>> tuple(Y)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tuple(Y)
NameError: name 'Y' is not defined. Did you mean: 'y'?
>>> set(y)
{'kelk', 'iek', 'jkj'}
>>> bool(y)
True
>>> t=("hjk",126,565,5)
>>> type(t)
<class 'tuple'>
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> bool(t)
True
>>> tuple(t)
('hjk', 126, 565, 5)
>>> g={2:2,3:3,5:8}
>>> type(G)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    type(G)
NameError: name 'G' is not defined. Did you mean: 'g'?
>>> type(g)
<class 'dict'>
>>> str(g)
'{2: 2, 3: 3, 5: 8}'
>>> list(g)
[2, 3, 5]
>>> dict(g)
{2: 2, 3: 3, 5: 8}
>>> tuple(g)
(2, 3, 5)
>>> tuple[g]
tuple[{2: 2, 3: 3, 5: 8}]
>>> tuple{g}
SyntaxError: invalid syntax
