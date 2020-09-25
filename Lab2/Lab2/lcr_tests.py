#
# Tests for the two required functions for lab 2.
#  DANIEL KLUVER 3 Feb 2020
#
# Each test has a comment showing what output is expected.

from lcr_die import roll_die, stage_for_testing, check_testing
from lcr_sim import *

# Tests for lcr_over
print(lcr_over([0,1,2,3,4]))       # False
print(lcr_over([3,0,0,1]))         # False
print(lcr_over([1,0,0,0,0]))       # True
print(lcr_over([0,4,0]))           # True

# Tests for lcr_winner
print(lcr_winner([1,0]))           # 0
print(lcr_winner([0,0,3,0,0]))     # 2

# Tests for left
x = [1,1,1,1,1]
left(x, 2)
print(x)                           # [1, 2, 0, 1, 1]

x = [1,1,1,1,1]
left(x, 0)
print(x)                           # [0, 1, 1, 1, 2]

x = [1,1,1,1,1]
left(x, 4)
print(x)                           # [1, 1, 1, 2, 0]


# Tests for right
x = [1,1,1,1,1]
right(x, 2)
print(x)                           # [1, 1, 0, 2, 1]

x = [1,1,1,1,1]
right(x, 0)
print(x)                           # [0, 2, 1, 1, 1]

x = [1,1,1,1,1]
right(x, 4)
print(x)                           # [2, 1, 1, 1, 0]


# Tests for center
x = [1,1,1,1,1]
center(x, 2)
print(x)                           # [1, 1, 0, 1, 1]

x = [1,1,1,1,1]
center(x, 0)
print(x)                           # [0, 1, 1, 1, 1]

x = [1,1,1,1,1]
center(x, 4)
print(x)                           # [1, 1, 1, 1, 0]


# Tests for lcr_game -
# Note, these tests use a secial testing interface I added to the dice that let me force specific dice rolls.
# This isn't the sort of feature you would want to see in a production game, but it's the exact sort of
# feature you want when testing, or in a classroom environment.

# force a quick 2-player loss
stage_for_testing("LCR")
print(lcr_game(2))                 # (1, 1)
# If you are getting False here - you arn't calling roll_dice the right number of times
# either you are under-rolling, or over-rolling.
print(check_testing())             # True

stage_for_testing("RRRRRRRRR.CRCCCCCC..LR")
# turn 1 [3, 3, 3] player 1 rolls RRR
# turn 2 [0, 6, 3] player 2 rolls RRR
# Turn 3 [0, 3, 6] player 3 rolls RRR
# Turn 4 [3, 3, 3] player 1 rolls .CR
# Turn 5 [1, 4, 3] player 2 rolls CCC
# Turn 6 [1, 1, 3] player 3 rolls CCC
# Turn 7 [1, 1, 0] player 1 rolls . (should only roll 1 die because they have only one chip
# Turn 8 [1, 1, 0] player 2 rolls . (should only roll 1 die because they have only one chip
# Turn 9 [1, 1, 0] player 3 rolls no dice, having no chips. but still gets a turn.
# Turn 10 [1, 1, 0] player 1 rolls L
# Turn 11 [0, 1, 1] player 2 rolls R
# end of turn 11 [0,0,2] player 3 (index 2) wins after 11 turns
print(lcr_game(3))                 # (2, 11)
print(check_testing())             # True


# Tests for most_common_winner
win, avg = most_common_winner(2)
print(win)                          #1 (this is technically random, but incredibly unlikely to not be 1)
print(avg)                          #0.615 (this should be within 0.15ish (so between 0.6 and 0.63)

win, avg = most_common_winner(2)
print(win)                          #1 (this is technically random, but incredibly unlikely to not be 1)
print(avg)                          #0.615 (this should be within 0.15ish (so between 0.6 and 0.63)

win, avg = most_common_winner(2)
print(win)                          #1 (this is technically random, but incredibly unlikely to not be 1)
print(avg)                          #0.615 (this should be within 0.15ish (so between 0.6 and 0.63