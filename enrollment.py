import streamlit as st
class Enroll:
    def enrollment_form(self):
        st.header("Enrollment Form")
            
        First_name = st.text_input("ENTER YOUR FIRST NAME")
        Last_name = st.text_input("ENTER YOUR LAST NAME")
        Father_name = st.text_input("ENTER YOUR PARENTS/GUARDIAN NAME")
        Mobile = st.text_input("ENTER MOBILE NUMBER")
        Father_mobile = st.text_input("ENTER YOUR PARENTS/GUARDIAN MOBILE NUMBER")
        email_address = st.text_input("ENTER YOUR EMAIL ADDRESS")
        department = st.text_input("NAME OF THE DEPARTMENT")
        
        month = st.selectbox("which month are you willing to start of your course",["January","February","March","April","May","June","july","August","September","October","November","December"])
        course_duration = st.slider("Select Course Duration (in weeks)", min_value=1, max_value=12, value=4)
        
        age = st.number_input("Enter Your Age", min_value=1, max_value=100, value=18)
        
        gender = st.radio("Select Your Gender", ["Male", "Female", "Other"])
        
        education_level = st.selectbox("Select Your Background", ["ST", "SC", "OBC", "GENERAL"])
        comment = st.text_input("Any request you want to add")
        
        submit_button = st.button("Enroll in Course")
        if submit_button:
                st.success("Enrollment Successful!")
                st.write(f"First name: {First_name}")
                st.write(f"Last name: {Last_name}")
                st.write(f"Parents/Guardian name: {Father_name}")
                st.write(f"mobile number: {Mobile}")
                st.write(f"Parents/Guardian: {Father_mobile}")
                st.write(f"E-Mail: {email_address}")
                st.write(f"Department: {department}")
                st.write(f"Month you are willing to start the course: {month}")
                st.write(f"Course Duration: {course_duration} weeks")
                st.write(f"Age: {age} years")
                st.write(f"Gender: {gender}")
                st.write(f"Background: {education_level}")
                st.write(f"comment: {comment}")
en=Enroll()         
en.enrollment_form()
    