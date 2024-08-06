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
- **Description**: Created a comprehensive data analysis and visualization dashboard using Python, Plotly, and Dash. The dashboard integrates financial data from TSMC and Samsung, as well as geopolitical event data for East Asia.
- **Features**:
  - **Geopolitical Events Dashboard**: Visualizes daily relationship intensity trends and geopolitical events on a map. As shown in the image, this map begins playing from January 1st of the selected year and displays the number of major geopolitical events in East Asian countries each month, with colors indicating whether the events are positive or negative.
  - **Financial Data Comparison**: Compares financial metrics (Total Assets, Total Liabilities, and Total Liabilities and Equity) between TSMC and Samsung over the years.
  - **Interactive Components**: Includes dropdowns for selecting years and financial metrics, and displays detailed event lists and financial comparisons.

### Main Components

1. **Geopolitical Events Visualization**
   - **Daily Intensity Trend**: Line chart showing the trend of relationship intensity over time.
   - **Geopolitical Events Map**: Scatter geo map visualizing geopolitical events with intensity and location. This map begins playing from January 1st of the selected year and displays the number of major geopolitical events in East Asian countries each month, with colors indicating whether the events are positive or negative.
   - **Event List**: List of top events for the selected date.

2. **Financial Data Analysis**
   - **Financial Metric Comparison**: Bar chart comparing selected financial metrics between TSMC and Samsung.
   - **Total Assets Trend**: Line chart showing the trend of total assets over the years for both companies.

### Example Code Snippets

#### Daily Intensity Trend
```python
fig = px.line(
    daily_intensity_sum,
    x='Event Date',
    y='Intensity',
    title=f'Daily Relationship Intensity Trend - Year {selected_year}',
    labels={'Intensity': 'Daily Intensity Sum', 'Event Date': 'Date'},
    line_shape='linear',
    render_mode='svg',
    markers=True,
    template='plotly',
    hover_data={'Intensity': True, 'Event Date': '|%B %d, %Y'}
)
