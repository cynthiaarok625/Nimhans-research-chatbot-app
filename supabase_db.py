from supabase import create_client, Client
import streamlit as st

@st.cache_resource
def get_supabase():
    url = st.secrets["supabase_keys"]["url"]
    key = st.secrets["supabase_keys"]["key"]
   
    return create_client(url, key)


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
    supabase = get_supabase()

    response = (
        supabase
        .table("research_participants")
        .insert({
            "full_name": full_name,
            "email": email,
            "phone_number": phone,
            "date_of_birth": str(dob) if dob else None,
            "gender": gender,
            "medical_interest": interest,
            "medical_conditions": conditions,
            "preferred_contact_method": contact_method,
            "consent_given": consent
        })
        .execute()
    )
    print("Added Data")
    return response


def get_participants():
    supabase = get_supabase()

    response = (
        supabase
        .table("research_participants")
        .select("*")
        .execute()
    )

    return response.data

