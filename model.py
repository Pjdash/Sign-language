import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load Local Data
# Replace 'your_data.csv' with the path to your local CSV file
data = pd.read_csv("imu_dataset.csv")
data1 = pd.read_csv("testing.csv")
# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Step 2: Preprocess the Data
# Assume the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # All columns except the last as features
y = data.iloc[:, -1]   # Last column as target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the Model
# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model with the training data
model.fit(X_train, y_train)

# Step 4: Test the Model
# Predict on the test data
y_pred = model.predict(X_test)

# Step 5: Evaluate the Model
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))
print(model.predict(data1))