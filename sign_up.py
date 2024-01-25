import streamlit as st
import mysql.connector

# Function to create a new user
def create_user(first_name,last_name,email,mobile_number,password,confirm_password):
    # Replace these with your MySQL database credentials
    db_connection = mysql.connector.connect(
        host="DESKTOP-JL8HNJK",
        user="root@localhost",
        password="Shelby@1256",
        database="sign_up"
    )
    
    cursor = db_connection.cursor()

    # Replace "users" with your table name
    query = f"INSERT INTO sign_up (first_name,last_name,email,mobile_number,password,confirm_password) VALUES ('{first_name}','{last_name}','{email}','{mobile_number}', '{password}','{confirm_password})"
    
    try:
        cursor.execute(query)
        db_connection.commit()
        st.success("Account created successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        db_connection.close()

def main():
    st.title("Sign Up")
    
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email (Gmail)")
    mobile_number = st.text_input("Mobile Number")
    password = st.text_input("Password", type="password",key=2)
    confirm_password = st.text_input("Confirm Password", type="password")
    
    
    if password != confirm_password:
        st.warning("Passwords do not match. Please try again.")
        
    
    if st.button("Sign Up"):
        create_user(first_name,last_name,email,mobile_number,password,confirm_password)  
        st.success("Sign up successful!")
    
if __name__ == "__main__":
    main()