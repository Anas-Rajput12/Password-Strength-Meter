import streamlit as st
import re

# Set Page Title
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

# UI Styling
st.markdown(
    """
    <style>
    .stApp {background-color: #f7f7f7;}
    .stTextInput, .stButton button {
        border-radius: 10px;
        text-align: center;
    }
    .stSuccess, .stWarning, .stError {
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🔒 Password Strength Meter")
st.write("Enter a password to check its strength and get security tips!")

# Password Input (Masked)
password = st.text_input("Enter Password:", type="password")

# Password Strength Function
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    return score

# Strength Feedback
if password:
    score = check_password_strength(password)
    st.subheader("🛡️ Password Strength:")

    if score == 5:
        st.success("✅ **Strong Password!** (Great mix of characters, numbers, and symbols) 🔥")
    elif score >= 3:
        st.warning("⚠️ **Medium Strength** (Try adding more symbols & numbers for better security)")
    else:
        st.error("❌ **Weak Password!** (Use at least 8 characters, a mix of uppercase, numbers & symbols)")

# Security Tips
st.subheader("🔑 Password Security Tips:")
st.write("✔️ Use at least **12+ characters**")  
st.write("✔️ Mix **uppercase, lowercase, numbers & symbols**")  
st.write("✔️ Avoid **common words & personal info**")  
st.write("✔️ Use a **password manager** for strong passwords")  

# Footer
st.write("🔐 Stay safe online! Built with ❤️ using Streamlit")
