import pandas as pd

def read_data_frequency():
    data = pd.read_csv('data/filtered_df.csv', index_col=[0])
    data = data.reset_index().drop("index", axis=1)
    return data.sort_values(by='count', ascending=False)

def read_verbs():
    return pd.read_csv('data/verbs.csv', index_col=[0])