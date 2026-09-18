import math

# Board positions:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

board = [" "] * 9


def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    # AI wins
    if check_winner("O"):
        return 1

    # User wins
    if check_winner("X"):
        return -1

    # Draw
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def user_move():
    while True:
        try:
            position = int(input("Enter your move (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number from 1 to 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("That position is already occupied.")
                continue

            board[index] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


def play_game():
    print("===== TIC-TAC-TOE =====")
    print("You are X. Computer is O.")

    print("\nBoard positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    display_board()

    while True:
        # User's turn
        user_move()
        display_board()

        if check_winner("X"):
            print("🎉 You win!")
            break

        if is_draw():
            print("It's a draw!")
            break

        # Computer's turn
        print("Computer is thinking...")
        ai_move()
        display_board()

        if check_winner("O"):
            print("💻 Computer wins!")
            break

        if is_draw():
            print("It's a draw!")
            break


# Start the game
play_game()