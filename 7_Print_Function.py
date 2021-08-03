def print_numbers(number):
    if(number != 0):
        print_numbers(number-1)
        print(str(number), end="")


n = int(input())
print_numbers(n)
