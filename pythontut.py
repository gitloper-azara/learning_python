# ask the user to input 2 variables and store them in variables num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()

# convert the strings into regular num integers
num1 = int(num1)
num2 = int(num2)

# add the values entered and store in sum
sum = num1 + num2

# subtract the values entered and store in diff
diff = num1 - num2

# multiply the values entered and store in product
product = num1 * num2

# divide the values entered and store in quotient
quotient = num1 / num2

# use modulus on the values to find the remainder
mod = num1 % num2

# print the results
print(f'{num1} + {num2} = {sum}')
print(f'{num1} - {num2} = {diff}')
print(f'{num1} * {num2} = {product}')
print(f'{num1} / {num2} = {quotient}')
print(f'{num1} % {num2} = {mod}')
