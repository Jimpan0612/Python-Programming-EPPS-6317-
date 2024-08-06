# Python Programming for Social Science (EPPS/GISC 4317/6317)

## Course Overview

This course, taught by Dr. Bryan Chastain at The University of Texas at Dallas, introduces computer programming skills and their application in social sciences using Python. Topics covered include fundamental programming syntax, control structures, numerical and scientific computation, visualization, and social data analytics. Students are expected to programmatically design and build projects related to social sciences.

## Midterm Project

### Objectives
Your midterm will have three components spanning the material covered thus far in class.

### Real Estate
- **Description**: You are a real estate agent who has clients interested in buying a new house in Collin County near UTD. It is a hot market, so you want to find existing homes that meet your clients’ criteria and then ask the owners if they are interested in selling.
- **Requirements**:
  - Single-family house (state_code='A1')
  - At least 1500 sq ft of living area
  - Market value between $250,000 and $350,000
  - Located in the area zoned to Aldridge Elementary (CAMPNAME='ALDRIDGE EL')
- **Task**: Write a Python script to prompt the user for each criterion and print the count and list of addresses. Ensure valid input for living area and cost.

### Coordinate Conversion
- **Description**: Write a script to convert Decimal Degree (DD) latitude/longitude coordinates into Degree-Minute-Second (DMS) coordinates.
- **Requirements**:
  - Accepts input coordinates in DD format and outputs them in DMS.
  - Returns an error message for invalid coordinates.
- **Task**: Prompt the user to run another conversion when finished.

### File Manipulation
- **Description**: Write a Python script that opens a CSV file and prints out the contents with tabs delimiting the columns for proper spacing.
- **Requirements**:
  - Ask the user for a directory to search for CSVs in, and print contents for each CSV found.
- **Task**: Ensure the script does not crash if the directory entered does not exist or if no CSV files are found.

## Final Project

### Description
The final project involves creating a comprehensive data analysis and visualization dashboard.

1. **Main Program**: `Data Analysis and Visualization.ipynb`
   - **Description**: The first half of the code is for testing and experimentation, and the second half contains the full version of the dashboard code and a segmented version of the dashboard code.
   
2. **Geo Data Filter**: `geo data filter EA.ipynb` located in `geo data/geo data east asia/`
   - **Description**: This program cleans and merges all geo events data.

3. **Data Files**:
   - `geo data` folder contains the geo events data and the data cleaning program.
   - `samsung financial` folder contains the Samsung data and the data cleaning program.
   - `TSMC financial` folder contains the TSMC data and the data cleaning program.

### Requirements
- Create a data analysis and visualization dashboard using Python.
- Clean and merge data from various sources.
- Use visualization tools to present the data effectively.

## Midterm Project Details
### Real Estate
You are a real estate agent who has clients who are interested in buying a new house in Collin County near UTD. It is a hot market so you cannot wait for homes to go for sale. Instead you want to find existing homes that meet your clients’ criteria and then ask the owners if they are interested in selling. Your clients want a single-family house (state_code=’A1’) with at least 1500 sq ft of living area (“living_area”) and a market value (“market_value”) between $250000 and $350000. They also have children and want to live in the area zoned to Aldridge Elementary (CAMPNAME=’ALDRIDGE EL’).

A file named “parcels.py” has been provided to you that contains a variable named parcels which is a list of dictionaries. Each dictionary contains the above-mentioned keys as well as street_address for a parcel. To access this data in your script you just need to import this file and then you should be able to use the parcels variable (from parcels import parcels).

Write a Python script to print the count of houses that meet the criteria as well as a list of all of the matching addresses. You also need to prompt the user for each criteria (state code living area min & max cost and elementary name). For living area and cost make sure the user enters valid numbers and ask them to retry if invalid entry is detected (no crashing!).

### Coordinate Conversion
Write a script to convert Decimal Degree (DD) latitude/longitude coordinates into Degree-Minute-Second (DMS) coordinates. Your program should behave in an identical fashion taking input coordinates in DD format and outputting them in DMS. The script should return an error message if the user inputs invalid coordinates (e.g. letters or numbers out-of-range). Prompt the user to run another conversion when finished.

### File Manipulation
Write a Python script that opens a CSV file and prints out the contents with tabs delimiting the columns for proper spacing. You should write a function that accepts the filename as the parameter that does the actual work of opening and printing. The main body of the script will just call this function for opening/printing. It should work on any CSV not just the one provided. Ask the user what directory to search for CSVs in. Search through all child directories as well. For each CSV you encounter pass to your function to print it out. Make sure the script does not crash if the directory entered does not exist or if no CSV files are found.

---

請按照以下步驟更新README文件：

### 更新README的步驟

1. **導航到存儲庫的根目錄**：
   ```sh
   cd ~/Python-Programming-EPPS-6317-
