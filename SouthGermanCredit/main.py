import pandas as pd 
import os 

df = pd.read_csv(r'SouthGermanCredit.asc') 
df.to_csv ('converted.csv')