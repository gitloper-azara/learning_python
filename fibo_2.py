# fibonacci with an 'end' argument

a = 0
b = 1

while a < 1000:
    print(a, end = ', ')
    a, b = b, a + b
print('\n')
