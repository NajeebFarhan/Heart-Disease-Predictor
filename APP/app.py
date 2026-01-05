import streamlit as st

st.header("Heart Disease Detector")


data = {
  "Age": 0,
  "Sex": 0,
  "Chest_pain_type": 0,
  "BP": 0,
  "Cholesterol": 0,
  "Exercise_angina": 0,
  "FBS_over_120": None,
  "EKG_results": None,
  "Max_HR": None,
  "ST_depression": None,
  "Slope_of_ST": None,
  "Number_of_vessels_fluro": None,
  "Thallium": None
}

with st.container():
    col1, col2, col3 = st.columns(3)
    col1.number_input("Age")
    col2.selectbox("Sex", options={"Male": 1, "Female": 0})
    col3.selectbox("Chest pain type", options=[1, 2, 3, 4])

    col1.number_input("BP")
    col2.number_input("Cholesterol")
    col3.selectbox("Exercise angina", options=[0, 1])


    st.subheader("Optional")
    col1, col2, col3 = st.columns(3)
    col1.selectbox("FBS over 120", options={"I don't know": None, "No": 0, "Yes": 1})
    col2.number_input("EKG results")
    col3.number_input("Max HR")

    col1.number_input("ST depression")
    col2.number_input("Slope of ST")
    col3.number_input("Number of vessels fluro")
    col1.number_input("Thallium")
