# CSCI 1913, Spring 2020, Lab 1
# Student Names:
# Omar Masri!
# Brandon Weinstein!
# MASRI013@umn.edu
# WEINS127@umn.edu

def lowest_common_multiple(x, y):
    a = x * y
    for i in range(a, 0, -1):
        if (i % x == 0) and (i % y == 0):
            lowest = i

    return lowest

# delete this line and then write this function
def print_divisors(x):
    num_divisors = 0
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            num_divisors += 1

    if num_divisors == 2 or x == 1:
        print(i, "is prime")
    else:
        print(i, 'is not prime')






if __name__ == "__main__":
    print('welcome to math tool')
    print('what do you want to do:')
    print('(lcm) compute the lowest common multiple of two numbers')
    print('(prime) test numbers for primeness (by listing divisors)')
    choice = input('> ')

    if choice == 'lcm':
        x = int(input('enter a number:  '))
        y = int(input('enter another number:  '))
        print('lowest common multiple of', x, 'and', y, 'is', lowest_common_multiple(x, y))

    if choice == 'prime':
        run = True
        while run:
            x = input("enter numbers to test primeness, enter 'done' when done\n> ")
            if x == 'done':
                run = False
            else:
                print_divisors(int(x))
