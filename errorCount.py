def main():
    n = int(input("Please input the total number of the test: "))
    a = [0] * n
    i = int(input("Please input the NO. of the error problem: ")) - 1
    while i < n:
        a[i] = a[i] + 1
        i = int(input("Please input the NO. of the error problem: ")) - 1
    print("The error number of each problem is: ", a)


main()
