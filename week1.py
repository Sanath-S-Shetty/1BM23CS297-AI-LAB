def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        board[row][col] = current_player

        win = False
        for i in range(3):
            if all(board[i][j] == current_player for j in range(3)) or \
               all(board[j][i] == current_player for j in range(3)):
                win = True
                break
        if not win and (all(board[i][i] == current_player for i in range(3)) or \
                        all(board[i][2 - i] == current_player for i in range(3))):
            win = True

        if win:
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()