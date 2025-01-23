import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv(r"C:\Users\SWAPNIL JAIN\Desktop\dataset\Sign-language\testing.csv")
df = df.drop("Timestamp",axis =1)
df = df.round(5)

# Divide the dataset into different labels
label_0 = df.iloc[1:479].copy()
label_1 = df.iloc[479:901].copy()
label_2 = df.iloc[901:1279].copy()
label_3 = df.iloc[1279:1639].copy()
label_4 = df.iloc[1639:1995].copy()

# Function to normalize data and add the 'gesture' column
def normalize_data_and_add_label(dataframe, label):
    scaler = MinMaxScaler()
    dataframe.iloc[:, :] = scaler.fit_transform(dataframe)  # Normalize all columns
    dataframe["gesture"] = label  # Add a new column for the gesture label
    return dataframe

# Normalize data and add gesture column
label_0 = normalize_data_and_add_label(label_0, "0")
label_1 = normalize_data_and_add_label(label_1, "1")
label_2 = normalize_data_and_add_label(label_2, "2")
label_3 = normalize_data_and_add_label(label_3, "3")
label_4 = normalize_data_and_add_label(label_4, "4")

# Combine all labels into one dataset
final_df = pd.concat([label_0, label_1, label_2, label_3, label_4], axis=0)

# Save or inspect the final dataframe
# print(final_df.head())
final_df.to_csv('normalised_data.csv',index=False)
