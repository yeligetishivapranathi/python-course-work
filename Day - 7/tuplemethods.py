Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=()
t
()
type(t)
<class 'tuple'>
t=()
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,1.1,'triyu',[])
t
(1, 1.1, 'triyu', [])
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
h=(90,80,70)
t+h
(10, 20, 30, 40, 50, 90, 80, 70)
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t
(10, 20, 30, 40, 50)
t[1]
20
t[4]
50
t[2]
30
t[1]
20

t
(10, 20, 30, 40, 50)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[-1:-4:-1]
(50, 40, 30)
t
(10, 20, 30, 40, 50)
10 in t
True
10 not in t
False
60 not in t
True
len(t)
5
>>> sorted(t)
[10, 20, 30, 40, 50]
>>> min(t)
10
>>> max(t)
50
>>> sum(t0
...     t.count(10)
...     
SyntaxError: '(' was never closed
>>> sum(t)
...     
150
>>> t.count(10)
...     
1
>>> t.index(10)
...     
0
>>> t=(1,2,3)
...     
>>> a,b,c=t
...     
>>> a
...     
1
>>> b
...     
2
>>> c
...     
3
>>> t=(1,2,3,[4,5,6],7,8)
...     
>>> t
...     
(1, 2, 3, [4, 5, 6], 7, 8)
>>> t[3].append(10)
...     
>>> del t[3]
...     
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    del t[3]
TypeError: 'tuple' object doesn't support item deletion
