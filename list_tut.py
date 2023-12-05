import random
import math

randList = ['string', 1.234, 28]
OnetoTen = list(range(10))
randList = randList + OnetoTen

print(randList[0])
print(len(randList))

numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))
print(numList)

# or

numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))
for i in numList:
    print(f'{i}', end=' ')
print()

'''
* bubblesort (outer loop that decreases in size each time it loops)
* the goal is to have the largest number at the end of the list
when the outer loop completes one cycle
* the inner loop starts comparing indexes at the beginning of the
loop
* check if list[index] > list[index + 1]
* if so, swap the index values
* when the lower loop completes, the largest number should be at 
the end of the list
* decrement the outer loop by 1
'''

numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))

i = len(numList) - 1
while i > 1:
    j = 0
    while j < i:
        print(f'Random numbers: {numList}')
        print(f'\nIs {numList[j]} > {numList[j + 1]}')
        if numList[j] > numList[j + 1]:
            print('yeah, switch!')
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print('nope, do not switch!')
        j += 1
        for k in numList:
            print(k, end=', ')
        print()
    print('End of round')
    i -= 1
print('BubbleSort: ', end='')
for k in numList:
    print(k, end=' ')
#print()