import string, random, os
from datetime import datetime

def create_grid(size):
    """ Creates the grid for the game to be played on."""
    size = int(size)
    grid = []

    for _ in range(size):
        grid.append(['.'] * size)

    return grid

def display_grid(grid):
    """ Responsible for showing the grid in console."""
    if not grid:
        raise ValueError("Grid not found.")

    lowercase_letters = list(string.ascii_lowercase)
    size = len(grid)

    # Define the column labels
    col_labels = '   ' + '  '.join(lowercase_letters[:size])

    print(col_labels)

    # Print the grid with row labels
    for i, row in enumerate(grid, start=1):
        row_display = [f"{cell}" for cell in row]
        print(f"{i}  {'  '.join(row_display)}")

def log_game_step(file, grid, player, move, step):
    """ Tracks the step count, player number and their move for logging in the text file. """
    with open(file, "a") as f:
        f.write(f"\nStep {step}: Player {player}\n")
        f.write(f"Move: {move}\n")
        for i, row in enumerate(grid, start=1):
            row_display = [f"{cell}" for cell in row]
            f.write(f"{i}  {'  '.join(row_display)}\n")
        f.write("\n")

def log_winner(file, winner):
    """ Logs the winner to the text file."""
    with open(file, "a") as f:
        f.write(f"Winner: {winner}\n")

def check_row(player, grid, row_number):
    """ Checks a given row for winning condition."""
    return all(item == player for item in grid[row_number])

def check_column(player, grid, column_number):
    """ Checks a given column for winning condition."""
    return all(row[column_number] == player for row in grid)

def check_diagonals(player, grid):
    """ Checks both diagonals for winning condition."""
    size = len(grid)

    # Main diagonal
    if all(grid[i][i] == player for i in range(size)):
        return True

    # Secondary diagonal
    if all(grid[i][size - 1 - i] == player for i in range(size)):
        return True

    return False

def has_someone_won(player, grid, row_number, column_number):
    """ Returns whether a given player has won."""
    if (check_row(player, grid, row_number) or
            check_column(player, grid, column_number) or
            check_diagonals(player, grid)):
        print(f"{player} has won. Congratulations!")
        return True
    return False

def is_odd(number):
    """ Checks if a number is odd."""
    return number % 2 != 0

def letter_to_number(letter):
    """ Converts a letter to its index number in the alphabet."""
    return ord(letter) - ord('a')

def is_grid_full(grid):
    """ Checks whether the grid has been filled. """
    return all(item != '.' for row in grid for item in row)

def parse_input(input_str, size):
    """ Parses the move input string, returning a row and column value."""
    input_str = input_str.strip().lower()
    row, col = None, None
    for char in input_str:
        if char.isdigit():
            row = int(char) - 1
        elif char.isalpha():
            col = letter_to_number(char)
    if row is None or col is None or row >= size or col >= size:
        raise ValueError("Invalid input")
    return row, col

def ai_move(grid, player):
    """ Logic for the AI player."""
    size = len(grid)
    opponent = 'O' if player == 'X' else 'X'

    # Check for winning move or block opponent
    for r in range(size):
        for c in range(size):
            if grid[r][c] == '.':
                # Simulate move
                grid[r][c] = player
                if has_someone_won(player, grid, r, c):
                    return r, c
                # Undo move
                grid[r][c] = '.'

                # Simulate opponent's move
                grid[r][c] = opponent
                if has_someone_won(opponent, grid, r, c):
                    grid[r][c] = '.'  # Undo opponent move
                    return r, c
                # Undo opponent move
                grid[r][c] = '.'

    # If no winning/blocking move found, choose a random available spot
    available_moves = [(r, c) for r in range(size) for c in range(size) if grid[r][c] == '.']
    if available_moves:
        return random.choice(available_moves)
    return None, None

def main():
    size = input("Enter the size of the grid you want to play in (3-9): ")

    while not (size.isdigit() and 3 <= int(size) <= 9):
        size = input("Sorry but that is not a valid input. Please try again: ")

    size = int(size)
    mode = input("Enter '1' for two players, '2' for player vs AI: ")

    while mode not in ('1', '2'):
        mode = input("Invalid mode. Enter '1' for two players, '2' for player vs AI: ")

    # Setting up the logging directory and file
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'Games')
    os.makedirs(base_dir, exist_ok=True)
    log_filename = f"Game_{datetime.now().strftime('%d-%M-%Y_%H-%M-%S')}.txt"
    log_file = os.path.join(base_dir, log_filename)
    
    with open(log_file, "w") as f:
        f.write(f"Tic Tac Toe Game Log - Grid Size: {size}x{size}\n")

    print(f"Grid is of size: {size} x {size}")
    grid = create_grid(size)
    display_grid(grid)
    player1 = 'X'
    player2 = 'O'
    turn = 1
    
    while not is_grid_full(grid):
        current_player = player1 if is_odd(turn) else player2
        player_number = 1 if current_player == player1 else 2
        
        if mode == '2' and current_player == player2:  # AI player
            row_number, column_number = ai_move(grid, current_player)
            if row_number is not None:
                grid[row_number][column_number] = current_player
                move = f"{row_number+1}{chr(column_number + ord('a'))}"
                print(f"AI player {player_number} chose move: {move}")
                display_grid(grid)
                log_game_step(log_file, grid, player_number, move, turn)
                if has_someone_won(current_player, grid, row_number, column_number):
                    log_winner(log_file, f"Player {player_number} (AI)")
                    break
                turn += 1
            else:
                print("No available moves for AI.")
                break
        else:  # Human player
            try:
                user_input = input(f"Player {player_number}, enter the row and column (e.g., '1a' or 'a1'): ")
                row_number, column_number = parse_input(user_input, size)
                
                if grid[row_number][column_number] == '.':
                    grid[row_number][column_number] = current_player
                    display_grid(grid)
                    log_game_step(log_file, grid, player_number, user_input, turn)
                    if has_someone_won(current_player, grid, row_number, column_number):
                        log_winner(log_file, f"Player {player_number}")
                        break
                    turn += 1
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
    
    if is_grid_full(grid):
        print("It's a draw!")
        log_winner(log_file, "Draw")

if __name__ == '__main__':
    main()
