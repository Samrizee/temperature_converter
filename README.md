# Temprature Converter

A simple Python package fro converting tempratures between celsius and  farhanite

## Installation

Clone the repository and Navigate into the Directory 

```bash
$ git clone https://github.com/Samrizee/temperature_converter.git
$ cd temprature_converter
$ pip install -e .
```

## add Python envirmental variable
```bash
$ echo $PYTHONPATH

$ export PYTHONPATH=$PYTHONPATH:/localpath/temperature_converter

```


## Running Unit test

To run tests, navigate to the test directory and run:


```bash
$ cd test
$ python -m unittest test_converter.py
```

## Usage

Import the conversion functions, open python on terminal on the root folder temperature_converter

```bash
$ cd ..
$ ipython
```

```python
from temprature_converter.converter import celsius_to_farhanite, farhanite_to_celcius
print (celisus_to_farhaniet(26))
print (farhanite to celsius(77))
```


## use the command-line interface for temperature conversions(CLI)usage

To Use this temprature converter from Command-Line Interface, go to the root folder, temperature_converter

```bash

cd ../temperature_converter
python -m temperature_converter.cli 100 Celsius Fahrenheit  #this will convert 100 Celsius to Fahrenheit
python -m temperature_converter.cli 10 Celsius Kelvin  # this will convert 10 Celsius to Kelvin
python -m temperature_converter.cli 30 Fahrenheit Kelvin # this will convert 30 Fahrenheit to Kelvin
python -m temperature_converter.cli 50 Fahrenheit Celsius # this will convert 50 Fahrenheit to Celsius
python -m temperature_converter.cli 200 Kelvin Fahrenheit # this will convert 200 Kelvin to Fahrenheit
python -m temperature_converter.cli 300 Kelvin Celsius # this will convert  300 Kelvin to Celsius

```

## log file

See [temperature_conversion.log](temperature_conversion.log) for a record of all temperature conversions.



 
