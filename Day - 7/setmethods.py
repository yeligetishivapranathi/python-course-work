Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=set()
s={1,1,1,1,1,1}
s
{1}
s={987,654.345}
s
{987, 654.345}
s=set()
s
set()
s.add()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s.add(1)
s
{1}
s.add(56.567)
s
{56.567, 1}
s.add('bhj')
s
{56.567, 1, 'bhj'}
#list is not allowed
#list is not allowed
#to add
s.add((1,2,3,4))
s
{56.567, 1, (1, 2, 3, 4), 'bhj'}
#set is allowed to add
s
{56.567, 1, (1, 2, 3, 4), 'bhj'}
1 in s
True
l is not s
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l is not s
NameError: name 'l' is not defined
l not in s
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l not in s
NameError: name 'l' is not defined
1 not in s
False
s.append('false'0
         
SyntaxError: incomplete input
s.append('False)
         
SyntaxError: incomplete input
s.append('False')
         
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.append('False')
AttributeError: 'set' object has no attribute 'append'
s.add('False')
         
s
         
{1, 'False', (1, 2, 3, 4), 56.567, 'bhj'}
a={a,d,g,e,c,w,,}
         
SyntaxError: invalid syntax
a={a,d,g,e,c,w}
         
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a={a,d,g,e,c,w}
NameError: name 'a' is not defined
a = {a,d,g,e,c,w}
         
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a = {a,d,g,e,c,w}
NameError: name 'a' is not defined
a={1,2,3,4,5}
         
b={2,2,3,4,5}
         
a|b
         
{1, 2, 3, 4, 5}
a.union(b)
         
{1, 2, 3, 4, 5}
a.intersection(b)
         
{2, 3, 4, 5}
a&b
         
{2, 3, 4, 5}
a-b
         
{1}
a^b
         
{1}
a
         
{1, 2, 3, 4, 5}
a
         
{1, 2, 3, 4, 5}
a
         
{1, 2, 3, 4, 5}

,

a<= {1}
         
False
a>={1}
         
True
a.={1}
         
SyntaxError: invalid syntax
a<={1}
         
False
a>={1}
         
True
a
         
{1, 2, 3, 4, 5}
b
         
{2, 3, 4, 5}
a.disjoint(b)
         
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
         
False
a.isdisjoint({90,80})
         
True
>>> a.add(14)
...          
>>> a
...          
{1, 2, 3, 4, 5, 14}
>>> a.add(170)
...          
>>> a
...          
{1, 2, 3, 4, 5, 170, 14}
>>> a.add(14)
...          
>>> a
...          
{1, 2, 3, 4, 5, 170, 14}
>>> a.update({11,12,16})
...          
>>> a
...          
{1, 2, 3, 4, 5, 170, 11, 12, 14, 16}
>>> a.pop()
...          
1
>>> a.remove(4)
...          
>>> a
...          
{2, 3, 5, 170, 11, 12, 14, 16}
>>> a.discard(4)
...          
>>> a
...          
{2, 3, 5, 170, 11, 12, 14, 16}
>>> #discard also do same thing but it won't through a error
...          
>>> a.discard(2)
...          
>>> a
...          
{3, 5, 170, 11, 12, 14, 16}
>>> a.discard(2)
...          
>>> a
...          
{3, 5, 170, 11, 12, 14, 16}
