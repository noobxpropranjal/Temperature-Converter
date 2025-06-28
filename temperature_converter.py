def convert_temperature(temp, unit):
    """
    Convert temperature between Fahrenheit and Celsius.

    Parameters:
    temp (float): The temperature to convert.
    unit (str): 'F' if the input temperature is in Fahrenheit, 'C' if in Celsius.

    Returns:
    float: The converted temperature rounded to 2 decimal places.
    """
    if unit == 'F':
        # Fahrenheit to Celsius
        celsius = (temp - 32) * 5/9
        return round(celsius, 2)
    elif unit == 'C':
        # Celsius to Fahrenheit
        fahrenheit = (temp * 9/5) + 32
        return round(fahrenheit, 2)
    else:
        # Invalid unit
        print("Invalid unit. Please use 'F' or 'C'.")
        return None

# Test the function
print(convert_temperature(100, 'F'))  # Should print 37.78
print(convert_temperature(0, 'C'))    # Should print 32.0

# Interactive input
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit of the input temperature ('F' or 'C'): ")

result = convert_temperature(temp, unit)
if result is not None:
    print(f"Converted temperature: {result}")
