#
# Tests for required functions on lab 4
#   DANIEL KLUVER 16 Feb 2020
#
# Each test has a comment showing what output is expected.
# In general, each test will be around 2 points each.

from assoc_lists import *

# Linear association list tests:

empty = []
lin_list_num = [("word", 3.14), ("reason", 1.23), ("candy", 5), ("fault", 4.1)]
# The lin_list is equivalent to this: {3:"word", 1:"reason", 5:"candy", 4:"fault"}
# Note, we can use any "sortable" data for keys, so any number or strings.

print(lin_contains(lin_list_num, 3.14))         # True
print(lin_contains(lin_list_num, 4.126))        # False
print(lin_contains(empty, 3.14))                # False

print(lin_get(empty, 1.23))                     # None
print(lin_get(lin_list_num, 53.2))              # None
print(lin_get(lin_list_num, 3.14))              # word
print(lin_get(lin_list_num, 5))                 # candy
print(lin_get(lin_list_num, 4.1))               # fault

lin_put(empty, "apple", "dog")
print(empty)                                    # [("dog", "apple")]

lin_put(lin_list_num, 5, "sugar")
print(len(lin_list_num))                        # 4
print( ("sugar", 5) in lin_list_num)            # True
print(lin_get(lin_list_num, 5))                 # sugar

lin_put(lin_list_num, 10.3, "flood")
print(len(lin_list_num))                        # 5
print( ("flood", 10.3) in lin_list_num)         # True



# BINARY SEAR ASSOCIATION TESTS
print("BINARY")
empty = []
#bin_list = {
#    "crow" : 3,
#    "raven" : 49,
#    "fish" : 2,
#    "cat" : 13,
#    "dog" : 52,
#    "zebra" : 13,
#    "whale" : 11.3,
#    "emu" : 56
#}
# note that python let's us use < and > so no issue here.
bin_list = [(13, 'cat'), (3, 'crow'), (52, 'dog'), (56, 'emu'), (2, 'fish'), (49, 'raven'), (11.3, 'whale'), (41, 'zebra')]


print(bin_contains(empty, "dog"))               # False
print(bin_contains(bin_list, "apple"))          # False
print(bin_contains(bin_list, "dragon"))         # False
print(bin_contains(bin_list, "zzz"))            # False
print(bin_contains(bin_list, "cat"))            # True
print(bin_contains(bin_list, "fish"))           # True
print(bin_contains(bin_list, "zebra"))          # True


print(bin_get(empty, "dog"))                    # None
print(bin_get(bin_list, "apple"))               # None
print(bin_get(bin_list, "dragon"))              # None
print(bin_get(bin_list, "zzz"))                 # None
print(bin_get(bin_list, "cat"))                 # 13
print(bin_get(bin_list, "whale"))               # 11.3
print(bin_get(bin_list, "zebra"))               # 41



bin_put(empty, "apple", "dog")
print(empty)                                    # [("dog", "apple")]

bin_list = [(13, 'cat'), (3, 'crow'), (52, 'dog'), (56, 'emu'), (2, 'fish'), (49, 'raven'), (11.3, 'whale'), (41, 'zebra')]
bin_put(bin_list, "cat", 99)
print(bin_get(bin_list, "cat"))                 # 99
print(len(bin_list))                            # 8
print(bin_list[0])                              # (99, 'cat')

bin_list = [(13, 'cat'), (3, 'crow'), (52, 'dog'), (56, 'emu'), (2, 'fish'), (49, 'raven'), (11.3, 'whale'), (41, 'zebra')]
bin_put(bin_list, "zebra", 99)
print(bin_get(bin_list, "zebra"))               # 99
print(len(bin_list))                            # 8
print(bin_list[7])                              # (99, 'zebra')

bin_list = [(13, 'cat'), (3, 'crow'), (52, 'dog'), (56, 'emu'), (2, 'fish'), (49, 'raven'), (11.3, 'whale'), (41, 'zebra')]
bin_put(bin_list, "dog", 99)
print(bin_get(bin_list, "dog"))                 # 99
print(len(bin_list))                            # 8
print(bin_list[2])                              # (99, 'dog')

bin_list = [(13, 'cat'), (3, 'crow'), (52, 'dog'), (56, 'emu'), (2, 'fish'), (49, 'raven'), (11.3, 'whale'), (41, 'zebra')]
bin_put(bin_list, "apple", 99)
print(bin_get(bin_list, "apple"))               # 99
print(len(bin_list))                            # 9
print(bin_list[0])                              # (99, 'apple')

bin_list = [(13, 'cat'), (3, 'crow'), (52, 'dog'), (56, 'emu'), (2, 'fish'), (49, 'raven'), (11.3, 'whale'), (41, 'zebra')]
bin_put(bin_list, "zzzzz", 99)
print(bin_get(bin_list, "zzzzz"))               # 99
print(len(bin_list))                            # 9
print(bin_list[-1])                              # (99, 'zzzzz')

bin_list = [(13, 'cat'), (3, 'crow'), (52, 'dog'), (56, 'emu'), (2, 'fish'), (49, 'raven'), (11.3, 'whale'), (41, 'zebra')]
bin_put(bin_list, "dragon", 99)
print(bin_get(bin_list, "dragon"))              # 99
print(len(bin_list))                            # 9
print(bin_list[3])   
print(bin_list)                                # (99, 'dragon')
