import os
import time
import pandas as pd
import plotly.express as px
import streamlit as st

from agents.orchestrator import run_campaign
from services.venue_email_service import send_venue_email

# =====================================================
# PAGE CONFIG & CUSTOM STYLING (THEME & COLORS)
# =====================================================
st.set_page_config(
    page_title="AI Event Orchestrator",
    layout="wide"
)

# Custom Enterprise Dark CSS Injection
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');

    /* Global Typography & Background adjustments */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #0d1117;
    }

    /* Main Titles styling */
    h1 {
        font-weight: 700 !important;
        color: #ffffff !important;
        letter-spacing: -0.5px;
    }
    h2, h3 {
        font-weight: 600 !important;
        color: #f0f6fc !important;
    }

    /* Sidebar styling tweaks */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }

    /* Custom Badge/Tag styling for status elements */
    .agent-badge {
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-success { background-color: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .badge-active { background-color: rgba(34, 197, 94, 0.15); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.3); }

    /* Tab Design Improvements */
    button[data-baseweb="tab"] {
        font-size: 15px !important;
        font-weight: 500 !important;
        color: #8b949e !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #58a6ff !important;
        border-bottom-color: #58a6ff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Headers
st.title("🚀 Cresco AI Event Marketing Platform")
st.markdown(
    "<p style='color: #fff; font-size: 16px; margin-top: -15px;'>Enterprise AI Platform for Executive Event Marketing Automation</p>",
    unsafe_allow_html=True)
st.markdown("---")

# =====================================================
# SIDEBAR CONFIGURATION
# =====================================================
st.sidebar.title("🤖 AI Campaign Config")

with st.sidebar.container():
    event_name = st.sidebar.text_input("Event Name", "AI Governance Dinner")
    audience = st.sidebar.text_input("Audience", "CIOs")
    location = st.sidebar.text_input("Location", "Dallas")
    event_date = st.sidebar.text_input("Event Date", "June 15, 2026")

st.sidebar.markdown("---")
st.sidebar.subheader("🔌 Connected Data Sources")

# Cleaner layout for connections instead of multiple stacked boxes
col_side1, col_side2 = st.sidebar.columns(2)
with col_side1:
    st.markdown('<div class="agent-badge badge-active">🟢 Sales Nav</div>', unsafe_allow_html=True)
    st.markdown('<div class="agent-badge badge-active" style="margin-top:8px;">🟢 HubSpot</div>', unsafe_allow_html=True)
with col_side2:
    st.markdown('<div class="agent-badge badge-active">🟢 OpenAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="agent-badge badge-active" style="margin-top:8px;">🟢 Google Map</div>',
                unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.metric("Expected Executive Leads", "1000+", delta="Target Pipeline")

# =====================================================
# RUN CAMPAIGN
# =====================================================
if st.button("🚀 Run AI Orchestration Campaign", type="primary", use_container_width=True):

    progress = st.progress(0)
    status = st.empty()

    steps = [
        ("🔍 Discovering Executive Prospects...", 15),
        ("🤖 Generating Personalized Invitations...", 30),
        ("💼 Syncing HubSpot CRM...", 45),
        ("📧 Preparing Email Campaign...", 60),
        ("🏢 Finding Best Venue...", 75),
        ("🧠 Building Executive Strategy...", 90)
    ]

    for text, prg in steps:
        status.info(text)
        progress.progress(prg)
        time.sleep(0.4)

    results = run_campaign(event_name, audience, location, event_date)
    progress.progress(100)
    status.success("✅ AI Campaign Context Successfully Built!")

    # =====================================================
    # TABS LAYOUT
    # =====================================================
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "📊 Overview", "📨 Outreach", "🔁 Follow-ups", "📈 Analytics",
        "🏢 Venues", "✉️ Venue Outreach", "🧠 Executive Strategy",
        "⚙️ Workflow Engine", "🏆 Finalization"
    ])

    # =====================================================
    # TAB 1 → OVERVIEW
    # =====================================================
    with tab1:
        c1, c2 = st.columns([1, 1])
        with c1:
            with st.container(border=True):
                st.subheader("📋 Campaign Brief")
                st.json(results["campaign_brief"])
        with c2:
            with st.container(border=True):
                st.subheader("🤖 AI Agent Status")
                agent_status = pd.DataFrame({
                    "AI Agent": ["Audience Discovery", "Copywriter", "HubSpot CRM", "Venue Intelligence",
                                 "Executive Strategy", "Workflow Engine"],
                    "Status": ["✅ Completed", "✅ Completed", "✅ Connected", "✅ Completed", "✅ Generated", "✅ Completed"]
                })
                st.dataframe(agent_status, hide_index=True, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📊 Operational Metrics")
        analytics = results["analytics_report"]

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Executive Prospects", analytics["total_contacts"])
        col2.metric("Emails Sent", analytics["emails_sent"])
        col3.metric("Follow-ups", analytics["followups_created"])
        col4.metric("Delivery Rate", analytics["delivery_rate"])

        st.markdown("---")
        st.subheader("👥 Discovered Target Prospects")
        st.dataframe(pd.DataFrame(results["target_contacts"]), use_container_width=True, hide_index=True)

        st.subheader("🔄 CRM Integration Live Feedback")
        st.dataframe(pd.DataFrame(results["crm_results"]), use_container_width=True, hide_index=True)

    # =====================================================
    # TAB 2 → OUTREACH
    # =====================================================
    with tab2:
        st.subheader("📨 Core Email Deployment")
        email_df = pd.DataFrame(results["email_results"])
        if not email_df.empty:
            st.dataframe(email_df, use_container_width=True, hide_index=True)
        else:
            st.warning("Email engine currently operating in sandbox/simulation mode.")

        st.markdown("---")
        st.subheader("💬 Generated LinkedIn InMail Outreach")

        for outreach in results["linkedin_outreach"]:
            name = outreach["contact"].get("firstname", outreach["contact"].get("first_name", "Executive"))
            with st.container(border=True):
                st.markdown(f"**Target:** {name} | <span class='agent-badge badge-success'>LinkedIn InMail</span>",
                            unsafe_allow_html=True)
                st.code(outreach["linkedin_message"], language="markdown")

    # =====================================================
    # TAB 3 → FOLLOW-UPS
    # =====================================================
    with tab3:
        st.subheader("🔄 Multi-Channel Follow-up Cadence")
        for followup in results["followup_sequences"]:
            name = followup["contact"].get("firstname", followup["contact"].get("first_name", "Executive"))
            with st.container(border=True):
                st.markdown(f"### Cadence Sequence for {name}")
                for idx, sequence in enumerate(followup["sequence"]):
                    st.markdown(f"**Step {idx + 1}: {sequence['type'].upper()}**")
                    st.info(sequence["message"])

    # =====================================================
    # TAB 4 → ANALYTICS
    # =====================================================
    with tab4:
        st.subheader("📈 Campaign Performance Diagnostics")
        email_df = pd.DataFrame(results["email_results"])

        if not email_df.empty and "status" in email_df.columns:
            delivery_chart = px.pie(
                email_df, names="status",
                title="Email Delivery Breakdown",
                template="plotly_dark",
                color_discrete_sequence=px.colors.sequential.Tealgrn
            )
            st.plotly_chart(delivery_chart, use_container_width=True)
        else:
            st.info("No distribution chart metrics captured for mock email logs.")

        st.subheader("📋 Core Meta Summary")
        st.json(results["analytics_report"])

    # =====================================================
    # TAB 5 → VENUES
    # =====================================================
    with tab5:
        venues = results["venue_recommendations"]
        if venues:
            best_venue = max(venues, key=lambda x: int(x["score"].replace("%", "")))
        else:
            st.error("No compatible geographic venues found.")
            st.stop()

        # AI Recommendation Box with cleaner HTML layout
        st.markdown(f"""
        <div style="background-color: rgba(88, 166, 255, 0.1); border: 1px solid #58a6ff; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
            <h3 style="margin-top:0; color:#58a6ff;">🏆 AI Top Selection: {best_venue['name']}</h3>
            <p><b>Match Confidence:</b> {best_venue['score']} | <b>Strategic Rationale:</b> {best_venue['reason']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("🏢 Viable Options Breakdown")
        venue_df = pd.DataFrame(venues)[["name", "address", "rating", "score", "estimated_cost"]]
        venue_df.columns = ["Venue Name", "Address", "Rating", "AI Score", "Est Cost"]
        st.dataframe(venue_df, use_container_width=True, hide_index=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🧠 Granular Space Insights")
        for venue in venues:
            with st.container(border=True):
                col_v1, col_v2 = st.columns([3, 1])
                with col_v1:
                    st.markdown(f"### {venue['name']}")
                    st.markdown(
                        f"📍 **Address:** {venue['address']} | ⭐ **Rating:** {venue['rating']} | 👥 **Capacity:** {venue['capacity']} guests")
                    st.markdown(f"💰 **Estimated Cost:** {venue['estimated_cost']}")
                    st.caption(f"💡 **AI Insight:** {venue['reason']}")
                with col_v2:
                    st.metric("Match Weight", venue["score"])
                    st.link_button("View on Map ↗", venue["maps_link"], use_container_width=True)

    # =====================================================
    # TAB 6 → VENUE OUTREACH
    # =====================================================
    with tab6:
        st.subheader("📨 Automated RFP Venue Inquiries")
        for outreach in results["venue_outreach_results"]:
            v_name = outreach.get("venue", outreach.get("venue_name", "Unknown Venue"))

            with st.container(border=True):
                col_o1, col_o2 = st.columns([3, 1])
                with col_o1:
                    st.markdown(f"### {v_name}")
                    st.text(f"To: {outreach['venue_email']} | Subject: {outreach['subject']}")
                    st.code(outreach["email_body"], language="markdown")
                with col_o2:
                    st.metric("System Tracking", outreach["status"])

                    if st.button(f"Deploy RFP Email", key=f"rfp_{v_name}", type="primary", use_container_width=True):
                        send_result = send_venue_email(
                            sender_email=os.getenv("EMAIL_ADDRESS"),
                            app_password=os.getenv("EMAIL_APP_PASSWORD"),
                            receiver_email=outreach["venue_email"],
                            subject=outreach["subject"],
                            body=outreach["email_body"]
                        )
                        if send_result["status"] == "sent":
                            st.success("RFP Dispatched Successfully!")
                        else:
                            st.error(send_result["error"])

        st.markdown("---")
        st.subheader("📊 RFP Lifecycle Tracker")
        tracking_data = [{
            "Venue": o.get("venue", o.get("venue_name", "Unknown Venue")),
            "Status": o["status"],
            "Proposal Status": o["proposal_received"],
            "Quoted Budget": o["quoted_price"]
        } for o in results["venue_outreach_results"]]
        st.dataframe(pd.DataFrame(tracking_data), use_container_width=True, hide_index=True)

    # =====================================================
    # TAB 7 → EXECUTIVE STRATEGY
    # =====================================================
    with tab7:
        st.subheader("🧠 Event Executive Structural Blueprint")
        strategy = results["executive_strategy"]

        st.info(f"🎯 **Core Evening Theme:** {strategy['theme']}")

        col_s1, col_s2 = st.columns(2)
        with col_s1:
            with st.container(border=True):
                st.markdown("### 🗣️ Core Topics for Moderate Discussion")
                for topic in strategy["discussion_topics"]:
                    st.write(f"👉 {topic}")
        with col_s2:
            with st.container(border=True):
                st.markdown("### 🤝 Strategic Networking Architecture")
                for item in strategy["networking_strategy"]:
                    st.write(f"⚡ {item}")

    # =====================================================
    # TAB 8 → WORKFLOW ENGINE
    # =====================================================
    with tab8:
        st.subheader("⚙️ Agentic Engine Event Logs")
        st.dataframe(pd.DataFrame(results["workflow_status"]), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("⏳ Orchestration Chronology")
        for item in results["workflow_status"]:
            if item["status"] == "Completed":
                st.markdown(f"🟢 **{item['step']}** — *Finished*")
            elif item["status"] == "In Progress":
                st.markdown(f"🟡 **{item['step']}** — *Processing*")
            else:
                st.markdown(f"⚪ **{item['step']}** — *Queued*")

    # =====================================================
    # TAB 9 → VENUE FINALIZATION
    # =====================================================
    with tab9:
        st.subheader("🏆 Confirmed Booking Strategy Anchor")
        final = results["finalized_venue"]

        if final:
            with st.container(border=True):
                st.markdown(f"## 🏢 {final['venue_name']}")

                col_f1, col_f2 = st.columns(2)
                with col_f1:
                    st.metric("Financial Lock", final['quoted_price'])
                    st.metric("Algorithmic ROI Score", final['roi_score'])
                with col_f2:
                    st.markdown(f"**Booking Placement Status:** `{final['status'].upper()}`")
                    st.markdown(f"**Selection Context:** {final['reason']}")
        else:
            st.warning("Awaiting workflow closure execution rules before final site selection matrix locks.")