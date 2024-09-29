
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit) :
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius) :
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result

def main():
    temperature_value = float(input("Enter the temperature to convert: "))
    value_to_convert = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()

    if value_to_convert == 'F' or value_to_convert == 'C' :
        match value_to_convert :
            case 'F' :
                print(f'{temperature_value}°{value_to_convert} is {convert_to_celsius(temperature_value)}°C')
            case 'C' :
                print(f'{temperature_value}°{value_to_convert} is {convert_to_fahrenheit(temperature_value)}°F')

if __name__ == "__main__" :
    main()
