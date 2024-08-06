"""6317 Midterm Real Estate
Confirm whether the entered value is valid


References
-----------
OpenAI. (2023). ChatGPT. https://chat.openai.com
"""

_auther_ = "Jim <cxp220025@utdallas.edu>"

def get_valid_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        # Check if the input is a numeric string
        if user_input.replace(".", "", 1).isdigit():
            return float(user_input)
        else:
            print("Invalid input. Please enter a valid number.")

def validate_input(prompt, valid_values):
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_values:
            return user_input
        else:
            print("Invalid input. Please try again.")
