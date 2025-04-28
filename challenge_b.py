import csv

def read_and_print_csv(file_path: str):
    """
    Reads a CSV file and prints its content to the console.

    Parameters:
    file_path (str): The path to the CSV file.
    """
    csv.field_size_limit(3000 * 1024)
    try:
        with open(file_path, mode="r", newline="", encoding="ASCII") as file:
            reader = csv.reader(file)
            row1 = next(reader)
            print("alphabetical string: " + row1[0] + "\n")
            print("real number: " + row1[1] + "\n")
            print("integer: " + row1[2]  + "\n")
            print("alphanumeric: " + row1[3].strip() + "\n")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # TODO: allow the user to enter a filename at a console prompt
    csv_file_path = "objects.csv"
    read_and_print_csv(csv_file_path)