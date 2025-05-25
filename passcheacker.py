import streamlit as st
import re

st.title("Password Strength Checker")
st.write("Enter a password to check its strength.")

def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    else:
        st.warning("Password must be at least 8 characters long.")
        
    if re.search("[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.warning("Password must contain at least one uppercase and one lowercase letter.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        st.warning("Password must contain at least one digit.")
        
    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        st.warning("Password must contain at least one special character.")

    
    if score == 4:
        st.success("Password is Strong 💪")
    elif score == 3:
        st.info("Password is Not Secured. Please try to make it stronger.")
    else:
        st.error("Password is Weak. Please try to make it stronger.")

password = st.text_input("Password", type="password")

if password:  
    check_password_strength(password)