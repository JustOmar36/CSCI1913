from lcr_die import roll_die

def lcr_over(coins):
    if coins.count(0) == (len(coins) - 1):
        return True

    else:
        return False
    #Return true if all elements are 0 except one of them
    #Return false if there are more than one element with a non-zero



def lcr_winner(coins):
    winner_coins = max(coins) + center_coins
    winner = coins.index(max(coins))
    return winner
    #Is called if lcr_over() returns true


def left(coins, player):

    coins[player] -= 1
    coins[player - 1] += 1
    #Should reduce player's coin count by 1 and then add 1 to the player on the left


def right(coins, player):

    coins[player] -= 1
    coins[(player + 1) % len(coins)] += 1
    #Should reduce player's coin count by 1 and add 1 to player on right
    #coins[(player + 1)%len(coins)]

def center(coins, player):

    coins[player] -= 1
    global center_coins
    center_coins += 1
    #Should reduce player's coin count by 1 and add it to the ground

def lcr_game(num_players):
    coins = [3] * num_players
    rounds = 0
    is_winner = False
    while is_winner:
        for player in coins:
            if coins[player] <= 3:
                for i in range(coins[player]):
                    roll = roll_die()
                    check_roll(coins, roll, player)
            elif coins[player] > 3:
                for i in range(3):
                    roll = roll_die()
                    check_roll(coins, roll, player)
        is_winner = lcr_over(coins)
        rounds += 1
    winner = (lcr_winner(coins), rounds)




    #Should play a full game of LCR
    #Start each player with 3 coins with player[0] going first
    #Print out winner and rounds it took in tuple

def most_common_winner(num_players):
    #simulate 2000 games
    #count each winner
    #figure out the player with most wins and percentage that person won
def check_roll(coins, roll, player):
    if roll == "L":
        left(coins, player)

    elif roll == "R":
        right(coins, player)

    elif roll == "C":
        center(coins, player)
