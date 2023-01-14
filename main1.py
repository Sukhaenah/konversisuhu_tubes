import streamlit as st

st.title('KONVERSI SUHU')

temp = st.number_input ("Masukkan Nilai Suhu", 0)

from_unit = st.radio(
    "Masukkan satuan suhu awal",
    ('Celcius', 'Kelvin', 'Fahrenheit', 'Reamur'))

to_unit = st.radio(
    "Masukkan satuan suhu tujuan",
    ('Celcius', 'Kelvin', 'Fahrenheit', 'Reamur'))

# Fungsi untuk mengkonversi suhu ke derajat Celsius
def to_celsius(temp, unit):
    if unit in ('Fahrenheit'):
        return (temp - 32) * 5 / 9
    elif unit in ('Kelvin'):
        return temp - 273
    elif unit in ('Reamur'):
        return (temp) * 5 / 4
    else:
        return temp

# Fungsi untuk mengkonversi suhu dari derajat Celsius ke unit yang diinginkan
def from_celsius(temp, unit):
    if unit in ('Fahrenheit'):
        return temp * 9 / 5 + 32
    elif unit in ('Kelvin'):
        return temp + 273
    elif unit in ('Reamur'):
        return temp * 4 / 5 
    else:
        return temp

hitung = st.button ("HASIL")

if hitung :
    converted_temp = from_celsius(to_celsius(temp, from_unit), to_unit)
    st.success (f'{temp} {from_unit} = {converted_temp} {to_unit}')