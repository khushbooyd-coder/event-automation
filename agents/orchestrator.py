from agents.copywriter_agent import generate_invite
from agents.hubspot_agent import create_campaign_contacts
from agents.audience_agent import get_target_audience
from agents.email_agent import send_campaign_email
from agents.registration_agent import create_registration_page
from agents.followup_agent import (
    generate_followup_sequence)
from agents.analytics_agent import ( generate_campaign_report )
from agents.linkedin_agent import ( generate_linkedin_outreach )
from agents.venue_agent import ( recommend_venues )
from agents.venue_outreach_agent import ( send_venue_inquiry )




def run_campaign(
    event_name,
    audience,
    location,
    event_date,
    uploaded_contacts=None
):



    brief = {
        "event_name": event_name,
        "audience": audience,
        "location": location,
        "event_date": event_date
    }


    # AGENT 1 → AUDIENCE INTELLIGENCE

    if uploaded_contacts is not None:

        audience_contacts = (
            uploaded_contacts.to_dict(
                orient="records"
            )
        )

    else:

        audience_contacts = (
            get_target_audience()
        )






# AGENT 2 → COPYWRITER

    personalized_invites = []

    for contact in audience_contacts:
        invite_content = generate_invite(
            event_name=brief["event_name"],
            audience=brief["audience"],
            location=brief["location"],
            event_date=brief["event_date"],
            contact_name=contact["firstname"],
            company=contact["company"]
        )

        personalized_invites.append({
            "contact": contact,
            "invite_content": invite_content
        })




# AGENT 3 → REGISTRATION PAGE
    registration_page = create_registration_page(
        event_name=brief["event_name"],
        location=brief["location"],
        event_date=brief["event_date"]
    )

    # AGENT 4 → HUBSPOT CRM
    crm_results = create_campaign_contacts(audience_contacts)

    # AGENT 5 → EMAIL OUTREACH
    email_results = send_campaign_email(
        contacts=audience_contacts,
        invite_content=personalized_invites
    )


    # AGENT 6 → FOLLOW-UP & NURTURE

    followup_sequences = (
        generate_followup_sequence(
            contacts=audience_contacts,
            event_name=brief["event_name"],
            event_date=brief["event_date"]
        )
    )


    # AGENT 7 → ANALYTICS & REPORTING

    analytics_report = (
        generate_campaign_report(
            contacts=audience_contacts,
            email_results=email_results,
            followup_sequences=followup_sequences
        )
    )


    # AGENT 8 → LINKEDIN OUTREACH

    linkedin_outreach = (
        generate_linkedin_outreach(
            contacts=audience_contacts,
            event_name=brief["event_name"],
            location=brief["location"]
        )
    )


    # AGENT → VENUE RECOMMENDATION

    venue_recommendations = (
        recommend_venues(
            city=location,
            attendees=50,
            event_type=event_name
        )
    )

    venue_outreach_results = []

    for venue in venue_recommendations:
        inquiry = send_venue_inquiry(
            venue_name=venue["name"],
            venue_email=venue["email"],
            event_name=event_name,
            event_date=event_date,
            attendees=50,
            audience=audience,
            location=location
        )

        venue_outreach_results.append(
            inquiry
        )

        # ---------------------------------------
        # AI PROPOSAL RESPONSE SIMULATION
        # ---------------------------------------

        import random

        proposal_prices = [
            "$6,500",
            "$8,000",
            "$9,500",
            "$12,000"
        ]

        response_probability = random.randint(1, 100)

        if response_probability > 40:
            inquiry["proposal_received"] = True

            inquiry["quoted_price"] = (
                random.choice(proposal_prices)
            )

            inquiry["status"] = (
                "Proposal Received"
            )


    return {
        "campaign_brief": brief,
        "target_contacts": audience_contacts,
        "registration_page": registration_page,
        "personalized_invites": personalized_invites,
        "crm_results": crm_results,
        "email_results": email_results,
        "followup_sequences": followup_sequences,
        "analytics_report": analytics_report,
        "linkedin_outreach": linkedin_outreach,
        "venue_recommendations": venue_recommendations,
        "venue_outreach_results": venue_outreach_results
    }



