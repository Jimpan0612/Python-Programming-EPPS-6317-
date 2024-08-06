"""6317 Lab4 mycount
Program to creat a basic function mycount to counts the number of empty fields in a header of a csv file

References
-----------

"""

_auther_ = "Jim <cxp220025@utdallas.edu>"

import csv

def countnullfields(csvfilepath):
    """
    Count the number of empty fields in the header of a CSV file.

    Parameters
    ----------
    csvfilepath : str
        Path to the CSV file.

    Returns
    -------
    int
        Number of empty fields in the header. Returns zero if there are no empty fields.
    """
    with open(csvfilepath) as csv_file:
        reader = csv.reader(csv_file)
        # Get the header row or an empty list if there are no headers
        headers = next(reader, [])  
        empty_count = headers.count('')
        return empty_count

# if __name__ == "__main__": ensures that the next block of code is run only if the mylist.py script is run by itself
if __name__ == "__main__":
    streests_csv = r"/Users/jimpan/Documents/EPPS 6317/Labs/lab4/lab4 files/streets.csv" 
    empty_field_count = countnullfields(streests_csv)
    # The f before the string allows you to embed expressions inside string literals, using curly braces {} to enclose the expressions
    print(f"Number of empty fields in the header: {empty_field_count}")
