# CSCI 1913, Spring 2020, Lab 2
# Student Names:
# Omar Masri!
# Brandon Weinstein!
# MASRI013@umn.edu
# WEINS127@umn.edu

from lcr_die import roll_die

center_coins = 0

def lcr_over(coins):
   
    if coins.count(0) == (len(coins) - 1):
        return True

    else:
        return False
    # Return true if all elements are 0 except one of them
    # Return false if there are more than one element with a non-zero


def lcr_winner(coins):
    winner = coins.index(max(coins))
    #print(center_coins, winner_coins)
    return winner
    # Is called if lcr_over() returns true


def left(coins, player):
    coins[player] -= 1
    coins[player - 1] += 1
    # Should reduce player's coin count by 1 and then add 1 to the player on the left


def right(coins, player):
    coins[player] -= 1
    coins[(player + 1) % len(coins)] += 1
    # Should reduce player's coin count by 1 and add 1 to player on right


def center(coins, player):
    coins[player] -= 1
    global center_coins
    center_coins += 1
    # Should reduce player's coin count by 1 and add it to the ground


def lcr_game(num_players):
    coins = [3] * num_players
    rounds = 0
    is_winner = False
    while not is_winner:
        for player in range(len(coins)):
            rounds += 1
            if coins[player] <= 3:
                for i in range(coins[player]):
                    roll = roll_die() 
                    check_roll(coins, roll, player)
                    if lcr_over(coins):
                        winner = (lcr_winner(coins), rounds)
                        return winner
            elif coins[player] > 3:
                for i in range(3):
                    roll = roll_die()
                    check_roll(coins, roll, player)
                    if lcr_over(coins):
                        winner = (lcr_winner(coins), rounds)
                        return winner   
    # Should play a full game of LCR
    # Start each player with 3 coins with player[0] going first
    # Print out winner and rounds it took in tuple


def most_common_winner(num_players):
    winners = [0] * num_players
    for i in range(2000):
        winner_tuple = lcr_game(num_players)
        winners[winner_tuple[0]] += 1
    max_winner = winners.index(max(winners))
    percent_winner = max(winners)/sum(winners)
    return max_winner, percent_winner

# simulate 2000 games
# count each winner
# figure out the player with most wins and percentage that person won
def check_roll(coins, roll, player):
    if roll == "L":
        left(coins, player)

    elif roll == "R":
        right(coins, player)

    elif roll == "C":
        center(coins, player)
   