# problem: receive miles and convert to kilometers
# kilometers = miles * 1.60934
print('**************************************************')
print('Welcome to your MILES to KILOMETER conversion tool')
print('**************************************************')
miles = input('Enter miles figure: ')
miles = int(miles)
fig = 1.60934
conversion = miles * fig

print(f'{miles}mi converted to km = {conversion:.2f}km')
