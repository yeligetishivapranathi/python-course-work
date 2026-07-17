Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d{'kom':89,'bha':76,'su':90,'na':76,'dine':50}
SyntaxError: invalid syntax
d={'kom':89,'bha':76,'su':90,'na':76,'dine':50}
d[kom]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d[kom]
NameError: name 'kom' is not defined
d['ko']
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d['ko']
KeyError: 'ko'
d.get('kom']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
d.get('kom')
89
#it vont raise a error when it not fount value
d.get('san")
      
SyntaxError: incomplete input
d.get('sam')
      
d.get('sam','ksdls')
      
'ksdls'
#if i want to give any message we can give
      
'sam' in d
      
False
'sam' not in d
      
True
d.keys()
      
dict_keys(['kom', 'bha', 'su', 'na', 'dine'])
d.values()
      
dict_values([89, 76, 90, 76, 50])
sorted(d)
      
['bha', 'dine', 'kom', 'na', 'su']
max(d)
      
'su'
min(d)
      
'bha'
len(d)
      
5
d
      
{'kom': 89, 'bha': 76, 'su': 90, 'na': 76, 'dine': 50}
d[kom]=80
      
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[kom]=80
NameError: name 'kom' is not defined
d['kom']=80
      
d['su']=50
...       
>>> d
...       
{'kom': 80, 'bha': 76, 'su': 50, 'na': 76, 'dine': 50}
>>> d.update({'pra':90,'man':80})
...       
>>> d
...       
{'kom': 80, 'bha': 76, 'su': 50, 'na': 76, 'dine': 50, 'pra': 90, 'man': 80}
>>> d.poitem()
...       
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d.poitem()
AttributeError: 'dict' object has no attribute 'poitem'. Did you mean: 'popitem'?
>>> d.popitem()
...       
('man', 80)
>>> d
...       
{'kom': 80, 'bha': 76, 'su': 50, 'na': 76, 'dine': 50, 'pra': 90}
>>> d.pop('sub')
...       
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d.pop('sub')
KeyError: 'sub'
>>> d.pop('su')
...       
50
>>> del d['kom']
...       
>>> d
...       
{'bha': 76, 'na': 76, 'dine': 50, 'pra': 90}
>>> d.clear()
...       
>>> d
...       
{}
>>> d.setdefault('koma',50)
...       
50
>>> d
...       
{'koma': 50}
