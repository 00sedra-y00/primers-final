import streamlit as st
from backend import analyze_message, analyze_link

st.set_page_config(layout="wide")

# ===== THEME =====
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #e8f6ff;
}

/* Title */
h1 {
    text-align: center;
    color: #1e3a5f;
    font-size: 42px;
}

/* Text */
p {
    color: #1e3a5f;
    font-size: 16px;
}

/* Buttons */
.stButton>button {
    background-color: #60a5dd;
    color: white;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
    width: 100%;
    transition: 0.3s;
}

/* Hover */
.stButton>button:hover {
    background-color: #81c1f4;
    color: #0f172a;
}

/* Input fields */
.stTextInput>div>div>input {
    border-radius: 10px;
    border: 2px solid #60a5dd;
}

/* Container spacing */
.block-container {
    padding-top: 2rem;
}

/* Hide Streamlit UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ===== TITLE =====
st.title("Phishing Detection System")

# ===== HOME PAGE TEXT =====
st.subheader("Guidelines for Online Safety Awareness")

st.write("""
This is not an official method for identifying attacks, so always exercise caution.

Always remember: Never click on a link without verifying it first. You can hover your cursor over it to see the actual destination.

Report any social engineering attacks to your local authorities.

Regularly educate users about online safety, emphasizing the importance of avoiding suspicious links and not sharing personal information.

Stay informed and help educate those around you about the dangers of social engineering.
""")

st.write("")

# ===== BUTTONS =====
col1, col2 = st.columns(2)

with col1:
    check_message = st.button("Check Message")

with col2:
    check_link = st.button("Check Link")

# ===== MESSAGE CHECK =====
if check_message:
    st.subheader("Message Analysis")

    message = st.text_input("Enter the message")

    if message:
        level, reasons = analyze_message(message)

        st.subheader(f"Risk Level: {level}")
        st.write("Reasons:")
        for r in reasons:
            st.write("- " + r)

# ===== LINK CHECK =====
if check_link:
    st.subheader("Link Analysis")

    link = st.text_input("Enter the link")

    if link:
        level, reasons = analyze_link(link)

        st.subheader(f"Risk Level: {level}")
        st.write("Reasons:")
        for r in reasons:
            st.write("- " + r)
