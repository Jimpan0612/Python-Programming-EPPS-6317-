# Python Programming for Social Science (EPPS/GISC 4317/6317)

## Course Overview

This course, taught by Dr. Bryan Chastain at The University of Texas at Dallas, introduces computer programming skills and their application in social sciences using Python. Topics covered include fundamental programming syntax, control structures, numerical and scientific computation, visualization, and social data analytics. Students are expected to programmatically design and build projects related to social sciences.

## Midterm Project

### Real Estate Analysis
- **Description**: Developed a Python script to help real estate agents identify potential homes for clients in a hot market. The script filters homes based on specific criteria such as single-family house type, minimum living area, market value range, and school zoning.
- **Features**:
  - Prompts the user for criteria like state code, living area, cost, and elementary school name.
  - Ensures valid input for living area and cost.
  - Outputs the count and addresses of homes that meet the criteria.

### Coordinate Conversion
- **Description**: Created a script to convert Decimal Degree (DD) latitude/longitude coordinates into Degree-Minute-Second (DMS) coordinates.
- **Features**:
  - Accepts input coordinates in DD format and outputs them in DMS.
  - Returns an error message for invalid coordinates.
  - Prompts the user to run another conversion when finished.

### File Manipulation
- **Description**: Developed a Python script to open and print the contents of CSV files with tabs delimiting the columns for proper spacing.
- **Features**:
  - Prompts the user for a directory to search for CSVs.
  - Searches through all child directories and prints contents of each CSV found.
  - Ensures the script does not crash if the directory does not exist or if no CSV files are found.

## Final Project

### Data Analysis and Visualization Dashboard

**Description**: Developed a comprehensive data analysis and visualization dashboard using Dash and Plotly to present financial and geopolitical data.

**Features**:
- **Data Integration**: Merged financial data from TSMC and Samsung, and geopolitical event data for East Asia.
- **Visualization**:
  - Line chart showing daily intensity trend of geopolitical events.
  - Interactive geopolitical events map.
  - Comparative bar chart for financial metrics of TSMC and Samsung.
  - Total assets line chart for TSMC and Samsung.

### Financial Data Visualization
- **TSMC and Samsung Financial Data**: Visualized financial data of TSMC and Samsung from CSV files.
- **Dashboard Example**:
  ![Financial Comparison Chart](images/financial_comparison_chart.png)
  ![Total Assets Chart](images/total_assets_chart.png)

### Geopolitical Event Analysis
- **Geopolitical Events in East Asia**: Visualized geopolitical events with a focus on event intensity.
- **Dashboard Example**:
  ![Geopolitical Map](images/geopolitical_map.png)
  ![Daily Intensity Chart](images/daily_intensity_chart.png)

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Jimpan0612/Python-Programming-EPPS-6317-.git
   cd Python-Programming-EPPS-6317-
