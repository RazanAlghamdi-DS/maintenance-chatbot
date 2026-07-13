import streamlit as st
from predict_tool import predict_failure

st.title("🔧 Predictive Maintenance Assistant")

machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature [K]",
    value=298.1
)

process_temp = st.number_input(
    "Process Temperature [K]",
    value=308.6
)

rotational_speed = st.number_input(
    "Rotational Speed [rpm]",
    value=1500
)

torque = st.number_input(
    "Torque [Nm]",
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear [min]",
    value=50
)

if st.button("Predict Failure"):

    result = predict_failure(
        machine_type,
        air_temp,
        process_temp,
        rotational_speed,
        torque,
        tool_wear
    )

    if result["prediction"] == 1:
        st.error(
            f"⚠️ Failure Risk: {result['probability']}%"
        )
    else:
        st.success(
            f"✅ Machine Healthy ({result['probability']}%)"
        )