def send_venue_inquiry(
    venue_name,
    venue_email,
    event_name,
    event_date,
    attendees,
    audience,
    location
):

    subject = (
        f"Venue Inquiry | {event_name} "
        f"for {attendees} Executive Guests"
    )

    email_body = f"""
Hello {venue_name} Team,

We are planning an executive event:

Event: {event_name}
Audience: {audience}
Expected Guests: {attendees}
Location: {location}
Date: {event_date}

We would like to inquire about:

- Venue availability
- Private dining/event space
- Pricing packages
- AV capabilities
- Catering options

Please share a proposal and pricing details.

Best Regards,
Cresco Team
"""


    return {
        "venue": venue_name,
        "venue_email": venue_email,
        "subject": subject,
        "email_body": email_body,
        "status": "Proposal Requested",
        "proposal_received": False,
        "quoted_price": None,
        "recommended": False
    }



