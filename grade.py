# problem: determine grade level based on age
# age = 5, go to kindergarten
# age = 6 through 17, go from primary to senior high
# age > 17, college or university
asteriks = '****************'
print(f'{asteriks}')
print('Level Determiner')
print(f'{asteriks}')
while 1:
    age = eval(input('Enter your age here: '))
    if age == 0:
        print('How are you able to operate a computer?!')
    elif age < 5:
        print('Hello creche student!')
    elif age == 5:
        print('Hello dear. You should be in kindergarten')
    elif age >= 6 and age <= 17:
        print('You should be in either primary, junior high or senior high')
    elif age >= 30:
        print('We shall not discriminate based on age. You can still be in school')
    else:
        print('Heyya university tank!')
pass
