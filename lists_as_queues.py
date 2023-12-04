'''
using collections.deque for FIFO instead of lists
doing inserts and pops from the beginning of a list
is slow (beacause all of the other elements have to be
shifted by one)
'''

from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
print('Printing Queue...')
print(queue)
queue.append(input('Insert name: '))
queue.append(input('Insert another: '))
print('Processing...')
print('Deleting original first two names...')
queue.popleft()
queue.popleft()
print('Success!')
print('New queue:')
print(queue)