import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]
del df["Mass"]
del df["Radius"]

df.to_csv('main.csv') 