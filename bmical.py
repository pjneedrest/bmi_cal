import streamlit as st

st.title("BMI Calculator")

gender = st.radio("Gender", options=["Male", "Female"])

weight = st.slider("Weight (kg)", 0, 200)
height = st.slider("Height (cm)", 0, 300)

if height != 0:
    bmi = weight / ((height / 100) ** 2)
    bmi_formatted = round(bmi, 2)

    st.write(f"Your BMI is: {bmi_formatted}")

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Healthy"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    st.markdown(f"**Category:** {category}")

    image_filename = f"{category.lower()}_{gender.lower()}.png"

    st.image(image_filename, width=250)

else:
    st.warning("Please enter a non-zero height.")
