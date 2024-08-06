"""6317 Midterm Real Estate
Write a Python script to print the count of houses that meet the criteria
 and a list of all matching addresses.
You also need to prompt the user for each criteria
 (state code, living area, min & max cost, and elementary name).
For living area and cost, make sure the user enters valid numbers
and ask them to retry if an invalid entry is detected (no crashing!).


References
-----------
OpenAI. (2023). ChatGPT. https://chat.openai.com
"""

_auther_ = "Jim <cxp220025@utdallas.edu>"

from valid_check import get_valid_numeric_input, validate_input
from parcels import parcels

# Extract unique values for state_code and elementary_name
state_codes = set(parcel['state_code'] for parcel in parcels)
elementary_names = set(parcel['CAMPNAME'] for parcel in parcels)

# Prompt the user for criteria
state_code = validate_input("Enter state code (e.g., 'A1'): ", state_codes)
min_living_area = get_valid_numeric_input("Enter minimum living area (sq ft): ")

min_market_value = get_valid_numeric_input("Enter minimum market value: $")
max_market_value = get_valid_numeric_input("Enter maximum market value: $")
while max_market_value < min_market_value:
    print("The maximum market value should be greater than or equal to the minimum market value.")
    max_market_value = get_valid_numeric_input("Enter maximum market value: $")

elementary_name = validate_input("Enter elementary school name(e.g., 'ALDRIDGE EL'): ", elementary_names)

# Filter properties that meet the criteria
matching_properties = []

for parcel in parcels:
    if (
        parcel['state_code'] == state_code and
        parcel['living_area'] >= min_living_area and
        min_market_value <= parcel['market_value'] <= max_market_value and
        parcel['CAMPNAME'] == elementary_name
    ):
        matching_properties.append(parcel)
# print(matching_properties)

# Print the count of matching houses and their addresses
print(f"Number of houses that meet the criteria: {len(matching_properties)}\n")
if matching_properties:
    print("Matching Addresses: \n")
    for property in matching_properties:
        print(property['street_address'])
else:
    print("No matching houses were found.")





