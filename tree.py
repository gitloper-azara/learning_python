# print a tree based on number of input given

def main():
    n = eval(input('Enter number of tree branches: '))
    branch = 1
    space = n - 1
    stump_space = space

    while n != 0:
        for i in range(space):
            print(' ', end="")
        for i in range(branch):
            print('#', end="")

        print()
        space = space - 1
        branch = branch + 2
        n = n - 1

    for i in range(stump_space):
        print(' ', end="")
    print('#')
main()
