import argparse
from temperature_converter.converter import (
    celisus_to_farhaniet,
    farhanite_to_celsius,
    celisus_to_Kelvin,
    Kelvin_to_Celisus,
    
    )
from temperature_converter.logger import log_conversion

def convert_temperature(value, input_unit, output_unit):
    """
    Converts a temperature from one unit to another.
    """
    # Convert input temperature to Celsius first (if necessary)
    if input_unit == "Celsius":
        celsius = value
    elif input_unit == "Fahrenheit":
        celsius = farhanite_to_celsius(value)
    elif input_unit == "Kelvin":
        celsius = Kelvin_to_Celisus(value)
    else:
        raise ValueError(f"Unsupported input unit: {input_unit}")

    # Convert Celsius to the desired output unit
    if output_unit == "Celsius":
        result = celsius
    elif output_unit == "Fahrenheit":
        result = celisus_to_farhaniet(celsius)
    elif output_unit == "Kelvin":
        result = celisus_to_Kelvin(celsius)
    else:
        raise ValueError(f"Unsupported output unit: {output_unit}")

    # Log the conversion
    log_conversion(value, input_unit, result, output_unit)

    return result

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    parser.add_argument("value", type=float, help="The temperature value to convert.")
    parser.add_argument("input_unit", type=str, choices=["Celsius", "Fahrenheit", "Kelvin"], help="The unit of the input temperature.")
    parser.add_argument("output_unit", type=str, choices=["Celsius", "Fahrenheit", "Kelvin"], help="The unit of the output temperature.")

    # Parse arguments
    args = parser.parse_args()

    # Perform conversion
    try:
        result = convert_temperature(args.value, args.input_unit, args.output_unit)
        print( f"\n🌡️  {args.value:.2f} {args.input_unit} is equal to {result:.2f} {args.output_unit}.\n")
    except ValueError as e:
        print(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    main()