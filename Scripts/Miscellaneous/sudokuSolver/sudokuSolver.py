# check the validity of the value at particular position
def isvalid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    x = pos[1] // 3
    y = pos[0] // 3

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


# print the board
def printb(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# check if board is already solved
def empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None


# recursive function to solve the board
def solve(board):
    find = empty(board)
    if not find:
        return True
    row, col = find

    for i in range(1, 10):
        if isvalid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


if __name__ == "__main__":
    board = []
    print(
        "=" * 5,
        "Enter Values separated by space and use 0 for empty values",
        "=" * 5,
    )
    for i in range(9):
        row = input(f"Enter row {i+1} values: ")
        row = row.split(" ")
        row = list(
            map(int, row)
        )  # converting every element from the row from string to int
        board.append(row)  # appending row to the board
    print("=" * 5, "Unsolved State", "=" * 5)
    printb(board)
    solve(board)
    print("=" * 5, "Solved State", "=" * 5)
    printb(board)
