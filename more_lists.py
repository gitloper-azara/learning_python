'''
we are going to do more lists for
a data structure
'''

lst = ['one', 'two', 'three', 'four', 'five']
print(lst)

# trying the append way
lst.append('six')
print(lst)

#trying the array way
lst[len(lst):] = ['seven']
print(lst)