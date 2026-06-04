Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[]
type(l)
<class 'list'>
l=list(l)
type(l)
<class 'list'>
l=[1,2,3,4]
m=[7,5,4,3]
l+m
[1, 2, 3, 4, 7, 5, 4, 3]
l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=[10,20,30,40,50]
l[4]
50
l[2]
30
l[0]
10
l[1]
20
l[-1]
50
l[-3]
30
l[1:4]
[20, 30, 40]
l[-1:-4:-1]
[50, 40, 30]
l[-3::-1]
[30, 20, 10]
20 in l
True
40 in l
True
70 not in l
True
10 not in l
False
l
[10, 20, 30, 40, 50]
id(1)
140728169653032
l[1]
20
l[1] = 70
l
[10, 70, 30, 40, 50]
l.append(400)
l
[10, 70, 30, 40, 50, 400]
l.insert(1,70)
l
[10, 70, 70, 30, 40, 50, 400]
id(1)
140728169653032
l.insert()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l.insert()
TypeError: insert expected 2 arguments, got 0
l.insert(4,50)
l
[10, 70, 70, 30, 50, 40, 50, 400]
l.extend([80,90,110])
l
[10, 70, 70, 30, 50, 40, 50, 400, 80, 90, 110]
l.pop()
110
l
[10, 70, 70, 30, 50, 40, 50, 400, 80, 90]
l.pop(0)
10
l
[70, 70, 30, 50, 40, 50, 400, 80, 90]
del l[1]
l
[70, 30, 50, 40, 50, 400, 80, 90]
del l[2]
l
[70, 30, 40, 50, 400, 80, 90]
l
[70, 30, 40, 50, 400, 80, 90]
l.clear()
l
[]
l=[20,30,50,60,70,80,90]
l
[20, 30, 50, 60, 70, 80, 90]
sorted(1)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    sorted(1)
TypeError: 'int' object is not iterable
sorted(l)
[20, 30, 50, 60, 70, 80, 90]
>>> min(l)
20
>>> max(l)
90
>>> l.reverse()
>>> l
[90, 80, 70, 60, 50, 30, 20]
>>> l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> sorted(l,reverse=True)
[90, 80, 70, 60, 50, 30, 20]
>>> l
[90, 80, 70, 60, 50, 30, 20]
>>> l.index(120)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    l.index(120)
ValueError: 120 is not in list
>>> l.index(70)
2
>>> l.count(30)
1
>>> m=l
>>> m
[90, 80, 70, 60, 50, 30, 20]
>>> m.append(200)
>>> l
[90, 80, 70, 60, 50, 30, 20, 200]
>>> m
[90, 80, 70, 60, 50, 30, 20, 200]
>>> sum(l)
600
>>> any([1,2,3,00000,0,0])
True
>>> all([1,2,3,5,0,0,0,0])
False
>>> any(1)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    any(1)
TypeError: 'int' object is not iterable
>>> any(l)
True
