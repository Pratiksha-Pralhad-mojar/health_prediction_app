import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = {
    "glucose": [
        90,95,100,
        150,160,170,
        100,105,110,
        90,95,100,
        160,170,180
    ],

    "haemoglobin": [
        13,14,15,
        13,14,15,
        9,10,11,
        13,14,15,
        10,11,12
    ],

    "cholesterol": [
        180,190,200,
        180,190,200,
        180,190,200,
        250,260,270,
        250,260,270
    ],

    "condition": [
        "Healthy","Healthy","Healthy",
        "Diabetes Risk","Diabetes Risk","Diabetes Risk",
        "Anemia Risk","Anemia Risk","Anemia Risk",
        "Heart Disease Risk","Heart Disease Risk","Heart Disease Risk",
        "Multiple Risks","Multiple Risks","Multiple Risks"
    ]
}

df = pd.DataFrame(data)

X = df[[
    "glucose",
    "haemoglobin",
    "cholesterol"
]]

y = df["condition"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(
    model,
    "health_model.pkl"
)

print("Model saved successfully")