import re
from datetime import date


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def validate_dob(dob):
    return dob <= date.today()


def validate_numeric(value):
    try:
        value = float(value)
        return value >= 0
    except ValueError:
        return False


def validate_name(name):
    return bool(name.strip())


def validate_patient_data(
    fullname,
    email,
    dob,
    glucose,
    haemoglobin,
    cholesterol
):

    if not validate_name(fullname):
        return False, "Full Name is required."

    if not validate_email(email):
        return False, "Invalid Email Address."

    if not validate_dob(dob):
        return False, "Date of Birth cannot be a future date."

    if not validate_numeric(glucose):
        return False, "Glucose must be a valid number."

    if not validate_numeric(haemoglobin):
        return False, "Haemoglobin must be a valid number."

    if not validate_numeric(cholesterol):
        return False, "Cholesterol must be a valid number."

    return True, ""