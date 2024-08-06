#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:16:13 2023

@author: jimpan
"""

class Parcel:
    def __init__(self, landuse, value):
        """
        

        Parameters
        ----------
        landuse : str
            Zoning class(e.g. SFR)
        value : int
            Parcel value indollars

        Returns
        -------
        None.

        """
        self.landuse = landuse
        self.value = value
    
    def assessment(self):
                
        if self.landuse == "SFR":
            # If single-family residence, tax at 5%
            rate = 0.05
        elif self.landuse == "MFR":
            rate  = 0.04
        else:
            rate = 0.02
        assessments = self.value * rate
        return assessments
    
    