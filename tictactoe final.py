board = [
    [".", ".", ".", ], #row 0
    [".", ".", ".", ], #row 1
    [".", ".", ".", ], #row 2
]
def printBoard(grid):
    for row in grid:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print()

current_player = "X"


def checkWinner(current_player,grid):
    for i in range(len(grid)): #This is going to pull all indices from [0,1,2]
        if grid[i][0] == grid[i][1] == grid[i][2] == current_player:
            print(f"Player {current_player} wins with a row victory")
            return True
    
    if grid[0][0] == grid[1][1] == grid[2][2] == current_player:
        print(f"{current_player} wins with a diagonal victory")
    
    if grid[0][2] == grid[1][1] == grid[2][0] == current_player:
        print(f"{current_player} wins with a right diagonal victory!")
        return True
    
    for i in range(len(grid[0])):
        if grid[0][i] == grid[1][i] == grid[2][i] == current_player:
            print(f"{current_player} wins with a column victory!")
            return True

def switchPlayer(current_player):
    if current_player == "X":
        return "O"
    if current_player == "O":
        return "X"

printBoard(board)

player = "X"
print(player)
player = switchPlayer(player)
print(player)

def main ():
    board = [
    [".", ".", ".", ], #row 0
    [".", ".", ".", ], #row 1
    [".", ".", ".", ], #row 2
]
player = "O"
check = True

while check == True:
    print(f"{player}'s turn")
    printBoard(board)
    row = int(input("enter the row you want to place your piece:"))
    col = int(input("enter the column you want to place your piece:"))
    board[row][col] = player
    if checkWinner(player,board) == True:
        check = False
    player = switchPlayer(player)

main()
    




