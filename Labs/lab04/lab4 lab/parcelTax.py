"""6317 Lab4 parceltax 
Modify the parceltax.py script so that it determines the property tax for each parcel and stores these values in a list. 
You should use the class created in the parcelclass.py script above (remain the class unchanged). 
Print the values of the final list by FID. 


References
-----------

"""

_auther_ = "Jim <cxp220025@utdallas.edu>"


import csv
import parcelclass

# Create an empty list to store tax values
tax_values = []

# Open the CSV file and read its contents
with open('/Users/jimpan/Documents/EPPS 6317/Labs/lab4/lab4 files/parcels.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row if it exists
    next(csv_reader, None)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract data from the row
        fid, landuse, value = int(row[0]), row[1], int(row[2])
        
        # Create an instance of the Parcel class
        myparcel = parcelclass.Parcel(landuse, value)
        
        # Calculate the tax assessment
        mytax = myparcel.assessment()
        
        # Append the tax value to the list
        tax_values.append((fid, mytax))

# Print the tax values by FID
for fid, tax_value in tax_values:
    print(f"FID {fid} has a tax value of {tax_value:.1f}")
