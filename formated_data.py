import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv(r"C:\Users\SWAPNIL JAIN\Desktop\dataset\Sign-language\dataset.csv")
df = df.drop("Timestamp", axis=1)

# Define ranges and corresponding labels
ranges_and_labels = [
    (1, 217, "A"), (218, 367, "B"), (368, 502, "C"), (503, 651, "D"),
    (652, 813, "E"), (814, 987, "F"), (988, 1134, "G"), (1135, 1218, "H"),
    (1219, 1321, "I"), (1322, 1396, "J"), (1397, 1555, "K"), (1556, 1652, "L"),
    (1653, 1746, "M"), (1747, 1881, "N"), (1882, 1998, "O"), (1999, 2155, "P"),
    (2156, 2266, "Q"), (2267, 2392, "R"), (2393, 2480, "S"), (2481, 2549, "T"),
    (2550, 2621, "U"), (2622, 2741, "V"), (2742, 2826, "W"), (2827, 2917, "X"),
    (2918, 3026, "Y"), (3027, 3093, "Z")
]

# Function to normalize data
def normalize_data(dataframe):
    # scaler = MinMaxScaler()
    # numeric_cols = dataframe.select_dtypes(include=["float64", "int64"]).columns
    # dataframe[numeric_cols] = scaler.fit_transform(dataframe[numeric_cols])  # Normalize numeric columns only
    return dataframe

# Process each range and assign the corresponding label
all_labels = []
for start, end, label in ranges_and_labels:
    label_df = df.iloc[start - 1:end].copy()  # Extract the range
    label_df = normalize_data(label_df)  # Normalize
    label_df["gesture"] = label  # Add gesture column
    all_labels.append(label_df)

# Combine all labels into one dataset
final_df = pd.concat(all_labels, axis=0)

# Round values to 5 decimal places
final_df = final_df.round(5)

# Save the final dataset
final_df.to_csv('final_dataset.csv', index=False)
