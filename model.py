import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

data = pd.read_csv("final_dataset.csv")
# data1 = pd.read_csv("normalised_test_dataset.csv")

'''print("Dataset Preview:")
print(data.head())'''

X = data.drop("gesture",axis=1) 
y = data["gesture"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=15, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("Classification Report:")
print(classification_report(y_test, y_pred))
# print(model.predict(data1))

# Save the model
joblib.dump(model, "random_forest_model.pkl")
print("Model saved as random_forest_model.pkl")