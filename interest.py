# calculating interest earned over a period of time
def main():
    principal = float(input('Enter your principal amount: '))
    interest = float(input('Enter your expected interest rate(ignore %): '))
    interest = interest * .01

    for i in range(1, 11):
        principal = principal + (principal * interest)
        print(f'Earnings after year {i} = {principal:.2f}')
    print(f'Total investment return = {principal:.2f}')
main()
