# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/21
# Gets the user input of a temperature in Celsius then
# Converts it to Fahrenheit. Uses a special function which
# is called.


def convert_to_fahrenheit():
    # Title
    print("Celsius To Fahrenheit!")

    # User input for temperature in Celsius
    celsius = input(("Enter temperature in Celsius: "))

    # Try Catch to make sure the input is a float
    try:
        celsius_float = float(celsius)
    except Exception:
        print("Please enter a number!")
    else:
        # Calculating the temperature in fahrenheit
        fahrenheit = (9 / 5) * celsius_float + 32

        # Displaying the temperature in fahrenheit
        print("The temperature in fahrenheit is {:.2f}!".format(fahrenheit))


# Calling the function convert_to_fahrenheit()
def main():
    convert_to_fahrenheit()


if __name__ == "__main__":
    main()
