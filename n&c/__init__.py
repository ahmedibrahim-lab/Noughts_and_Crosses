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

if __name__ == '__main__':
    main()
