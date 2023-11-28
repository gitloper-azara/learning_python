# for loops
def main():
    n = eval(input('How many numbers do you have? '))
    total = 0.0

    for i in range(n):
        x = float(input('Enter a number >> '))
        total = total + x
    print(f'\nThe average of the numbers is: {total / n}')
main()
