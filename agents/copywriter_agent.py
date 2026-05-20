from services.openai_service import (
    generate_ai_invite
)


def generate_invite(
    event_name,
    audience,
    location,
    event_date,
    contact_name=None,
    company=None,
    job_title="Executive"
):

    subject = (
        f"Exclusive Invitation for {audience} | "
        f"{event_name} in {location}"
    )

    try:

        ai_email = generate_ai_invite(
            contact_name=contact_name,
            company=company,
            job_title=job_title,
            event_name=event_name,
            location=location,
            event_date=event_date
        )

    except Exception:

        greeting = (
            f"Hello {contact_name}"
        )

        ai_email = f"""
{greeting},

You are invited to our exclusive event:

Event: {event_name}
Location: {location}
Date: {event_date}

We believe leaders at {company}
would find this discussion valuable.

This event is specially designed
for {audience} to discuss
innovation and AI strategy.

Best Regards,
Cresco Team
"""

    linkedin_post = f"""
Excited to host {event_name}
in {location} on {event_date}.

#AI #Leadership #Cresco
"""

    cta = "Reserve Your Seat"

    return {
        "subject": subject,
        "email_body": ai_email,
        "linkedin_post": linkedin_post,
        "cta": cta
    }

