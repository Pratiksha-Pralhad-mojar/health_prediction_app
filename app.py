import streamlit as st
import pandas as pd
from datetime import date

from database import (
    create_table,
    add_patient,
    get_patients,
    update_patient,
    delete_patient
)

from predictor import predict_health
from validation import validate_patient_data


create_table()

st.set_page_config(
    page_title="Health Prediction Application",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Health Prediction Application")
st.markdown("Manage patient records and predict health risks using Machine Learning.")

menu = [
    "Create Patient",
    "View Patients",
    "Update Patient",
    "Delete Patient"
]

choice = st.sidebar.selectbox("Menu", menu)

# CREATE PATIENT
if choice == "Create Patient":

    st.header("➕ Add New Patient")

    fullname = st.text_input("Full Name")

    dob = st.date_input(
        "Date of Birth",
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

    email = st.text_input("Email Address")

    glucose = st.number_input(
        "Glucose",
        min_value=0.0,
        step=1.0
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        min_value=0.0,
        step=0.1
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0.0,
        step=1.0
    )

    if st.button("Save Patient"):

        valid, message = validate_patient_data(
            fullname,
            email,
            dob,
            glucose,
            haemoglobin,
            cholesterol
        )

        if not valid:
            st.error(message)

        else:

            remarks = predict_health(
                glucose,
                haemoglobin,
                cholesterol
            )

            add_patient(
                fullname,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success("Patient Added Successfully")
            st.info(f"Prediction: {remarks}")

# VIEW PATIENTS
elif choice == "View Patients":

    st.header("📋 Patient Records")

    patients = get_patients()

    if patients:

        df = pd.DataFrame(
            patients,
            columns=[
                "ID",
                "Full Name",
                "DOB",
                "Email",
                "Glucose",
                "Haemoglobin",
                "Cholesterol",
                "Remarks"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("No patient records found.")

# UPDATE PATIENT
elif choice == "Update Patient":

    st.header("✏️ Update Patient")

    patients = get_patients()

    if patients:

        patient_ids = [patient[0] for patient in patients]

        selected_id = st.selectbox(
            "Select Patient ID",
            patient_ids
        )

        selected_patient = next(
            patient
            for patient in patients
            if patient[0] == selected_id
        )

        fullname = st.text_input(
            "Full Name",
            value=selected_patient[1]
        )

        email = st.text_input(
            "Email",
            value=selected_patient[3]
        )

        glucose = st.number_input(
            "Glucose",
            value=float(selected_patient[4])
        )

        haemoglobin = st.number_input(
            "Haemoglobin",
            value=float(selected_patient[5])
        )

        cholesterol = st.number_input(
            "Cholesterol",
            value=float(selected_patient[6])
        )

        if st.button("Update Patient"):

            remarks = predict_health(
                glucose,
                haemoglobin,
                cholesterol
            )

            update_patient(
                selected_id,
                fullname,
                selected_patient[2],  # Existing DOB
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success("Patient Updated Successfully")
            st.info(f"New Prediction: {remarks}")

    else:
        st.warning("No patient records available.")

# DELETE PATIENT
elif choice == "Delete Patient":

    st.header("🗑 Delete Patient")

    patients = get_patients()

    if patients:

        patient_ids = [patient[0] for patient in patients]

        selected_id = st.selectbox(
            "Select Patient ID",
            patient_ids
        )

        if st.button("Delete Patient"):

            delete_patient(selected_id)

            st.success(
                f"Patient ID {selected_id} deleted successfully."
            )

    else:
        st.warning("No patient records available.")