#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:47:40 2023

@author: jimpan
"""

import csv

def listheadernames(csvfilepath):
    """
    

    Parameters
    ----------
    csvfilepath : str
        Path to speccify csv files.

    Returns
    -------
    List

    """

    with open(csvfilepath) as csv_file:
        reader = csv.reader(csv_file)
        headers = reader.__next__()
        headerlist = []
        for header in headers:
            headerlist.append(header)
            # print(headerlist)
    # Return list back to calling code
    return headerlist

# other way
# if __name__ == "__main__": ensures that the next block of code is run only if the mylist.py script is run by itself. 
if __name__ == "__main__":        
    streests_csv = r"/Users/jimpan/Documents/EPPS 6317/Labs/lab4/lab4 files/streets.csv"
    headernames = listheadernames(streests_csv)
    print(headernames)
