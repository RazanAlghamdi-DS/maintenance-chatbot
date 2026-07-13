import streamlit as st
from predict_tool import predict_failure

st.title("🤖 Gemma Predictive Maintenance Assistant")

user_message = st.chat_input(
    "Example: M,298.1,308.6,3000,90,300"
)

if user_message:

    st.chat_message("user").write(user_message)

    try:

        data = user_message.split(",")

        result = predict_failure(
            machine_type=data[0],
            air_temp=float(data[1]),
            process_temp=float(data[2]),
            rotational_speed=float(data[3]),
            torque=float(data[4]),
            tool_wear=float(data[5])
        )

        if result["prediction"] == 1:

            response = f"""
⚠️ Failure Risk: {result['probability']}%

Gemma Analysis:

The machine shows a high risk of failure.
Tool wear and operating conditions indicate maintenance should be scheduled immediately.
"""

        else:

            response = f"""
✅ Machine Healthy

Failure Probability: {result['probability']}%

Gemma Analysis:

The machine is currently operating within a normal range.
Continue monitoring and perform routine maintenance.
"""

        st.chat_message("assistant").write(response)

    except Exception as e:

        st.chat_message("assistant").write(
            "Invalid format. Example: M,298.1,308.6,3000,90,300"
        )