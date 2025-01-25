def celisus_to_farhaniet(celsius):
    """
    this is a function that converts
    temprature form celsius scale to farhanite scale
    """
    fahr = (celsius *9/5) + 32
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
   return celsius 
