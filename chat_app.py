import streamlit as st
from huggingface_hub import InferenceClient

TOKEN = "your token"

client = InferenceClient(
    provider="hf-inference",
    api_key=TOKEN,
)

st.title("🤖 Gemma 4 Chatbot")

prompt = st.chat_input("Ask Gemma anything...")

if prompt:

    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        model="google/gemma-2-2b-it",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300,
    )

    answer = response.choices[0].message.content

    st.chat_message("assistant").write(answer)