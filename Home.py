import streamlit as st
from streamlit.connections import SQLConnection


st.set_page_config(
        page_title= "multipage app",
        initial_sidebar_state="expanded",
        layout="wide",
        menu_items={
        'Get Help': 'https://www.rianmacwan04@gmail.com/help'
        }
    )

st.title("HOME")
st.markdown("-----")
st.subheader("VENTURE IS NOT AN OPTION WHEN YOU KNOW YOU ARE SELECTING THE RIGHT PATH")
st.markdown("---")
st.subheader("Over **30+** courses available at university")
st.write("Get Started now")
st.button("GET STARTED")
title_alignment= """
<style>
#GET STARTED {
  text-align: right
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Invest in your professional goals</h2>", unsafe_allow_html=True)

col1, col2, col3, col4= st.columns(4)
original = "images.png"
col1.image(original, use_column_width=True)
col1.subheader("Learn anything")
col1.write('''Explore any interest or trending topic, take prerequisites, and advance your skills''')

originals = "images(2).JPG"
col2.image(originals, use_column_width=True)
col2.subheader("Flexible learning")
col2.write("Learn at your own pace, move between multiple courses, or switch to a different course")

original_s = "1604739.png"
col3.image(original_s, use_column_width=True)
col3.subheader("Career Options")
col3.write("Many more paths will be opened to you according to your interest")

original_s1 = "downloa.png"
col4.image(original_s1, use_column_width=True)
col4.subheader("Time Consuming")
col4.write("You can select the period in which you want to learn, with multiple programs")
st.markdown("---")
st.subheader("Enroll now in any particular group of courses -")

col_1,col_2=st.columns(2)
with col_1:
    button1=st.button('SPECIALIZATION')

with col_2:
    button2=st.button('ADDITIONAL')

if button1:
    pass
if button2:
    pass
st.text("")
st.write("Look some of the famous courses available")
st.text("")

class course_show:
    def co_r(self):
        main_courses = st.selectbox('Courses',['Additional Course','Specialization Course'])
        if main_courses == "Specializations":
           st.selectbox("Mechanical Engineering","Civil Engineering","Electrical Engineering","Computer Engineering","Chemical Engineering","Aerospace Engineering","Biomedical Engineering","Environmental Engineering","Materials Engineering","Petroleum Engineering","Industrial Engineering","Biomechanical Engineering","Nuclear Engineering","Robotics Engineering","Telecommunications Engineering","Systems Engineering","Structural Engineering","Software Engineering","Renewable Energy Engineering","Marine Engineering")
        elif main_courses == "Additional":
            pass
    
    def special(self):
       course_s1=["Mechanical Engineering","Civil Engineering","Electrical Engineering","Computer Engineering","Chemical Engineering","Aerospace Engineering","Biomedical Engineering","Environmental Engineering","Materials Engineering","Petroleum Engineering","Industrial Engineering","Biomechanical Engineering","Nuclear Engineering","Robotics Engineering","Telecommunications Engineering","Systems Engineering","Structural Engineering","Software Engineering","Renewable Energy Engineering","Marine Engineering"]
       st.selectbox("See the famous speciliaztion courses Course",course_s1)
       
b=course_show()
b.co_r()