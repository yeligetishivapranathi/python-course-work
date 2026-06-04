Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
operators
-----------
art(+ - * / // % **)
compar(< > <= >= == !=)
ass(= += -= *= /= //= %= **=)
logical(and or not)
membership operator(in not in)
identity operator(is is not)
bit(& | ^ ~ << >>)
'''
'\noperators\n-----------\nart(+ - * / // % **)\ncompar(< > <= >= == !=)\nass(= += -= *= /= //= %= **=)\nlogical(and or not)\nmembership operator(in not in)\nidentity operator(is is not)\nbit(& | ^ ~ << >>)\n'
a=5
b=6
a+b
11
a-b
-1
a*b
30
a/b
0.8333333333333334
a//b
0
a%b
5
a**b
15625
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a!=b
True
a=b
a+=b
a
12
a-=10
a
2
a*=20
a/=30
a
1.3333333333333333
a*=20
a
26.666666666666664
a%=20
a**=30
a and b
6
a or b
5.215095050846507e+24
a not b
SyntaxError: incomplete input
b=50
a not b
SyntaxError: incomplete input
a or b
5.215095050846507e+24
''' and or not gates
a= '''
' and or not gates\na= '
a=True
b=False
a and b
False
a or b
True
a%10==10 and b%20
False
a%10==0
False
#str,list,tuple,set,dict
a='python programming'
a
'python programming'
'y' in a
True
'g' in a
True
'z' not in a
True
'r' not in a
False
l=['java','python','mysql','keyword']
'mysql' in l
True
'ja' not in l
True
t={1,2,4,56,7,78,235,23}
t
{1, 2, 4, 7, 235, 78, 23, 56}
>>> 4 in t
True
>>> 24 in t
False
>>> d={'egg':8,'oil':120,"sugar":40,"salt:30}
...    
SyntaxError: incomplete input
>>> d={'egg':8,'oil':120,"sugar":40,"salt":30}
...    
>>> 'oil' in d
...    
True
>>> 120 in d
...    
False
>>> "sugar" in d
...    
True
>>> 30 in d
...    
False
>>> i=[1,2,3,4,5]
...    
>>> m=[1,2,3,4,5]
...    
>>> n==m
...    
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    n==m
NameError: name 'n' is not defined
>>> i==m
...    
True
>>> n==i
...    
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    n==i
NameError: name 'n' is not defined
>>> n=m
...    
>>> n==i
...    
True
