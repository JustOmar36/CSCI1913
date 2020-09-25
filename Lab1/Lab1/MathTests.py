#
# Tests for the two required functions for lab 1.
#   DANIEL KLUVER 27 Jan 2020
#
# Running this file should not trigger the interactive user interface of MathTools.
# Each test has a comment showing what output is expected.

# NOTE: this file will not work until you (at least) declare the print_divisors function.
from MathTools import lowest_common_multiple, print_divisors

print(lowest_common_multiple(1,2))          # 2
print(lowest_common_multiple(3,2))          # 6
print(lowest_common_multiple(15,21))        # 105
print(lowest_common_multiple(15,15))        # 15
print(lowest_common_multiple(1315,105))     # 27615

x = print_divisors(10)
# 1
# 2
# 5
# 10
print(x) # False

x = print_divisors(60)
# 1
# 2
# 3
# 4
# 5
# 6
# 10
# 12
# 15
# 20
# 30
# 60
print(x) # False

x = print_divisors(61)
# 1
# 61
print(x) # True


x = print_divisors(2)
# 1
# 2
print(x) # True

x = print_divisors(1031)
# 1
# 1031
print(x) # True