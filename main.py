import random

moves = {1:'Rock',2:'Paper',3:'Scissors'}     
winning_combinations = {tuple([1,3]) : 'rock beats scissors', tuple([3,2]) : 'scissors beats paper', tuple([2,1]) : 'paper beats rock'}
losing_combinations = {tuple([3,1]) : 'scissors loses to rock', tuple([2,3]) : 'paper loses to scissors', tuple([1,2]) : 'rock loses to paper'}

class Player:
    def __init__(self):
        self.name = input("Select name: ")
        self.winner = False
        self.moves = []
        self.move = ''
        self.wins = 0
        self.losses = 0
        self.ties = 0
        if self.name == 'cpu':
            self.is_cpu = True
        else:
            self.is_cpu = False

    def make_move(self):
        if self.is_cpu:
            move = random.randint(1,3)
        else:
            move = input("Select your move Rock (1), Paper (2), Scissors (3) ")
         
        if is_valid_move(move):
            move = int(move)
            print(f"{self.name} threw {moves[move]}")
            self.moves.append(move)
            self.move = move
        else:
            self.make_move()

    def count_wins(self):
        return self.wins

def get_score(player_1, player_2):
    return f"SCORE: {player_1.name} - {player_1.wins}, {player_2.name} - {player_2.wins}"


def is_valid_move(move) -> bool:
    if isinstance(move, int) and move in moves:
        return True
    if isinstance(move, str) and move.isdigit() and int(move) in moves:
        return True
    else:
        print("ERROR: Please make a selection between 1-3")
        return False

def determine_outcome(player_1, player_2):
    if player_1.move == player_2.move:
        player_1.ties += 1
        player_2.ties += 1
        return "Tie"
    moves = tuple([player_1.move, player_2.move])
    if moves in winning_combinations:
        player_1.winner = True
        player_1.wins += 1
        player_2.losses += 1
        return winning_combinations[moves]
        
    else:
        player_2.winner = True
        player_2.wins += 1
        player_1.losses += 1
        return losing_combinations[moves]
    
def conclude_round(player_1, player_2):
    print(f"Player {player_1.name} total wins: {player_1.wins}, Player {player_2.name} total wins: {player_2.wins}")
    if player_1.wins == player_2.wins:
        print("TIE!!!!")
    elif player_1.wins > player_2.wins:
        print(f"{player_1.name} is the winner")
    else:
        print(f"{player_2.name} is the winner")


def start_game():
    count = 0
    game_is_active = True
    rounds = int(input('Select how many rounds: '))
    player_1 = Player()
    player_2 = Player()


    while (game_is_active):
        player_1.winner = False
        player_2.winner = False
        player_1.make_move()
        player_2.make_move()

        print(determine_outcome(player_1, player_2))
        print(get_score(player_1, player_2))
        count += 1

        if count >= rounds:
            conclude_round(player_1, player_2)  
            game_is_active = False          
            return game_is_active


if __name__ == '__main__':
    start_game()















