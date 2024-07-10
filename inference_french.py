import pandas as pd
import random as rn
import numpy as np



print("The probability rate should be between 0 and 1. If you want to make it more coming select 0.55, if you want to eliminate it select 0.02")

df = pd.read_json('francais_dataset_after_mistake.json', orient ='split')

def select_item(df):
    return np.random.choice(df['anglais'], p=df['Coefficient']/100)


while True:
    sentence = select_item(df)
    mask = df['anglais'].str.contains(sentence, case=False, na=False)
    item_number = df.loc[mask].index[0]
    print(sentence)
    answer_french = input()
    print(df['francais'][item_number])
