a=int(input('введите первое число:'))
b=int(input('введите второе число:'))
if b!=0 and a%b==0:
    print(f'первое число {a} делится на второе число {b}')
    print(f'остаток: {a%b}')
    print(f'частное: {a/b}')
elif b==0:
     print('делитель не может быть равен нулю')
else:
    print(f'первое число {a} не делится на второе число {b}')
    print(f'остаток: {a%b}')
    print(f'частное: {a/b}')


    
