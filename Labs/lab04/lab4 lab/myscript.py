#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:01:11 2023

@author: jimpan
"""
import csv
import mylist


streests_csv = r"/Users/jimpan/Documents/EPPS 6317/Labs/lab4/lab4 files/streets.csv"
    
headernames = mylist.listheadernames(streests_csv)
print(headernames)