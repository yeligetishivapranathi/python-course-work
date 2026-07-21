data={
    'subbu':{'status':True,'python':98,'mysql':95,'flask':94},
    'nagendra':{'status':True,'python':92,'mysql':55,'flask':35},
    'dinesh':{'status':False,'python':None,'mysql':None,'flask':None}
    }
name=input('enter your name:')
if name in data:
    if data[name]['status']:
        total = data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=total/3
        if avg > 90:
            print(f"Congration{name},you got first class!!!")
        elif avg>70:
            print(f'good{name},keep it up for the the next time!!')
        elif avg >35:
            print(f'batter{name},work hard for next time!!')
    else:
            print(f'{name} didnot write the exam.Bring your parents')

else:
    print(f"{name}'s data is not found")
