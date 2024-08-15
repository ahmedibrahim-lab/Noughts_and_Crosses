import string

# Define function to create a grid of dimensions size x size
def create_grid(size):
    
    # Check for empty string
    if not size:  
        raise ValueError("Input cannot be empty.")
    
    # Check for invalid inputs
    if not all(char in '0123456789' for char in size):
        raise ValueError("Input must be a number.")
    
    size = int(size)
    
    # Initialise variables
    grid = []
    row = []
    
    for x in range(size):
        row.append('.')
    
    for x in range(size):
        grid.append(row)
        
    return grid

def display_grid(grid):
    
    if not grid:  
        raise ValueError("Grid not found.")
    
    lowercase_letters = list(string.ascii_lowercase)
    size = len(grid)
    
    # Define the column labels
    col_labels = '   '
    for x in range(size):
        col_labels += lowercase_letters[x] + '  '

    # Print the grid with row labels
    for i, row in enumerate(grid, start=1):
        # Print the row label and the row values
        print(f"{i}  ", end='')
        print('  '.join(row))

    # Print the column labels
    print(col_labels)

def check_row(player, grid, row_number):
    """Checks if all elements in the specified row match the player's marker."""
    # Iterate over each element in the specified row
    for item in grid[row_number]:
        if item != player:
            return False  # If any element doesn't match, return None
    return True  # If all elements match, return the player's marker

def check_column(player, grid, column_number):
    """Checks if all elements in the specified column match the player's marker."""
    # Iterate over each row in the grid
    for row in grid:
        # Check if the element in the current row at the column_number doesn't match the player
        if row[column_number] != player:
            return False  # If any element doesn't match, return None
    return True  # If all elements match, return the player's marker

def check_diagonals(player, grid):
    size = len(grid)
    diag_1 = []
    diag_2 = []

    # Collect the main diagonal elements
    for i in range(size):
        diag_1.append(grid[i][i])

    # Collect the secondary diagonal elements
    for i in range(size):
        diag_2.append(grid[i][size - 1 - i])

    # Check if all elements in the main diagonal match the player
    if all(item == player for item in diag_1):
        return player
    
    # Check if all elements in the secondary diagonal match the player
    if all(item == player for item in diag_2):
        return True

    return False

def has_someone_won(player, grid, row_number, column_number):
    
    if check_row(player, grid, row_number) or check_column(player, grid, column_number) or check_diagonals(player, grid):
        print(player + " has won. Congratulations!")
        return True
    else:
        return False
    
def is_odd(number):
    """Returns True if the number is odd, False otherwise."""
    return number % 2 != 0
    
def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

def letter_to_number(letter):
    """Converts a lowercase letter to a number where 'a' is 0, 'b' is 1, etc."""
    return ord(letter) - ord('a')

def is_grid_full(grid):
    """Check if a specific element exists in the grid."""
    for row in grid:
        for item in row:
            if item == '.':
                return False
    return True

def main():
    
    # Get input from user
    size = input("Enter the size of the grid you want to play in (1-9): ")

    # Validation loop
    while not all(char in '0123456789' for char in size):
        size = input("Sorry but that is not a valid input. Please try again: ")
        
    while int(size) < 1 or int(size) > 9:
        size = input("Sorry but that is not a valid input. Please try again: ")

    print("Grid is of size: " + size + ' x ' + size)
    grid = create_grid(size)
    display_grid(grid)
    player1 = 'X'
    player2 = 'O'
    turn = 1
    while is_grid_full(grid) == False:
        if is_odd(turn):
            row_number = int(input("Player 1, please place your X by putting in the corresponding row number: ")) - 1
            column_number = letter_to_number(input("Player 1, please place your X by putting in the corresponding column letter: "))
            grid[row_number][column_number] = 'X'
            if (has_someone_won(player1, grid, row_number, column_number)):
                break
            turn += 1
        if is_even(turn):
            row_number = int(input("Player 2, please place your O by putting in the corresponding row number: ")) - 1
            column_number = letter_to_number(input("Player 2, please place your O by putting in the corresponding column letter: "))
            grid[row_number][column_number] = 'O'
            if (has_someone_won(player2, grid, row_number, column_number)):
                break
            turn += 1
        
            
             
        

if __name__ == '__main__':
    main()
