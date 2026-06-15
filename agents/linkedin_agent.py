def generate_linkedin_outreach(
    contacts,
    event_name,
    location
):

    linkedin_messages = []

    for contact in contacts:

        first_name = (
            contact.get("firstname")
            or contact.get("first_name")
            or contact.get("First Name")
            or contact.get("name")
            or "there"
        )

        message = f"""
Hi {first_name},

I wanted to personally invite you to our upcoming
{event_name} event in {location}.

We're bringing together technology leaders
to discuss AI, innovation, and enterprise strategy.

Would love to connect and share more details.

Best,
Cresco Team
"""

        linkedin_messages.append({
            "contact": contact,
            "linkedin_message": message
        })

    return linkedin_messages