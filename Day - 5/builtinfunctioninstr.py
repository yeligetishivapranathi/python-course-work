Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
 Type "help", "copyright", "credits" or "license()" for more information.
s = "python programing"
len(s)
17
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
order('0')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    order('0')
NameError: name 'order' is not defined
ord('0')
48
chr(120)
'x'
chr(35)
'#'
s
'python programing'
s.upper()
'PYTHON PROGRAMING'
s.lower()
'python programing'
s.capitalize()
'Python programing'
s.title()
'Python Programing'
s.swapcase()
'PYTHON PROGRAMING'
'PYTHON PROGRAMING'
'PYTHON PROGRAMING'
s.center(25,'*')
'****python programing****'
s.ljust(28,'-')
'python programing-----------'
s.rjust(28,'-')
'-----------python programing'
'123'.zfill(10)
'0000000123'
'123'.zfill()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    '123'.zfill()
TypeError: str.zfill() takes exactly one argument (0 given)
'123'.zfill(13)
'0000000000123'
#search&find methods
s
'python programing'
s.find('o')
4
s.find('o')
4
s.rfind('o')
9
s.find('z')
-1
s.index(-0)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s.index(-0)
TypeError: must be str, not int
s.index('0')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.index('0')
ValueError: substring not found
s.index('o')
4
s.index('m')
13
s.count('m')
1
s.index('z')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.index('z')
ValueError: substring not found
#find is recamended because it will donnot raise error
s
'python programing'
s.replace('python','java')
'java programing'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456'))
'123456 1r5grami6g'
k='java,pyton,javascript,c,c++'
s.split(',')
['python programing']
>>> s.split(',',2)
['python programing']
>>> s.rsplit(',',2)
['python programing']
>>> g='sdfgh'
>>> g='''dsnkdk'''
>>> g='''hjhkj
... hhkjk
... jjlkj
... hghjk'''
>>> g
'hjhkj\nhhkjk\njjlkj\nhghjk'
>>> s.splitlines()
['python programing']
>>> g.split()
['hjhkj', 'hhkjk', 'jjlkj', 'hghjk']
>>> s.split()
['python', 'programing']
>>> j=['java,pyton,javascript,c,c++']
>>> ''.join(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    ''.join(l)
NameError: name 'l' is not defined
>>> ''.join(j)
'java,pyton,javascript,c,c++'
>>> '-'join(j)
SyntaxError: invalid syntax
>>> '-'.join(j)
'java,pyton,javascript,c,c++'
>>> '8'.join(j)
'java,pyton,javascript,c,c++'
>>> s
'python programing'
>>> k
'java,pyton,javascript,c,c++'
>>> k.partition(',')
('java', ',', 'pyton,javascript,c,c++')
>>> k.rpartition(',')
('java,pyton,javascript,c', ',', 'c++')
>>> t = 'hello ☺'
>>> t.encode()
b'hello \xe2\x98\xba'
>>> b'hello \xe2\x98\xba'.decode()
'hello ☺'
