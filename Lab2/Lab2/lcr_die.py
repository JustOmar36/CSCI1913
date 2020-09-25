#
# This python module contains a special function roll_die, detailed below, which rolls a standard LCR game die.
# The standard LCR game dice has 6 sides, three of which have a dot ".", the remaining three have "L", "C", and "R"
# on them. This function is separate from the other code in order to aid testing. Other functions and logic in this
# module exists to allow us to force specific rolls for testing purposes.
#
# Author Daniel Kluver
#

import random

# The dice.
__DICE__ = [".", ".", ".", "L", "C", "R"]

#####     TESTING STUFF, SKIP IT.
# When this list is empty rolls will actually come from the random number generator
__testng_preroll__ = []
# a flag for tracking if any real dice were rolled
__real_roll__ = False
def check_testing():
    """ returns true if testing went as expected relative to the dice function"""
    return not __real_roll__ and len(__testng_preroll__) == 0

def stage_for_testing(value):
    for letter in value:
        __testng_preroll__.insert(0, letter)

#####    SKIP TO THIS ONE. ALL THE DICE STUFF LIVES HERE, THE REST IS TESTING
def roll_die():
    """Rolls an LCR game, returning either ".", "L", "C", or "R" depending on the dice roll."""
    if len(__testng_preroll__) == 0:
        global __real_roll__
        __real_roll__= True
        # Only this line really has anything to do with the random dice rolls, the rest is to help me with testing.
        return random.choice(__DICE__)
    else:
        return __testng_preroll__.pop()

