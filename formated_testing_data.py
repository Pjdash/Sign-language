import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv(r"C:\Users\SWAPNIL JAIN\Desktop\dataset\Sign-language\testing.csv")
df = df.drop("Timestamp",axis =1)


# Function to normalize data and add the 'gesture' column
def normalize_data_and_add_label(dataframe):
    # scaler = MinMaxScaler()
    # dataframe.iloc[:, :] = scaler.fit_transform(dataframe)  # Normalize all columns
    return dataframe

df_new = normalize_data_and_add_label(df)
df_new=df_new.round(5)
df_new.to_csv("normalised_test_dataset.csv",index=False)