import streamlit as st
import requests

API = "http://localhost:8000"

st.title("🤖 AI Interview Coach")

menu = st.sidebar.selectbox(
    "Choose",
    ["Resume", "Questions", "Evaluate"]
)

try:

    if menu == "Resume":
        text = st.text_area("Paste Resume")

        if st.button("Analyze"):
            res = requests.post(
                f"{API}/resume",
                json={"text": text}
            )

            st.write(res.json()["result"])

    elif menu == "Questions":
        role = st.text_input("Job Role")

        if st.button("Generate"):
            res = requests.post(
                f"{API}/questions",
                json={"role": role}
            )

            st.write(res.json()["result"])

    elif menu == "Evaluate":
        ans = st.text_area("Your Answer")

        if st.button("Check"):
            res = requests.post(
                f"{API}/evaluate",
                json={"answer": ans}
            )

            st.write(res.json()["result"])

except Exception as e:
    st.error(f"Backend Error: {e}")