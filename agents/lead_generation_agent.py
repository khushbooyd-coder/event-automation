import pandas as pd


def get_target_executives(
    title,
    location,
    limit=1000
):
    """
    Placeholder for future Sales Navigator integration.

    For now returns simulated executive contacts.

    Later replace with:
    - Sales Navigator
    - Evaboot
    - HubSpot
    - Apollo
    - Clay
    """

    contacts = []

    for i in range(limit):

        contacts.append({

            "firstname": f"Executive{i}",

            "lastname": "Leader",

            "email": f"executive{i}@company.com",

            "company": f"Company {i}",

            "title": title,

            "location": location
        })

    return contacts

