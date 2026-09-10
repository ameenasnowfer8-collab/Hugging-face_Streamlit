import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="Smart AI",
    page_icon="💬"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(120deg, #f0f9ff, #eef2ff);
}

.main-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

h1 {
    text-align: center;
    color: #2563eb;
}

.info {
    text-align: center;
    color: #64748b;
    margin-bottom: 25px;
}

.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    height: 45px;
}

.result {
    background: #f8fafc;
    border-left: 5px solid #2563eb;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------- Header ----------
st.markdown("# 💬 Smart AI")
st.markdown(
    '<div class="info">Ask your question and let AI find the answer.</div>',
    unsafe_allow_html=True
)


# ---------- API ----------
token = st.secrets["Token"]

client = InferenceClient(api_key=token)


# ---------- Question ----------
st.markdown("### 📝 Ask your question")

question = st.text_area(
    "Question",
    placeholder="Example: What is Artificial Intelligence?",
    height=130,
    label_visibility="collapsed"
)


# ---------- Generate ----------
if st.button("Generate Answer", use_container_width=True):

    if not question.strip():
        st.info("Please type a question first.")

    else:
        with st.spinner("Generating answer..."):

            result = client.chat.completions.create(
                model="google/gemma-3-4b-it",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        answer = result.choices[0].message.content

        st.markdown("### 💡 Answer")

        st.markdown(
            f'<div class="result">{answer}</div>',
            unsafe_allow_html=True
        )
