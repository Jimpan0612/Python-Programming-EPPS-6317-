"""6317 Midterm File Manipulation
Write a Python script to open and print any CSV file's contents with proper tab
 spacing. Create a function that accepts the filename parameter and
 performs the opening/printing task.
The script's main body will call this function.
The script should work with any CSV file.
The script shoild ask the user what directory to search for CSVs in.
Search through all child directories as well.
For each CSV you encounter, pass to your function to print it out.
Make sure the script does not crash if the directory entered does not exist
 or if no CSV files are found.
 

References
-----------
Python os.walk() Method. Tutorialspoint.
 https://www.tutorialspoint.com/python/os_walk.htm
 
Python os Module. W3Schools. https://www.w3schools.com/python/module_os.asp

OpenAI. (2023). ChatGPT. https://chat.openai.com
"""

_auther_ = "Jim <cxp220025@utdallas.edu>"

import os
import csv

# Function to print the contents of a CSV file
def print_csv_contents(filename):
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print('\t'.join(row))

# Function to list CSV files in the specified directory and its subdirectories
def list_csv_files(directory):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files

# Main program logic
def main():
    # Ask the user for the directory path
    directory = input("Enter the directory path to search for CSV files: ")
    
    # Check if the directory exists
    if not os.path.exists(directory):
        print("Directory not found.")
        return
    
    # List CSV files in the specified directory and subdirectories
    csv_files = list_csv_files(directory)
    
    # Check if any CSV files were found
    if not csv_files:
        print("No CSV files were found in the specified directory.")
        return
    
    print("CSV files found:\n")
    
    # List the found CSV files with numbers for selection
    for i, file_path in enumerate(csv_files, start=1):
        print(f"{i}. {file_path}\n")
    
    while True:
        # Ask the user to select a CSV file by number or exit
        choice = input("Enter the number of the CSV file you want to print (0 to exit): ")
        if choice == "0":
            print("Exit program")
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(csv_files):
                selected_file = csv_files[choice - 1]
                print(f"Selected CSV file: {selected_file}\n")
                print("Contents:")
                print_csv_contents(selected_file)
            else:
                print("Invalid choice. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()




