import streamlit as st

st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI)")

# Input fields for weight and height
weight = st.number_input("Enter your weight (kg)", min_value=10, max_value=90 , value=70) 
height = st.number_input("Enter your height (m)", min_value=0.5, max_value=5.0, value=1.75)

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid weight and height values.") 