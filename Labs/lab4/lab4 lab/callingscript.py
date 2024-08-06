"""6317 Lab4 callingscript
Program to test the mycount.py

References
-----------

"""

_auther_ = "Jim <cxp220025@utdallas.edu>"

# import mycount and get the countnullfields function
from mycount import countnullfields


streests_csv = r"/Users/jimpan/Documents/EPPS 6317/Labs/lab4/lab4 files/streets.csv"
empty_field_count = countnullfields(streests_csv)
print(f"Number of empty fields in the header: {empty_field_count}")