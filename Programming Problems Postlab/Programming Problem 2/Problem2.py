def navigate_file():
    """Navigates through the lines of text in a file."""

    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return  # Exit the function if the file isn't found
    except Exception as e: # Catch other potential file errors
        print(f"An error occurred while reading the file: {e}")
        return

    num_lines = len(lines)

    while True:
        print(f"\nThe file has {num_lines} lines.")
        try:
            line_number = int(input("Enter a line number (0 to quit): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Go back to the beginning of the loop

        if line_number == 0:
            break  # Exit the loop and end the program
        elif 1 <= line_number <= num_lines:
            # Important: list indices start at 0, so we subtract 1
            print(f"Line {line_number}: {lines[line_number - 1].rstrip()}")  #rstrip() removes trailing newline
        else:
            print("Invalid line number. Please enter a number between 1 and", num_lines)

if __name__ == "__main__":
    navigate_file()
