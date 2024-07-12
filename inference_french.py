import streamlit as st

import pandas as pd
import random as rn
import numpy as np

st.title("Pratiquer le francais")


@st.cache_data
def load_data():
    df = pd.read_json('francais_training_dataset.json', orient ='split')
    return df

def select_item(df):
    return np.random.choice(df['anglais'])

data = load_data()
sentence = select_item(data)
mask = data['anglais'].str.contains(sentence, case=False, na=False)
item_number = data.loc[mask].index[0]
french = data['francais'][item_number]

st.write(sentence)

@st.experimental_fragment
def fragment():
    user_input = st.text_input("Traduit le phrase en francais")
    st.write(user_input)

    if st.button("Montre"):
        st.write(french)

fragment()
st.button("Essaye encore!")
