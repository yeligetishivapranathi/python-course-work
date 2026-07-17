Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
type(d)
<class 'dict'>
#key properties,value properies
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d
{}
d[1]='int'
d
{1: 'int'}
d[2]='float'
d
{1: 'int', 2: 'float'}
>>> d[3]='double'
>>> d
{1: 'int', 2: 'float', 3: 'double'}
>>> d[2.1]='float'
>>> d
{1: 'int', 2: 'float', 3: 'double', 2.1: 'float'}
>>> d['demo']='str'
>>> d
{1: 'int', 2: 'float', 3: 'double', 2.1: 'float', 'demo': 'str'}
>>> d[2+3j]='complex'
>>> d
{1: 'int', 2: 'float', 3: 'double', 2.1: 'float', 'demo': 'str', (2+3j): 'complex'}
>>> d[False]='bool'
>>> d
{1: 'int', 2: 'float', 3: 'double', 2.1: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
>>> d[(1,2)]='tuple'
>>> d
{1: 'int', 2: 'float', 3: 'double', 2.1: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool', (1, 2): 'tuple'}
>>> d={}
>>> d
{}
>>> d[23]=23.4
>>> d[3]='dfg'
>>> d[4]=3+4j
>>> d[5]=[1,2,3]
>>> d[6]=()
>>> d[7]={}
>>> d[8]={1:2}
>>> d[9]=False
>>> d
{23: 23.4, 3: 'dfg', 4: (3+4j), 5: [1, 2, 3], 6: (), 7: {}, 8: {1: 2}, 9: False}
>>> d={}
>>> d[1]=14
>>> d
{1: 14}
>>> d[1]=2
>>> d[2]=3
>>> d[3]=4
>>> d[4]=5
>>> d
{1: 2, 2: 3, 3: 4, 4: 5}
>>> d[3]
4
>>> d[4]
5
