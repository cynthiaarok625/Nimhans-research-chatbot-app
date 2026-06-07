import mysql.connector
import streamlit as st

def get_connection():
    return mysql.connector.connect(
         host= st.secrets["db_details"]["host"],
         user=st.secrets["db_details"]["user"],
         database=st.secrets["db_details"]["database"],
         password=st.secrets["db_details"]["password"]
    )


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS research_participants (
        participant_id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        email VARCHAR(150) NOT NULL,
        phone_number VARCHAR(20),
        date_of_birth DATE,
        gender VARCHAR(20),
        medical_interest VARCHAR(100),
        medical_conditions TEXT,
        preferred_contact_method VARCHAR(20),
        consent_given BOOLEAN NOT NULL,
        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status VARCHAR(30) DEFAULT 'New'
    )
    """)
    print("Table sucessfully created")

    conn.commit()
    conn.close()


def insert_participant(
    full_name,
    email,
    phone,
    dob,
    gender,
    interest,
    conditions,
    contact_method,
    consent
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO research_participants (
        full_name,
        email,
        phone_number,
        date_of_birth,
        gender,
        medical_interest,
        medical_conditions,
        preferred_contact_method,
        consent_given
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        full_name,
        email,
        phone,
        dob,
        gender,
        interest,
        conditions,
        contact_method,
        consent
    ))

    conn.commit()
    conn.close()