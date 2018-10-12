GamePositions = [1,2,3,4,5,6,7,8,9]
PlayerSymbols = ['X', 'O']
GameMoves = 0
WonPlayer = None
GameMovesCounter = 9
Position = None

def TicTacToePlay():
    while (True):
        global GameMoves
        global WonPlayer
        global GameMovesCounter
        global Position
        if GameMoves % 2 == 0:
            Player1 = 'X'
            print("Player {} turn".format(Player1))
            Position = int(input("Enter the Position for your input between (1 to 9): "+"\n"))
            if (Position > 0) and (Position < 10) and GamePositions[Position-1] in PlayerSymbols:
                print("Please choose a different number Position as the other user has occupied that Position!")
                continue
            elif (Position > 0) and (Position < 10):
                GameMoves += 1
                WonPlayer = Player1
            else:
                print("Please choose a number between 1-9 only!")
                continue
        elif GameMoves % 2 == 1:
            Player2 = 'O'
            print("Player {} turn".format(Player2))
            Position = int(input("Enter the Position for your input between (1 to 9): "+"\n"))
            if (Position > 0) and (Position < 10) and GamePositions[Position-1] in PlayerSymbols:
                print("Please choose a different number Position as the other user has occupied that Position!")
                continue
            elif (Position > 0) and (Position < 10):
                GameMoves += 1
                WonPlayer = Player2
            else:
                print("Please choose a number between 1-9 only!")
                continue
        GamePositions[Position-1] = WonPlayer
        GameMovesCounter -= 1
        TicTacToeBoard()
        WinStatus = TicTacToeWinCheck()
        if WinStatus == 1:
            print("Player {} Won this game and you played Awesome!".format(WonPlayer))
            break
        elif GameMovesCounter == 0:
            print("No Player won!")
            break


def TicTacToeBoard():
    print(" {} | {} | {}".format(GamePositions[0] , GamePositions[1] , GamePositions[2]))
    print(" {}   {}   {}".format('-','-','-'))
    print(" {} | {} | {}".format(GamePositions[3] , GamePositions[4] , GamePositions[5]))
    print(" {}   {}   {}".format('-','-','-'))
    print(" {} | {} | {}".format(GamePositions[6] , GamePositions[7] , GamePositions[8]))

def TicTacToeWinCheck():
    if GamePositions[2] == 'X' and GamePositions[4] == 'X' and GamePositions[6] == 'X':
        return 1
    elif GamePositions[0] == 'X' and GamePositions[4] == 'X' and GamePositions[8] == 'X':
        return 1
    elif GamePositions[0] == 'X' and GamePositions[1] == 'X' and GamePositions[2] == 'X':
        return 1
    elif GamePositions[3] == 'X' and GamePositions[4] == 'X' and GamePositions[5] == 'X':
        return 1
    elif GamePositions[6] == 'X' and GamePositions[7] == 'X' and GamePositions[8] == 'X':
        return 1
    elif GamePositions[0] == 'X' and GamePositions[3] == 'X' and GamePositions[6] == 'X':
        return 1
    elif GamePositions[1] == 'X' and GamePositions[4] == 'X' and GamePositions[7] == 'X':
        return 1
    elif GamePositions[2] == 'X' and GamePositions[5] == 'X' and GamePositions[8] == 'X':
        return 1
    elif GamePositions[2] == 'O' and GamePositions[4] == 'O' and GamePositions[6] == 'O':
        return 1
    elif GamePositions[0] == 'O' and GamePositions[4] == 'O' and GamePositions[8] == 'O':
        return 1
    elif GamePositions[0] == 'O' and GamePositions[1] == 'O' and GamePositions[2] == 'O':
        return 1
    elif GamePositions[3] == 'O' and GamePositions[4] == 'O' and GamePositions[5] == 'O':
        return 1
    elif GamePositions[6] == 'O' and GamePositions[7] == 'O' and GamePositions[8] == 'O':
        return 1
    elif GamePositions[0] == 'O' and GamePositions[3] == 'O' and GamePositions[6] == 'O':
        return 1
    elif GamePositions[1] == 'O' and GamePositions[4] == 'O' and GamePositions[7] == 'O':
        return 1
    elif GamePositions[2] == 'O' and GamePositions[5] == 'O' and GamePositions[8] == 'O':
        return 1

if __name__ == "__main__":
    GamePlay = TicTacToePlay()

