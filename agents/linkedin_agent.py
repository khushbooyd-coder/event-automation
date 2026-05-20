def generate_linkedin_outreach(
    contacts,
    event_name,
    location
):

    linkedin_messages = []

    for contact in contacts:

        message = f"""
Hi {contact['firstname']},

I wanted to personally invite you to our upcoming
{event_name} event in {location}.

We’re bringing together technology leaders
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

