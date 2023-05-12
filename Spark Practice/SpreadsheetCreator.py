import pyspark
import openpyxl
import os
import pandas as pd

workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet["A1"] = 'Name'
worksheet["B1"] = 'Age'
worksheet["A2"] = "Krish"
worksheet["B2"] = "31"
worksheet["A3"] = "Sudhansh"
worksheet["B3"] = "30"
worksheet["A4"] = "Sunny"
worksheet["B4"] = "29"
worksheet["C1"] = "Experience"
worksheet["C2"] = "10"
worksheet["C3"] = "8"
worksheet["C4"] = "4"

workbook.save('Test1.xlsx')

df = pd.read_excel('Test1.xlsx')
df.to_csv('Test1.csv', index=False)
