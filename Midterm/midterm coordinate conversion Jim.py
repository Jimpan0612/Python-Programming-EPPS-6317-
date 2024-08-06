"""6317 Midterm Coordinate Conversion
Write a script to convert Decimal Degree (DD) latitude/longitude coordinates
 into Degree-Minute-Second (DMS) coordinates.
Your program should behave in an identical fashion,
taking input coordinates in DD format and outputting them in DMS.
The script should return an error message if the user inputs
 invalid coordinates (e.g. letters or numbers out-of-range).
Graduates should prompt the user to run another conversion when finished.


References
-----------
Decimal degrees. (2023). In Wikipedia. https://en.wikipedia.org/wiki/Decimal_degrees

Convert DD (decimal degrees) to DMS (degrees minutes seconds) in Python.
(2010). StackOverflow.
https://stackoverflow.com/questions/2579535/convert-dd-decimal-degrees-to-dms-degrees-minutes-seconds-in-python

OpenAI. (2023). ChatGPT. https://chat.openai.com
"""

_auther_ = "Jim <cxp220025@utdallas.edu>"

# Function to convert Decimal Degrees (DD) to Degree-Minute-Second (DMS)
def dd_to_dms(coord, is_latitude):
    degrees = int(abs(coord))
    minutes_float = (abs(coord) - degrees) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60
    # TRUE or False
    if is_latitude is True:
        if coord >= 0:
            direction = "N"
        else:
            direction = "S"
    else:
        if coord >= 0:
            direction = "E"
        else:
            direction = "W"

    # Use the Unicode value for the degree symbol (°)
    degree_symbol = "\u00b0"

    return f"{degrees}{degree_symbol} {minutes}' {seconds:.1f}\" {direction}"


# Main program loop
while True:
    # Prompt user for latitude and longitude input in Decimal Degrees (DD)
    while True:
        latitude_input = input("Enter a Decimal Degree latitude: ")
        if latitude_input.replace(".", "", 1).lstrip('-').isdigit():
            latitude = float(latitude_input)
            if -90 <= latitude <= 90:
                print(f"{latitude:.1f}")
                break
            else:
                print("Invalid entry. Latitude must be ±90°.")
        else:
            print("Invalid entry. Decimal degrees must be numeric.")

    while True:
        longitude_input = input("Enter a Decimal Degree longitude: ")
        if longitude_input.replace(".", "", 1).lstrip('-').isdigit():
            longitude = float(longitude_input)
            if -180 <= longitude <= 180:
                print(f"{longitude:.1f}")
                break
            else:
                print("Invalid entry. Longitude must be ±180°.")
        else:
            print("Invalid entry. Decimal degrees must be numeric.")

    # Convert to DMS
    dms_latitude = dd_to_dms(latitude, is_latitude=True)
    dms_longitude = dd_to_dms(longitude, is_latitude=False)

    # Print DMS coordinates
    print("\nResult:")
    print(dms_latitude)
    print(dms_longitude)

    another_conversion = input("\nEnter another? (Y/N) ").strip().lower()
    if another_conversion != "y" and another_conversion != "yes":
        print("\nClose program")
        break






