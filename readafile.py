import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("offers-1000.csv")

print(df.head())         
print(df.info())          
print(df.describe())