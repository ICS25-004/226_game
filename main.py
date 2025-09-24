from Board import Board
from Player import Player


#Initialize Board and Player
b = Board(5, '5')
p1 = Player('One', 0)

def runGame():
    game_active = True
    while game_active:
        print('---Treasure Hunt---')
        print(b)
        try:
            print("Select a Row & Column...")
            print("Row: ")
            row = int(input())
            if row < 0 or row > b.n - 1:
                raise ValueError

            print("Column: ")
            col = int(input())
            if col < 0 or col > b.n - 1:
                raise ValueError
        except ValueError:
            print("\033[31mInvalid Input. Try again.\033[0m")
            #continue to the next turn
            continue

        p1.add_score(int(b.pick(row, col)))
        print(p1.__str__())

runGame()