name = input()
rollno = int(input())
s1 = int(input())
s2 = int(input())
s3 = int(input())
total = s1+s2+s3
avg = total/3
print(f'Student Name : {name}')
print(f'Roll Number : {rollno}')
print(f'total Marks: {total}')
print(f'Average Marks:{avg}')

s=input()
print('Total Characters:',len(s))
print('First Charcter:',s[0])
print('last Character:',s[-1])
print('upper case',s.upper())
print('Revesed String:',s[::-1])

a,b,c = list(map(int,input().split()))
print('Sum:',a+b+c)
print('Average:',(a+b+c)/3)
print('Product:',a*b*c)
