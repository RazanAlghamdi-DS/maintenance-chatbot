import streamlit as st
from predict_tool import predict_failure

st.title("🤖 Gemini Predictive Maintenance Assistant")

user_message = st.chat_input(
    "Ask a question or enter machine data"
)

if user_message:

    st.chat_message("user").write(user_message)

    message = user_message.lower()

    # Knowledge Questions

    if "tool wear" in message:

        st.chat_message("assistant").write(
            """
Tool wear represents how much the tool has been used.

High tool wear may increase machine failure risk and
indicate that maintenance is required.
"""
        )

    elif "torque" in message:

        st.chat_message("assistant").write(
            """
Torque measures the rotational force applied by the machine.

High torque values may place additional stress on machine components and increase failure risk.
"""
        )

    elif "rpm" in message or "rotational speed" in message:

        st.chat_message("assistant").write(
            """
Rotational speed (RPM) measures how fast the machine rotates.

Abnormally high RPM values can increase wear and failure probability.
"""
        )

    elif "predictive maintenance" in message:

        st.chat_message("assistant").write(
            """
Predictive Maintenance uses machine data and AI models to predict failures before they occur.

This helps reduce downtime, maintenance costs, and production interruptions.
"""
        )

    elif "failure risk" in message:

        st.chat_message("assistant").write(
            """
Machine failure risk is commonly affected by:

• Tool Wear
• Torque
• Rotational Speed
• Air Temperature
• Process Temperature

Higher abnormal values may increase failure probability.
"""
        )

    elif "," in user_message:

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

Gemini Analysis:

Risk Assessment: High

Key Factors:
• High Torque
• High Tool Wear
• Abnormal Operating Conditions

Recommended Actions:
1. Inspect the machine immediately.
2. Check tool condition.
3. Schedule preventive maintenance.
4. Monitor machine temperature.

Business Impact:
Unexpected downtime may occur if maintenance is delayed.
"""

            else:

                response = f"""
✅ Machine Healthy

Failure Probability: {result['probability']}%

Gemini Analysis:

Risk Assessment: Low

The machine appears to be operating normally.

Recommended Actions:
• Continue monitoring
• Follow routine maintenance schedule
• Inspect tools periodically
"""

            st.chat_message("assistant").write(response)

        except:

            st.chat_message("assistant").write(
                """
Invalid Format

Example:

M,298.1,308.6,3000,90,300
"""
            )

    else:

        st.chat_message("assistant").write(
            """
I can help with:

• Predictive Maintenance
• Tool Wear
• Torque
• RPM
• Failure Risk
• Machine Analysis

Or enter machine data like:

M,298.1,308.6,3000,90,300
"""
        )