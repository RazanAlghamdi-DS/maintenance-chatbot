import joblib
import pandas as pd

model = joblib.load("machine_failure_model.pkl")
le = joblib.load("label_encoder.pkl")

def predict_failure(
    machine_type,
    air_temp,
    process_temp,
    rotational_speed,
    torque,
    tool_wear
):

    machine_type = le.transform([machine_type])[0]

    data = pd.DataFrame({
        "Type": [machine_type],
        "Air temperature [K]": [air_temp],
        "Process temperature [K]": [process_temp],
        "Rotational speed [rpm]": [rotational_speed],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear],
        "TWF": [0]
    })
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    return {
   "prediction": int(prediction),
   "probability": round(probability * 100, 2)
}
result = predict_failure(
    machine_type="H",
    air_temp=320,
    process_temp=340,
    rotational_speed=3000,
    torque=90,
    tool_wear=300
)

print(result)
