# Health Prediction Application

## Overview

The Health Prediction Application is a Python-based web application developed using Streamlit and SQLite. The application allows users to manage patient records and predict possible health risks based on blood test parameters.

The system performs CRUD (Create, Read, Update, Delete) operations and generates health predictions using Glucose, Haemoglobin, and Cholesterol values.

---

## Features

### Patient Management

* Add new patient records
* View all patient records
* Update existing patient records
* Delete patient records

### Data Validation

* Valid email validation
* Date of Birth cannot be a future date
* Numeric validation for blood test values
* Mandatory field validation

### Health Prediction

The application analyzes:

* Glucose
* Haemoglobin
* Cholesterol

Based on these values, the system generates health risk predictions such as:

* Healthy Range
* Diabetes Risk
* Anemia Risk
* Heart Disease Risk

### Persistent Storage

Patient records are stored in a SQLite database for permanent storage.

---

## Technologies Used

* Python
* Streamlit
* SQLite
* Pandas

---

## Project Structure

health_prediction_app/

├── app.py

├── database.py

├── predictor.py

├── validation.py

├── patients.db

├── requirements.txt

└── README.md

---

## Installation

### Clone Repository

```bash
git clone <your-github-repository-link>
cd health_prediction_app
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## Database Schema

The application stores the following information:

| Field         | Description                |
| ------------- | -------------------------- |
| ID            | Unique Patient ID          |
| Full Name     | Patient Name               |
| Date of Birth | Patient DOB                |
| Email         | Patient Email              |
| Glucose       | Blood Glucose Level        |
| Haemoglobin   | Haemoglobin Level          |
| Cholesterol   | Cholesterol Level          |
| Remarks       | Predicted Health Condition |

---

## Workflow

1. User enters patient information.
2. System validates the input.
3. Health prediction is generated.
4. Data is stored in SQLite database.
5. Users can view, update, or delete records.

---

## Future Improvements

* Integration with real healthcare APIs
* Machine Learning based prediction model
* Authentication and user management
* Dashboard and analytics
* Cloud database integration

---

## Author

Pratiksha Mojar

Final Year B.Tech CSE (Data Science)

GitHub: https://github.com/Pratiksha-Pralhad-mojar
