from .logger import log_conversion

def celisus_to_farhaniet(celsius):
    """
    this is a function that converts
    temprature form celsius scale to farhanite scale
    """
    fahr = (celsius *9/5) + 32
    log_conversion(celsius,'Celsius',fahr, 'Fahrenheit')
    return fahr

def farhanite_to_celsius(fahr):
   """
   this is a function that converts
   temprature form farhanite scale to celsius scale
    example :
    >> fahrenite_to_celsius(32)
    >> 0
    
   """
   celsius= (fahr -32) *5/9
   log_conversion(fahr,'Fahrenheit',celsius, 'Celsius')
   return celsius

def celisus_to_Kelvin(celisus):
    """
    this is a fucntion that converts celisus to Kelvin.
    Example:
     >>celisus_to_Kelvin(0)
     >> 273.15
     """
    Kelvin= celisus + 273.15
    log_conversion(celisus,'Celsius',Kelvin, 'Kelvin')
    return Kelvin

def Kelvin_to_Celisus(Kelvin):
    """
    This function converts Kelvin to Celisus.
    Example
    >>Kelvin_to_Celisus(273.15)
    >>0
    """
    celisus= Kelvin -273.15
    log_conversion(Kelvin,'Kelvin',celisus, 'Celsius')
    return celisus

def Kelvin_to_Fahrenheit(Kelvin):
    """
    This function changes Kelvin to Fahrenheit
    """
    Fahrenheit = ((Kelvin- 273.15) * (9/5)) + 32
    log_conversion(Kelvin,'Kelvin',Fahrenheit, 'Fahrenheit')
    return Fahrenheit

def Fahrenheit_to_Kelvin(Fahrenheit):
    """
    This function is usd to convert Farhenhit to KElvin scale
    """
    Kelvin = ((Fahrenheit - 32) * (5/9)) + 273.15
    log_conversion(Fahrenheit,'Fahrenheit',Kelvin, 'Kelvin')
    return Kelvin
