import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUBSPOT_ACCESS_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN")




BASE_URL = "https://api.hubapi.com"

headers = {
    "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}


# ---------------------------------------------------
# SEARCH CONTACT BY EMAIL
# ---------------------------------------------------

def search_contact_by_email(email):

    url = f"{BASE_URL}/crm/v3/objects/contacts/search"

    payload = {
        "filterGroups": [
            {
                "filters": [
                    {
                        "propertyName": "email",
                        "operator": "EQ",
                        "value": email
                    }
                ]
            }
        ],
        "properties": [
            "firstname",
            "lastname",
            "email"
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    data = response.json()

    results = data.get("results", [])

    if results:
        return results[0]

    return None


# ---------------------------------------------------
# CREATE CONTACT
# ---------------------------------------------------

def create_contact(
    firstname,
    lastname,
    email,
    company=None,
    job_title=None
):

    url = f"{BASE_URL}/crm/v3/objects/contacts"

    payload = {
        "properties": {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "company": company,
            "jobtitle": job_title
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    return response.json()


# ---------------------------------------------------
# UPDATE CONTACT
# ---------------------------------------------------

def update_contact(contact_id, properties):

    url = f"{BASE_URL}/crm/v3/objects/contacts/{contact_id}"

    payload = {
        "properties": properties
    }

    response = requests.patch(
        url,
        headers=headers,
        json=payload
    )

    return response.json()


# ---------------------------------------------------
# CREATE OR UPDATE CONTACT
# ---------------------------------------------------

def upsert_contact(
    firstname,
    lastname,
    email,
    company=None,
    job_title=None
):

    existing_contact = search_contact_by_email(email)

    properties = {
        "firstname": firstname,
        "lastname": lastname,
        "company": company,
        "jobtitle": job_title
    }

    # UPDATE EXISTING
    if existing_contact:

        contact_id = existing_contact["id"]

        updated = update_contact(
            contact_id,
            properties
        )

        return {
            "action": "updated",
            "data": updated
        }

    # CREATE NEW
    created = create_contact(
        firstname,
        lastname,
        email,
        company,
        job_title
    )

    return {
        "action": "created",
        "data": created
    }


# ---------------------------------------------------
# ADD EVENT TAG / STATUS
# ---------------------------------------------------

def update_event_status(
    contact_id,
    event_name,
    status
):

    properties = {
        "event_name": event_name,
        "event_rsvp_status": status
    }

    return update_contact(
        contact_id,
        properties
    )


# ---------------------------------------------------
# GET CONTACT DETAILS
# ---------------------------------------------------

def get_contact(contact_id):

    url = f"{BASE_URL}/crm/v3/objects/contacts/{contact_id}"

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()
