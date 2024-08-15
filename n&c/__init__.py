import string

def create_grid(size):
    if not size:
        raise ValueError("Input cannot be empty.")
    
    if not size.isdigit():
        raise ValueError("Input must be a number.")
    
    size = int(size)
    grid = []
    
    for _ in range(size):
        grid.append(['.'] * size)
        
    return grid

def display_grid(grid):
    if not grid:
        raise ValueError("Grid not found.")
    
    lowercase_letters = list(string.ascii_lowercase)
    size = len(grid)
    
    # Define the column labels
    col_labels = '   ' + '  '.join(lowercase_letters[:size])
    
    print(col_labels)
    # Print the grid with row labels
    for i, row in enumerate(grid, start=1):
        print(f"{i}  {'  '.join(row)}")

def check_row(player, grid, row_number):
    return all(item == player for item in grid[row_number])

def check_column(player, grid, column_number):
    return all(row[column_number] == player for row in grid)

def check_diagonals(player, grid):
    size = len(grid)
    
    # Main diagonal
    if all(grid[i][i] == player for i in range(size)):
        return True
    
    # Secondary diagonal
    if all(grid[i][size - 1 - i] == player for i in range(size)):
        return True

    return False

def has_someone_won(player, grid, row_number, column_number):
    if (check_row(player, grid, row_number) or
            check_column(player, grid, column_number) or
            check_diagonals(player, grid)):
        print(f"{player} has won. Congratulations!")
        return True
    return False

def is_odd(number):
    return number % 2 != 0
    
def is_even(number):
    return number % 2 == 0

def letter_to_number(letter):
    return ord(letter) - ord('a')

def is_grid_full(grid):
    return all(item != '.' for row in grid for item in row)

def main():
    size = input("Enter the size of the grid you want to play in (1-9): ")

    while not (size.isdigit() and 1 <= int(size) <= 9):
        size = input("Sorry but that is not a valid input. Please try again: ")

    print("Grid is of size: " + size + ' x ' + size)
    grid = create_grid(size)
    display_grid(grid)
    player1 = 'X'
    player2 = 'O'
    turn = 1
    
    while not is_grid_full(grid):
        current_player = player1 if is_odd(turn) else player2
        player_number = 1 if current_player == player1 else 2
        
        try:
            row_number = int(input(f"Player {player_number}, enter the row number: ")) - 1
            column_letter = input(f"Player {player_number}, enter the column letter: ").lower()
            column_number = letter_to_number(column_letter)
            
            if grid[row_number][column_number] == '.':
                grid[row_number][column_number] = current_player
                display_grid(grid)
                if has_someone_won(current_player, grid, row_number, column_number):
                    break
                turn += 1
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
    
    if is_grid_full(grid):
        print("It's a draw!")

if __name__ == '__main__':
    main()
