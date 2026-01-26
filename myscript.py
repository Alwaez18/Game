print("Hello, What is your Name?")
name = input()
print('Приятно познакомиться, ', name, '!', sep ='')
age = int(input('Сколько тебе лет, '+ name + '?'))
print('А я думал тебе ', age + 1, end = '')
x = age + 1
if x >=11 and x<=19:
    print('лет')
elif x % 10==1:
    print('год')
elif x % 10 >= 2 and x % 10<=4:
    print('года')
else:
    print('лет')

print('!..')

