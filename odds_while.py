# printing odd numbers using while loop

def main():
    i = 1;
    while i <= 20:
        if i % 2 == 0:
            i = i + 1
            continue

        if i == 15:
            break

        print(i)
        i = i + 1
main()
