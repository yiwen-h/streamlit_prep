import streamlit as st

import numpy as np
import pandas as pd
import random

st.markdown("""# This is a header
## This is a sub header
This is text
\n **I really really love cats**
""")

def get_random_number():
    random_number = random.randint(1,99)
    return random_number
st.write(get_random_number())

get_random_number()

@st.cache_data
def cached_random_number():
    return get_random_number()

st.write(cached_random_number())


df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
