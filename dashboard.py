import pandas as pd
import plotly.express as px
import streamlit as st

from agents.orchestrator import run_campaign

from services.venue_email_service import (
    send_venue_email
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(

    page_title="AI Event Orchestrator",

    layout="wide"
)

st.title(
    "AI Event Marketing Orchestrator"
)

st.write(
    "Multi-Agent Campaign Automation Dashboard"
)

# =====================================================
# SIDEBAR CONFIGURATION
# =====================================================

st.sidebar.title(
    "Campaign Settings"
)

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

# =====================================================
# FILE UPLOAD
# =====================================================

contacts_data = None

if uploaded_file is not None:

    contacts_data = pd.read_csv(
        uploaded_file
    )

    st.sidebar.success(
        "CSV Uploaded Successfully"
    )

# =====================================================
# RUN CAMPAIGN
# =====================================================

if st.button("Run Campaign"):

    with st.spinner(
        "AI agents are executing campaign workflows..."
    ):

        results = run_campaign(

            event_name,

            audience,

            location,

            event_date,

            contacts_data
        )

    st.success(
        "Campaign Executed Successfully"
    )

    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([

        "Overview",

        "Outreach",

        "Follow-ups",

        "Analytics",

        "Venues",

        "Venue Outreach",

        "Executive Strategy",

        "Workflow Engine",

        "Venue Finalization"
    ])

    # =====================================================
    # TAB 1 → OVERVIEW
    # =====================================================

    with tab1:

        st.header(
            "Campaign Brief"
        )

        st.json(
            results["campaign_brief"]
        )

        st.header(
            "Campaign Metrics"
        )

        analytics = results[
            "analytics_report"
        ]

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

        st.header(
            "Target Contacts"
        )

        contacts_df = pd.DataFrame(
            results["target_contacts"]
        )

        st.dataframe(
            contacts_df,
            use_container_width=True
        )


        st.header(
            "CRM Synchronization Status"
        )

        crm_df = pd.DataFrame(
            results["crm_results"]
        )

        st.dataframe(
            crm_df,
            use_container_width=True
        )


    # =====================================================
    # TAB 2 → OUTREACH
    # =====================================================

    with tab2:

        st.header(
            "Email Delivery Results"
        )

        email_df = pd.DataFrame(
            results["email_results"]
        )

        if not email_df.empty:

            st.dataframe(
                email_df,
                use_container_width=True
            )

        else:

            st.warning(
                "Email sending currently disabled for demo stability."
            )

        st.header(
            "LinkedIn Outreach"
        )

        for outreach in results[
            "linkedin_outreach"
        ]:

            st.subheader(
                outreach["contact"]["firstname"]
            )

            st.code(
                outreach["linkedin_message"]
            )

    # =====================================================
    # TAB 3 → FOLLOW-UPS
    # =====================================================

    with tab3:

        st.header(
            "Follow-up Sequences"
        )

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

    # =====================================================
    # TAB 4 → ANALYTICS
    # =====================================================

    with tab4:

        st.header(
            "Email Delivery Analytics"
        )

        email_df = pd.DataFrame(
            results["email_results"]
        )

        if (
            not email_df.empty
            and "status" in email_df.columns
        ):

            delivery_chart = px.pie(

                email_df,

                names="status",

                title="Email Delivery Status"
            )

            st.plotly_chart(

                delivery_chart,

                use_container_width=True
            )

        else:

            st.warning(
                "No email delivery analytics available."
            )

        st.header(
            "Campaign Summary"
        )

        st.json(
            results["analytics_report"]
        )


    # ===================================================
    # TAB 5 → VENUES
    # ===================================================

    with tab5:

        venues = results[
            "venue_recommendations"
        ]

        # ---------------------------------------
        # AI BEST VENUE SELECTION
        # ---------------------------------------

        best_venue = max(

            venues,

            key=lambda x: int(
                x["score"].replace(
                    "%",
                    ""
                )
            )
        )

        # ---------------------------------------
        # SINGLE AI RECOMMENDATION BOX
        # ---------------------------------------

        st.success(
            f"""
    🏆 AI Recommended Venue

    Venue:
    {best_venue['name']}

    Score:
    {best_venue['score']}

    Reason:
    {best_venue['reason']}
    """
        )

        # ---------------------------------------
        # VENUE TABLE
        # ---------------------------------------

        st.header(
            "Venue Recommendations"
        )

        venue_df = pd.DataFrame(
            venues
        )

        # CLEAN TABLE COLUMNS

        venue_df = venue_df[[

            "name",

            "address",

            "rating",

            "score",

            "estimated_cost"
        ]]

        # CLEAN COLUMN NAMES

        venue_df.columns = [

            "Venue Name",

            "Address",

            "Rating",

            "AI Score",

            "Estimated Cost"
        ]

        st.dataframe(

            venue_df,

            use_container_width=True,

            hide_index=True
        )

        # ---------------------------------------
        # DETAILED VENUE CARDS
        # ---------------------------------------

        st.subheader(
            "AI Venue Insights"
        )

        for venue in venues:
            with st.container(border=True):
                col1, col2 = st.columns([4, 1])

                # -----------------------------------
                # LEFT SIDE
                # -----------------------------------

                with col1:
                    st.markdown(
                        f"### {venue['name']}"
                    )

                    st.write(
                        f"📍 Address: {venue['address']}"
                    )

                    st.write(
                        f"⭐ Rating: {venue['rating']}"
                    )

                    st.write(
                        f"👥 Capacity: {venue['capacity']} attendees"
                    )

                    st.write(
                        f"💰 Estimated Cost: {venue['estimated_cost']}"
                    )

                    st.write(
                        f"🧠 AI Insight: {venue['reason']}"
                    )

                # -----------------------------------
                # RIGHT SIDE
                # -----------------------------------

                with col2:
                    st.metric(
                        "AI Score",
                        venue["score"]
                    )

                    st.link_button(
                        "Open Map",
                        venue["maps_link"]
                    )




# =====================================================
    # TAB 6 → VENUE OUTREACH
    # =====================================================

    with tab6:

        st.header(
            "Venue Proposal Outreach"
        )

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

                            sender_email="your_email@gmail.com",

                            app_password="your_app_password",

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

        st.header(
            "Proposal Tracking"
        )

        tracking_data = []

        for outreach in results[
            "venue_outreach_results"
        ]:

            tracking_data.append({

                "Venue":
                    outreach["venue"],

                "Status":
                    outreach["status"],

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

    # =====================================================
    # TAB 7 → EXECUTIVE STRATEGY
    # =====================================================

    with tab7:

        st.header(
            "AI Executive Event Strategy"
        )

        strategy = results[
            "executive_strategy"
        ]

        st.success(
            strategy["theme"]
        )

        st.subheader(
            "Discussion Topics"
        )

        for topic in strategy[
            "discussion_topics"
        ]:

            st.write(f"• {topic}")

        st.subheader(
            "Networking Strategy"
        )

        for item in strategy[
            "networking_strategy"
        ]:

            st.write(f"• {item}")

    # =====================================================
    # TAB 8 → WORKFLOW ENGINE
    # =====================================================

    with tab8:

        st.header(
            "AI Campaign Workflow Engine"
        )

        workflow_df = pd.DataFrame(
            results["workflow_status"]
        )

        st.dataframe(
            workflow_df,
            use_container_width=True
        )

        st.subheader(
            "AI Execution Timeline"
        )

        for item in results[
            "workflow_status"
        ]:

            status = item["status"]

            if status == "Completed":

                st.success(
                    f"✓ {item['step']}"
                )

            elif status == "In Progress":

                st.warning(
                    f"⏳ {item['step']}"
                )

            else:

                st.info(
                    f"• {item['step']}"
                )

    # =====================================================
    # TAB 9 → VENUE FINALIZATION
    # =====================================================

    with tab9:

        st.subheader(
            "AI Venue Finalization Engine"
        )

        final = results[
            "finalized_venue"
        ]

        if final:

            st.success(
                f"""
🏆 FINAL VENUE SELECTED

Venue:
{final['venue_name']}

Quoted Price:
{final['quoted_price']}

ROI Score:
{final['roi_score']}

Reason:
{final['reason']}
"""
            )

            st.metric(
                "Final Booking Status",
                final["status"]
            )

        else:

            st.warning(
                "No finalized venue yet."
            )

