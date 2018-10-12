GamePositions = [1,2,3,4,5,6,7,8,9]
PlayerSymbols = ['X', 'O']
GameMoves = 0
WonPlayer = None

def TicTacToePlay():
    while (True):
        global GameMoves
        global WonPlayer
        if GameMoves % 2 == 0:
            Player1 = 'X'
            print("Player {} turn".format(Player1))
            GameMoves += 1
            WonPlayer = Player1
        elif GameMoves % 2 == 1:
            Player2 = 'O'
            print("Player {} turn".format(Player2))
            GameMoves += 1
            WonPlayer = Player2
        position = int(input("Enter the position for your input between (1 to 9): "+"\n"))
        if (position > 0 and position < 10) and GamePositions[position-1] not in PlayerSymbols:
            GamePositions[position-1] = WonPlayer
            TicTacToeBoard()
            WinStatus = TicTacToeWinCheck()
            if WinStatus == 1:
                print("Player {} Won this game and you played Awesome!".format(WonPlayer))
                break
            continue
        elif position > 9:
            print("Please choose a number between 1-9 only!")
            continue
        else:
            print("Please choose a different number position as the other user has occupied that position!")
            continue


def TicTacToeBoard():
    print(" {} | {} | {}".format(GamePositions[0] , GamePositions[1] , GamePositions[2]))
    print(" {}   {}   {}".format('-','-','-'))
    print(" {} | {} | {}".format(GamePositions[3] , GamePositions[4] , GamePositions[5]))
    print(" {}   {}   {}".format('-','-','-'))
    print(" {} | {} | {}".format(GamePositions[6] , GamePositions[7] , GamePositions[8]))

def TicTacToeWinCheck():
    if GamePositions[2] == 'X' and GamePositions[4] == 'X' and GamePositions [6] == 'X':
        return 1
    elif GamePositions[0] == 'X' and GamePositions[4] == 'X' and GamePositions [8] == 'X':
        return 1
    elif GamePositions[0] == 'X' and GamePositions[1] == 'X' and GamePositions [2] == 'X':
        return 1
    elif GamePositions[3] == 'X' and GamePositions[4] == 'X' and GamePositions [5] == 'X':
        return 1
    elif GamePositions[6] == 'X' and GamePositions[7] == 'X' and GamePositions [8] == 'X':
        return 1
    elif GamePositions[0] == 'X' and GamePositions[3] == 'X' and GamePositions [6] == 'X':
        return 1
    elif GamePositions[1] == 'X' and GamePositions[4] == 'X' and GamePositions [7] == 'X':
        return 1
    elif GamePositions[2] == 'X' and GamePositions[5] == 'X' and GamePositions [8] == 'X':
        return 1
    elif GamePositions[2] == 'O' and GamePositions[4] == 'O' and GamePositions [6] == 'O':
        return 1
    elif GamePositions[0] == 'O' and GamePositions[4] == 'O' and GamePositions [8] == 'O':
        return 1
    elif GamePositions[0] == 'O' and GamePositions[1] == 'O' and GamePositions [2] == 'O':
        return 1
    elif GamePositions[3] == 'O' and GamePositions[4] == 'O' and GamePositions [5] == 'O':
        return 1
    elif GamePositions[6] == 'O' and GamePositions[7] == 'O' and GamePositions [8] == 'O':
        return 1
    elif GamePositions[0] == 'O' and GamePositions[3] == 'O' and GamePositions [6] == 'O':
        return 1
    elif GamePositions[1] == 'O' and GamePositions[4] == 'O' and GamePositions [7] == 'O':
        return 1
    elif GamePositions[2] == 'O' and GamePositions[5] == 'O' and GamePositions [8] == 'O':
        return 1

GamePlay = TicTacToePlay()

