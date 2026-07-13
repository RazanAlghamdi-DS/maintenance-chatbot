import os

os.chdir(r"C:\Users\razan\Desktop\AI")

import pandas as pd

df = pd.read_csv("ai2020.csv")

print(df.shape)
print(df.head())

import os
os.chdir(r"C:\Users\razan\Desktop\AI")

import pandas as pd

df = pd.read_csv("ai2020.csv", sep=";")

print(df.shape)
print(df.head())

print(df.info())
print(df.isnull().sum())


print(df["Machine failure"].value_counts())

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


data = df.copy()


data = data.drop(["UDI", "Product ID"], axis=1)


le = LabelEncoder()
data["Type"] = le.fit_transform(data["Type"])


X = data.drop("Machine failure", axis=1)
y = data["Machine failure"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

import joblib

joblib.dump(model, "machine_failure_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("Model Saved Successfully")