import pandas as pd
import plotly.express as px
import streamlit as st

from agents.orchestrator import run_campaign
from services.venue_email_service import (
    send_venue_email
)


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Event Orchestrator",
    layout="wide"
)

st.title("AI Event Marketing Orchestrator")

st.write(
    "Multi-Agent Campaign Automation Dashboard"
)


# ---------------------------------------------------
# SIDEBAR CONFIGURATION
# ---------------------------------------------------

st.sidebar.title("Campaign Settings")

event_name = st.sidebar.text_input(
    "Event Name",
    "AI Governance Dinner"
)

audience = st.sidebar.text_input(
    "Audience",
    "CIOs"
)

location = st.sidebar.text_input(
    "Location",
    "Dallas"
)

event_date = st.sidebar.text_input(
    "Event Date",
    "June 15, 2026"
)


uploaded_file = st.sidebar.file_uploader(
    "Upload Contacts CSV",
    type=["csv"]
)



# ---------------------------------------------------
# RUN CAMPAIGN
# ---------------------------------------------------


contacts_data = None

if uploaded_file is not None:

    contacts_data = pd.read_csv(
        uploaded_file
    )

    st.sidebar.success(
        "CSV Uploaded Successfully"
    )



if st.button("Run Campaign"):

    results = run_campaign(
        event_name,
        audience,
        location,
        event_date,
        contacts_data
    )

    st.success("Campaign Executed Successfully")

    # ---------------------------------------------------
    # TABS
    # ---------------------------------------------------

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Overview",
        "Outreach",
        "Follow-ups",
        "Analytics",
        "Venues",
        "Venue Outreach"
    ])

    # ===================================================
    # TAB 1 → OVERVIEW
    # ===================================================

    with tab1:

        st.header("Campaign Brief")

        st.json(results["campaign_brief"])

        st.header("Campaign Metrics")

        analytics = results["analytics_report"]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Contacts",
            analytics["total_contacts"]
        )

        col2.metric(
            "Emails Sent",
            analytics["emails_sent"]
        )

        col3.metric(
            "Follow-ups",
            analytics["followups_created"]
        )

        col4.metric(
            "Delivery Rate",
            analytics["delivery_rate"]
        )

        st.header("Target Contacts")

        contacts_df = pd.DataFrame(
            results["target_contacts"]
        )

        st.dataframe(
            contacts_df,
            use_container_width=True
        )

    # ===================================================
    # TAB 2 → OUTREACH
    # ===================================================

    with tab2:

        st.header("Email Delivery Results")

        email_df = pd.DataFrame(
            results["email_results"]
        )

        st.dataframe(
            email_df,
            use_container_width=True
        )

        st.header("LinkedIn Outreach")

        for outreach in results["linkedin_outreach"]:

            st.subheader(
                outreach["contact"]["firstname"]
            )

            st.code(
                outreach["linkedin_message"]
            )

    # ===================================================
    # TAB 3 → FOLLOW-UPS
    # ===================================================

    with tab3:

        st.header("Follow-up Sequences")

        for followup in results[
            "followup_sequences"
        ]:

            st.subheader(
                followup["contact"]["firstname"]
            )

            for sequence in followup["sequence"]:

                st.write(
                    f"• {sequence['type']}"
                )

                st.write(
                    sequence["message"]
                )


    # ===================================================
    # TAB 4 → ANALYTICS
    # ===================================================

    with tab4:

        st.header("Email Delivery Analytics")

        delivery_chart = px.pie(
            email_df,
            names="status",
            title="Email Delivery Status"
        )

        st.plotly_chart(
            delivery_chart,
            use_container_width=True
        )

        st.header("Campaign Summary")

        st.json(results["analytics_report"])

    # ===================================================
    # TAB 5 → VENUES
    # ===================================================

    with tab5:

        st.header("Venue Recommendations")

        venue_df = pd.DataFrame(
            results["venue_recommendations"]
        )

        venue_df = venue_df[[
            "name",
            "address",
            "rating",
            "score",
            "estimated_cost"
        ]]

        st.dataframe(
            venue_df,
            use_container_width=True
        )

        st.subheader("AI Venue Insights")

        for venue in results["venue_recommendations"]:
            with st.container(border=True):
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.markdown(
                        f"### {venue['name']}"
                    )

                    st.write(
                        f"Type: {venue['type']}"
                    )

                    st.write(
                        f"Address: {venue['address']}"
                    )

                    st.write(
                        f"Rating: {venue['rating']}"
                    )

                    st.write(
                        f"Capacity: {venue['capacity']} attendees"
                    )

                    st.write(
                        f"Estimated Cost: {venue['estimated_cost']}"
                    )

                    st.write(
                        f"Why Recommended: {venue['reason']}"
                    )

                with col2:
                    st.metric(
                        "AI Match Score",
                        venue["score"]
                    )

                    st.link_button(
                        "View Venue",
                        venue["maps_link"]
                    )


    # ===================================================
    # TAB 6 → VENUE OUTREACH
    # ===================================================

    with tab6:

        st.header("Venue Proposal Outreach")

        for outreach in results[
            "venue_outreach_results"
        ]:
            with st.container(border=True):
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.subheader(
                        outreach["venue"]
                    )

                    st.write(
                        f"Venue Email: {outreach['venue_email']}"
                    )

                    st.write(
                        f"Subject: {outreach['subject']}"
                    )

                    st.code(
                        outreach["email_body"]
                    )

                with col2:
                    st.metric(
                        "Status",
                        outreach["status"]
                    )

                    if st.button(
                            f"Send Proposal Request to {outreach['venue']}",
                            key=outreach["venue"]
                    ):

                        send_result = send_venue_email(

                            sender_email="khushbooyd@gmail.com",

                            app_password="nsdnywyzopvbcavy",

                            receiver_email=outreach["venue_email"],

                            subject=outreach["subject"],

                            body=outreach["email_body"]
                        )

                        if send_result["status"] == "sent":

                            st.success(
                                "Proposal request sent successfully."
                            )

                        else:

                            st.error(
                                send_result["error"]
                            )

        st.header("Proposal Tracking")

        tracking_data = []

        for outreach in results[
            "venue_outreach_results"
        ]:
            tracking_data.append({

                "Venue": outreach["venue"],

                "Status": outreach["status"],

                "Proposal Received":
                    outreach["proposal_received"],

                "Quoted Price":
                    outreach["quoted_price"]
            })

        tracking_df = pd.DataFrame(
            tracking_data
        )

        st.dataframe(
            tracking_df,
            use_container_width=True
        )









