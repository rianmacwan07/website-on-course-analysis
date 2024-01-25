import streamlit as st

user_credentials = {
    "user@example.com": "password123",
    "admin@example.com": "admin123"
}


st.title("Login Page")


email = st.text_input("Email")
password = st.text_input("Password", type="password")


if st.button("Login"):
    if email in user_credentials and password == user_credentials[email]:
        st.success("Logged in as: " + email)
        
    else:
        st.error("Invalid email or password")

if st.button("Forgot Password"):
    st.text("Enter your email to reset password:")
    reset_email = st.text_input("Email")
    if st.button("Reset Password"):
        if reset_email in user_credentials:
            st.success("Password reset email sent to: " + reset_email)
        else:
            st.error("Email not found")