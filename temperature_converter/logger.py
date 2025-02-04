import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='temperature_conversion.log',
    filemode='a'  # Append mode to avoid overwriting logs
)

def log_conversion(input_temp, input_unit, output_temp, output_unit):
    """
    Logs the temperature conversion details.

    Args:
        input_temp (float): The input temperature value.
        input_unit (str): The unit of the input temperature (e.g., 'Celsius', 'Fahrenheit', 'Kelvin').
        output_temp (float): The converted temperature value.
        output_unit (str): The unit of the output temperature (e.g., 'Celsius', 'Fahrenheit', 'Kelvin').
    """
    logging.info(f"Conversion: {input_temp} {input_unit} -> {output_temp} {output_unit}")