"""
Streamlit Basic Functions
"""
# Importing library
import streamlit as st
import time as t

# Adding image
st.image("streamlit.png")

# Adding title
st.title("Learning Streamlit Basics")

# Adding header
st.header("This is header in streamlit")

# Adding sub-header
st.subheader("This is the subheader in streamlit")

# Adding information
st.info("This is the information section we can use in streamlit")

# Add warning message
st.warning("This gives the warning message")

# Add error message
st.error("This shows the error message")

# Add success message
st.success("This gives the success message")

# Adding text with write function
st.write("This covers all the basic functions we use in streamlit")
st.write(range(10,50))     # Showing code in streamlit

# Adding markdown
st.markdown("# This is Markdown-1")
st.markdown("## This is Markdown-2")
st.markdown("### This is Markdown-2")
st.markdown(":+1:")       # Adding emoji

# Adding text
st.text("Streamlit is a web development framework which helps to build data science projects and does" \
" not require any prior knowledge in web development")

# Adding caption
st.caption("This provides the caption in streamlit")

# Adding latex function to display mathematical equation
st.latex(r''' a x +b x^2 + c ''')

# Streamlit Widgets
st.title("Understanding Streamlit Widgets")

# 1. Checkbox 
st.checkbox("CheckBox-1")

# 2. Button
st.button("Click Button")

# 3. Radio Button
st.radio("Select Radio Button",['RadioButton-1','RadioButton-2','None'])

# 4. Select Box 
st.selectbox('Select Option',['Option-1','Option-2','Option-3'])

# 5. Multiselect Box
st.multiselect("Select Level",['Beginner','Medium','Advanced','Pro'])

# 6. Select Slider
st.select_slider("Rating",['Bad','Good','Neutral','Outstanding'])

# 7. Slider
st.slider("Enter your marks",0,80)

# 8. Number Input
st.number_input("Pick a Number",0,10)

# 9. Text Input
st.text_input("Enter Email Address")

# 10. Date Input
st.date_input("Choose Date")

# 11. Time Input
st.time_input("Select Time")

# 12. Text Area
st.text_area("Leave your Comments")

# 13. File Uploader
st.file_uploader("Upload File")

# 14. Color Picker
st.color_picker('Pick Color')

# 15. Progress
st.write("Track your Progress")
st.progress(60)

# 16. Spinner
with st.spinner("Please Wait"):
    t.sleep(2)

# 17. Showing Balloons
st.balloons()

# 18. Sidebar
st.sidebar.title("Welcome User")
st.sidebar.text_input("Email Address")
st.sidebar.text_input("Password")
st.sidebar.checkbox("Remember Me")
st.sidebar.button("Login")
st.sidebar.radio("Occupation",['Student','Fresher','Professional'])

# Data Visualization in Streamlit
import pandas as pd
import numpy as np
# 1. Bar Chart
st.title("Data Visualization in Streamlit")
st.subheader("1. Bar Chart")
data = pd.DataFrame(np.random.rand(50,2),columns = ["x","y"])
st.bar_chart(data)

# 2. Line Chart
st.subheader("2. Line Chart")
st.line_chart(data)

# 3. Area Chart
st.subheader("3. Area Chart")
st.area_chart(data)

# 4. Map Chart
st.subheader("4. Map Chart")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Creating Table without using write function
st.header("Creating Table Using Pandas")
df = pd.DataFrame({
    "Column 1" : [10,20,30,40],
    "Column 2" : [50,60,70,80]
})

df

# Creating DataFrame
st.header("Creating DataFrame")
data = np.random.randn(10,4)
st.dataframe(data)

# Using the Pandas Styler object to highlight some elements in the interactive table.
st.header("Highlighting Elements in DataFrame")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# Creating Table
st.header("Creating Table")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.table(dataframe)

# View dataframe on checkbox selection
st.header("Selecting DataFrame")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.write(chart_data)

# View dataframe on selectbox selection
st.header("Selecting Number")
df = pd.DataFrame({
    "Column-1":[1,2,3,4],
    "Column-2":[10,20,30,40]
})

option = st.selectbox("Choose Number",df['Column-1'])
st.write("You Selected :",option)


# Adding Divider
st.header("Divider")
st.divider()

