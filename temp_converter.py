import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

# Streamlit app layout
st.title("Temperature Converter")

# Input for temperature value
temperature_value = st.number_input("Enter temperature value", value=0.0)

# Select the input and output units
input_unit = st.selectbox("Select the input unit", ("Celsius", "Fahrenheit", "Kelvin"))
output_unit = st.selectbox("Select the output unit", ("Celsius", "Fahrenheit", "Kelvin"))

# Convert the temperature
converted_value = None

if input_unit == "Celsius":
    if output_unit == "Fahrenheit":
        converted_value = celsius_to_fahrenheit(temperature_value)
    elif output_unit == "Kelvin":
        converted_value = celsius_to_kelvin(temperature_value)
    else:
        converted_value = temperature_value

elif input_unit == "Fahrenheit":
    if output_unit == "Celsius":
        converted_value = fahrenheit_to_celsius(temperature_value)
    elif output_unit == "Kelvin":
        converted_value = fahrenheit_to_kelvin(temperature_value)
    else:
        converted_value = temperature_value

elif input_unit == "Kelvin":
    if output_unit == "Celsius":
        converted_value = kelvin_to_celsius(temperature_value)
    elif output_unit == "Fahrenheit":
        converted_value = kelvin_to_fahrenheit(temperature_value)
    else:
        converted_value = temperature_value

# Display the result
if converted_value is not None:
    st.write(f"{temperature_value} {input_unit} is equal to {converted_value:.2f} {output_unit}")
