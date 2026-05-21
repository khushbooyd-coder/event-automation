from agents.copywriter_agent import generate_invite
from agents.hubspot_agent import create_campaign_contacts
from agents.audience_agent import get_target_audience
from agents.email_agent import send_campaign_email
from agents.registration_agent import create_registration_page
from agents.followup_agent import (
    generate_followup_sequence
)
from agents.analytics_agent import (
    generate_campaign_report
)
from agents.linkedin_agent import (
    generate_linkedin_outreach
)
from agents.venue_agent import (
    recommend_venues
)
from agents.venue_outreach_agent import (
    send_venue_inquiry
)
from agents.strategy_agent import (
    generate_event_strategy
)
from agents.workflow_agent import (
    generate_campaign_workflow
)
from agents.finalization_agent import (
    finalize_best_venue
)

import random


def run_campaign(
    event_name,
    audience,
    location,
    event_date,
    uploaded_contacts=None
):

    # =====================================================
    # CAMPAIGN BRIEF
    # =====================================================

    brief = {

        "event_name": event_name,

        "audience": audience,

        "location": location,

        "event_date": event_date
    }

    # =====================================================
    # AGENT 1 → AUDIENCE INTELLIGENCE
    # =====================================================

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

    # =====================================================
    # AGENT 2 → COPYWRITER
    # =====================================================

    personalized_invites = []

    for contact in audience_contacts:

        invite_content = generate_invite(

            event_name=brief["event_name"],

            audience=brief["audience"],

            location=brief["location"],

            event_date=brief["event_date"],

            contact_name=contact.get(
                "firstname",
                "Executive"
            ),

            company=contact.get(
                "company",
                "Enterprise"
            )
        )

        personalized_invites.append({

            "contact": contact,

            "invite_content": invite_content
        })

    # =====================================================
    # AGENT 3 → REGISTRATION PAGE
    # =====================================================

    registration_page = create_registration_page(

        event_name=brief["event_name"],

        location=brief["location"],

        event_date=brief["event_date"]
    )

    # =====================================================
    # AGENT 4 → HUBSPOT CRM
    # =====================================================

    # Temporarily disabled for demo stability


    crm_results = [

        {
            "firstname": "John",
            "company": "Microsoft",
            "status": "Synced to HubSpot"
        },

        {
            "firstname": "Sarah",
            "company": "Google",
            "status": "Synced to HubSpot"
        },

        {
            "firstname": "Alex",
            "company": "IBM",
            "status": "Pending Sync"
        }
    ]


    # =====================================================
    # AGENT 5 → EMAIL OUTREACH
    # =====================================================

    # Temporarily disabled for demo stability


    email_results = [

        {
            "email": "john@company.com",
            "status": "Delivered"
        },

        {
            "email": "sarah@company.com",
            "status": "Opened"
        },

        {
            "email": "alex@company.com",
            "status": "Clicked"
        }
    ]


    # =====================================================
    # AGENT 6 → FOLLOW-UP & NURTURE
    # =====================================================

    followup_sequences = (

        generate_followup_sequence(

            contacts=audience_contacts,

            event_name=brief["event_name"],

            event_date=brief["event_date"]
        )
    )

    # =====================================================
    # AGENT 7 → ANALYTICS & REPORTING
    # =====================================================

    analytics_report = (

        generate_campaign_report(

            contacts=audience_contacts,

            email_results=email_results,

            followup_sequences=followup_sequences
        )
    )

    # =====================================================
    # AGENT 8 → LINKEDIN OUTREACH
    # =====================================================

    linkedin_outreach = (

        generate_linkedin_outreach(

            contacts=audience_contacts,

            event_name=brief["event_name"],

            location=brief["location"]
        )
    )

    # =====================================================
    # AGENT 9 → VENUE RECOMMENDATION
    # =====================================================

    venue_recommendations = (

        recommend_venues(

            city=location,

            attendees=50,

            event_type=event_name
        )
    )

    # =====================================================
    # AI AUTO VENUE DECISION ENGINE
    # =====================================================

    best_venue = max(

        venue_recommendations,

        key=lambda venue: int(
            venue["score"].replace(
                "%",
                ""
            )
        )
    )

    selected_venue = {

        "name":
            best_venue["name"],

        "score":
            best_venue["score"],

        "reason":
            best_venue["reason"],

        "address":
            best_venue["address"],

        "maps_link":
            best_venue["maps_link"],

        "estimated_cost":
            best_venue["estimated_cost"],

        "status":
            "Automatically Selected by AI",

        "email":
            best_venue.get(
                "email",
                "events@example.com"
            )
    }

    # =====================================================
    # AGENT 10 → VENUE OUTREACH
    # =====================================================

    venue_outreach_results = []

    proposal_prices = [

        "$6,500",

        "$8,000",

        "$9,500",

        "$12,000"
    ]

    for venue in [selected_venue]:

        inquiry = send_venue_inquiry(

            venue_name=venue["name"],

            venue_email=venue["email"],

            event_name=event_name,

            event_date=event_date,

            attendees=50,

            audience=audience,

            location=location
        )

        # =====================================================
        # AI PROPOSAL RESPONSE SIMULATION
        # =====================================================

        response_probability = random.randint(
            1,
            100
        )

        if response_probability > 40:

            inquiry["proposal_received"] = True

            inquiry["quoted_price"] = (

                random.choice(
                    proposal_prices
                )
            )

            inquiry["status"] = (
                "Proposal Received"
            )

        else:

            inquiry["proposal_received"] = False

            inquiry["quoted_price"] = (
                "Awaiting Response"
            )

            inquiry["status"] = (
                "Inquiry Sent"
            )

        venue_outreach_results.append(
            inquiry
        )

    # =====================================================
    # AGENT 11 → VENUE FINALIZATION ENGINE
    # =====================================================

    finalized_venue = (
        finalize_best_venue(
            venue_outreach_results
        )
    )

    # =====================================================
    # AGENT 12 → EXECUTIVE STRATEGY
    # =====================================================

    executive_strategy = (

        generate_event_strategy(

            event_name=event_name,

            audience=audience,

            location=location,

            event_date=event_date
        )
    )

    # =====================================================
    # AGENT 13 → WORKFLOW ENGINE
    # =====================================================

    workflow_status = (
        generate_campaign_workflow()
    )

    # =====================================================
    # FINAL RESPONSE
    # =====================================================

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

        "selected_venue": selected_venue,

        "venue_outreach_results": venue_outreach_results,

        "executive_strategy": executive_strategy,

        "workflow_status": workflow_status,

        "finalized_venue": finalized_venue
    }

