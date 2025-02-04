# Temprature Converter

A simple Python package fro converting tempratures between celsius and  farhanite

## Installation

Clone the repository and Navigate into the Directory 

```bash
$ git clone https://github.com/Samrizee/temperature_converter.git
$cd temprature_converter
$pip install -e .
```

## Usage

Import the conversion functions

```python
from temprature_converter.converter import celsius_to_farhanite, farhanite_to_celcius
print (celisus_to_farhaniet(26))
print (farhanite to celsius(77))
```
## Running Unit test

To run tests, navigate to the test directory and run:

```bash
$ python -m unittest test_converter.py
```


## CLI usage

To Use this temprature converter from Command-Line Interface, go to the root folder, temperature_converter

```bash

cd /Pypi/temperature_converter
python -m temperature_converter.cli 100 Celsius Fahrenheit -- this will convert 100 Celsius to Fahrenheit
python -m temperature_converter.cli 10 Celsius Kelvin -- this will convert 10 Celsius to Kelvin
python -m temperature_converter.cli 30 Fahrenheit Kelvin -- this will convert 30 Fahrenheit to Kelvin
python -m temperature_converter.cli 50 Fahrenheit Celsius -- this will convert 50 Fahrenheit to Celsius
python -m temperature_converter.cli 200 Kelvin Fahrenheit -- this will convert 200 Kelvin to Fahrenheit
python -m temperature_converter.cli 300 Kelvin Celsius -- this will convert  300 Kelvin to Celsius

```




 
