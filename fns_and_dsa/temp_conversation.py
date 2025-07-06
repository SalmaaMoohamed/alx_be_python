FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

temperature = float(input("Enter the temperature to convert: "))

tempKind = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(fahrenheit):
   fahrenheit = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
   print(temperature, "°C is", fahrenheit)

def convert_to_fahrenheit(celsius):
    celsius = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(temperature, "°F is", celsius)

    if tempKind == "C":
        convert_to_fahrenheit(temperature)
    elif tempKind == "F":
        convert_to_celsius(temperature)
    else:
        print("Invalid temperature. Please enter a numeric value.")
        exit(1)