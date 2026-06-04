Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='        hello      word      '
s
'        hello      word      '
s.strip()
'hello      word'
s.lstrip()
'hello      word      '
s.rstrip()
'        hello      word'
s='string.py'
s
'string.py'
s.startswith('str')
True
>>> s.startswith('sss')
False
>>> s.endswith('py')
True
>>> 'hsjhdksjdk'.isalpha()
True
>>> '235656'.isalpha()
False
>>> 'bjdfoDFGnkdkodk.isalpha()
SyntaxError: incomplete input
>>> 'bjdfoDFGnkdkodk'.isalpha()
True
>>> '656563'.isnum()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    '656563'.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> '656563'.isalnum()
True
>>> 'daljkf'isupper()
SyntaxError: invalid syntax
>>> 'daljkf'.isupper()
False
>>> 'hkskdl'.islower()
True
>>> 'HDJHFI@3KDFKSKF'.isupper()
True
>>> ' '.isspace()
True
>>> 'hello       '.isspace()
False
>>> 'Py Prg Lan'.istitle()
True
>>> 'kddppd'.istitle()
False
>>> 'py_python'.isidentifier()
True
>>> 'py@123'.isidentifier()
False
>>> l=[]
>>> type(l)
<class 'list'>
>>> l=list()
>>> type(l)
<class 'list'>
