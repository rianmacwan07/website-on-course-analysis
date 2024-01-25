import streamlit as st
from other_pages.enrollment import Enroll
class course_analysis:
    def button(self):
        btn = st.button("ENROLL NOW")
        if btn:
            Enroll.enrollment_form(Enroll)
    def main_course(self):
        main_course = st.sidebar.selectbox('Courses',['Main','Specialization Course','Additional Course'])

        if main_course == 'Main':
            course_analysis.Courses(course_analysis)
        elif main_course == "Specialization Course":
            course_analysis.specilization_courses(course_analysis)
        elif main_course == "Additional Course": 
            pass
    def Courses(self):
        st.title("MAIN COURSES")
        courses = st.selectbox("select an option:",["Mechanical Engineering", "Electrical Engineering", "Computer Science", "Civil Engineering", "Chemical Engineering"])
        if courses== "Mechanical Engineering":
           st.subheader('''Mechanical engineers design and analyze mechanical systems and machinery.
            Benefits of Learning: Gain expertise in the design and manufacturing of various products and machines.
        Future Scope: Opportunities in industries like automotive, aerospace, and energy systems.''')
           st.text("")
           a.button()

        
        elif courses== "Electrical Engineering":
            st.subheader('''  Electrical engineers work with electrical systems, electronics, and power generation.
             Benefits of Learning: Develop skills in electronics, power systems, and control systems.
        Future Scope: Growing demand for renewable energy and smart technologies''')
            st.text("")
            a.button()
        
        elif courses=="Computer Science":
            st.subheader('''Computer engineers design hardware and software systems, including computer networks.
             Benefits of Learning: Master programming, software development, and cybersecurity.
        Future Scope: Booming tech industry, with roles in software development, AI, and cybersecurity.''')
            st.text("")
            a.button()

        elif courses=="Civil Engineering":
            st.subheader('''Civil engineers design and maintain infrastructure such as buildings, bridges, roads, and dams.
             Benefits of Learning:Learn to create sustainable and safe structures, and contribute to urban development.
        Future Scope:High demand for infrastructure development worldwide, including transportation and environmental projects.''')
            st.text("")
            a.button()
        
        elif courses=="Chemical Engineering":
            st.subheader('''Chemical engineers work with chemical processes and materials, often in manufacturing.
             Benefits of Learning:Learn to optimize chemical processes and design sustainable solutions.
        Future Scope:Opportunities in chemical, pharmaceutical, and environmental industries.''')
            st.text("")
            a.button()
    def specilization_courses(self):
        st.title("SPECIALIZATION COURSES")
        specialize=st.selectbox("select a course:",["Thermal Engineering",
"Mechatronics and Robotics",
"Automotive Engineering",
"Aerospace Engineering",
"Manufacturing Engineering",
"Materials Engineering",
"Mechanical Design Engineering",
"Energy Engineering",
"Biomechanical Engineering",
"Nuclear Engineering",
"Marine Engineering",
"Environmental Engineering",
"Renewable Energy Engineering"])
         
        btn = st.button("ENROLL NOW")
        if btn:
            Enroll()
a=course_analysis()
a.main_course()
