def read_file_with_line_numbers(filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"Line{line_number}: {line}", end='')  # Avoid double newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
read_file_with_line_numbers('sample.txt')
