# NIMHANS Research Study Discovery & Participant Registration Platform

## Overview
This project is built using Streamlit that helps users discover ongoing research studies, register as research participants, and interact with an AI-powered chatbot for
research-related queries.

### Participant Registration

Users can register their interest in research studies by submitting:

* Full Name
* Email Address
* Phone Number
* Date of Birth
* Gender
* Medical Research Interest
* Medical Conditions
* Preferred Contact Method
* Consent for Future Contact

Participant information is securely stored in a cloud database.

### AI Research Assistant

An AI-powered chatbot assists users by:

* Answering research-related questions
* Providing information about study participation
* Explaining research concepts in simple language
* Guiding users through the registration process

The chatbot is integrated using the Gemini API. and the questions related to the project is in a faq.txt file

### Cloud Database Integration

The application uses a cloud-hosted database i.e Supabase to:

* Store participant registrations
* Maintain participant records
* Enable secure and scalable data management

### Responsive User Interface

* Modern Streamlit-based interface
* Custom CSS styling
* Easy navigation and accessibility-focused design

---

## Technology Stack

### Frontend

* Streamlit
* HTML/CSS

### Backend

* Python

### Database

* Supabase (PostgreSQL)

### AI Integration

* Google Gemini API

### Deployment

* Streamlit Community Cloud

---

## Project Structure

```text
NimhansResearchProject/
│
├── NimhansLandingPage.py      # Main Streamlit application
├── chatbot.py                 # Gemini chatbot implementation
├── database.py                # Database operations
├── requirements.txt           # Project dependencies
├── .streamlit/
│   └── secrets.toml           # Environment secrets
└── README.md
```

---


## Database Schema

### research_participants

| Column                   | Type      |
| ------------------------ | --------- |
| participant_id           | BIGINT    |
| full_name                | TEXT      |
| email                    | TEXT      |
| phone_number             | TEXT      |
| date_of_birth            | DATE      |
| gender                   | TEXT      |
| medical_interest         | TEXT      |
| medical_conditions       | TEXT      |
| preferred_contact_method | TEXT      |
| consent_given            | BOOLEAN   |
| registration_date        | TIMESTAMP |
| status                   | TEXT      |


## Author

Developed as a healthcare-focused full-stack application demonstrating:

* Streamlit Development
* AI Integration
* Cloud Database Management
* Full Stack Python Development
* Healthcare Technology Solutions
