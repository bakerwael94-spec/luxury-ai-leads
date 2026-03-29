## The Big Opportunity: AI Real Estate Operating System
## A full AI Co-Pilot for Real Estate Professionals.
#--------------------------------------------------------------------------
## 🎯 AI Agent for Real Estate Agents & Brokerages, Why?

# 1. They live on commission.
# 2. If you increase conversions by 10%, you change their income.
# 3. They’ll pay monthly.
#--------------------------------------------------------------------------
## Not: “AI CRM for real estate” But: AI Private Intelligence System for Luxury Brokers
#--------------------------------------------------------------------------
## Designed for agents selling:

# 1. $1M–$50M properties
# 2. High-net-worth individuals (HNWIs)
# 3. International buyers
#--------------------------------------------------------------------------
## Tech Architecture (Simple but Powerful)

# LLM (OpenAI or similar)
# Supabase (DB + auth)
# CRM integration (HubSpot / Salesforce)
# Email + WhatsApp automation / WhatsApp Business API
# Property listing API
# Stripe
# Memory database
# Behavior tracking engine
# Predictive scoring model
# Next.js frontend
#--------------------------------------------------------------------------
# 🎯 V1 Focus: Luxury Lead Intelligence + Smart Follow-Up Engine
#--------------------------------------------------------------------------
## Realistic 6-Month Roadmap

# Month 1: Market interviews
# Month 2: Manual AI prototype
# Month 3: MVP build
# Month 4: First paying brokers
# Month 5–6: Refine scoring model
# Month 6+: Raise price
#--------------------------------------------------------------------------
# Import
from openai import OpenAI
import streamlit as st # Import library as stremlit app
import pandas as pd   ## This imports Pandas library for working with tables / CSV / Excel / data .... read/write CSV
import os
#--------------------------------------------------------------------------
#Add Sidebar Title
st.sidebar.title("🏡 Luxury AI")
st.sidebar.markdown("---")
st.sidebar.caption("Lead Intelligence Platform")
#--------------------------------------------------------------------------
st.set_page_config(
    page_title="Luxury AI",
    page_icon="🏡",
    layout="wide"
)
#--------------------------------------------------------------------------
# Save leads permanently (so they don’t disappear when app refreshes)
# simple CSV database (fastest + reliable).

DB_FILE = "leads_db.csv" # create database file
#--------------------------------------------------------------------------
# 🔐 Login
# Username
# Password
# Login button

# Only after login → show app.

# Add Users
USERS = {
    "admin": "1234",
    "agent": "1234"
}

# Create Login State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login Screen
if not st.session_state.logged_in:

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()
#-------------------------------------------------------------------------- 
## Load Existing Leads on App Start
if "leads" not in st.session_state:
    if os.path.exists(DB_FILE):
        st.session_state.leads = pd.read_csv(DB_FILE).to_dict("records")
    else:
        st.session_state.leads = []

#--------------------------------------------------------------------------        
# 🔐 OpenAI client
client = OpenAI(api_key="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")  # replace with your real key

# This is for the App UI (safer)
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]) 
#--------------------------------------------------------------------------
# Head title
st.title("🏡 Luxury AI Lead Intelligence Analyzer")
st.caption("AI-powered luxury real estate lead scoring & follow-up")
#--------------------------------------------------------------------------
# 🧠 Initialize memory / store leads in memory (no database yet) / Store leads + history
if "leads" not in st.session_state:  ## st.session_state: Streamlit memory (stores values between reruns)
    st.session_state.leads = []
#--------------------------------------------------------------------------
# 📝 Inputs
name = st.text_input("Client Name")
budget = st.number_input("Budget (AED)", value=1000000)
area = st.text_input("Preferred Area")
timeline = st.selectbox("Timeline", ["1 month", "3 months", "6 months"])
message = st.text_area("Client Message")
#--------------------------------------------------------------------------
# 🚀 Analyze Button

if st.button("Analyze Lead"):

    # 🔹 Scoring
    score = 0

    if budget > 5000000:
        score += 50

    if "investment" in message.lower(): # .lower() is detecting uppercase or lowercase words
        score += 30

    if timeline == "1 month":
        score += 20

    # 🔹 Classification
    if score >= 80:
        quality = "High"
    elif score >= 50:
        quality = "Medium"
    else:
        quality = "Low"

  # Deal probability
    probability = min(95, score + 10)

    if "investment" in message.lower():
        lead_type = "Investor"
    else:
        lead_type = "End-user"

    # 📊 Display Results
    st.write(f"### Lead Score: {score}")
    st.write(f"### Quality: {quality}")
    st.write(f"### Type: {lead_type}")

    # 🤖 AI Prompt
    prompt = f"""
    You are a luxury real estate broker in Dubai.

    Client name: {name}
    Area: {area}
    Budget: {budget}
    Timeline: {timeline}
    Client type: {lead_type}
    Lead quality: {quality}

    Write a short WhatsApp-style follow-up message.
    Do NOT include a subject line.
    Make it feel natural, premium, and direct.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    ai_message = response.choices[0].message.content

    # 💬 Show AI message
    st.write("### AI Suggested Message:")
    st.success(ai_message)
#--------------------------------------------------------------------------
# 💾 Save lead
    st.session_state.leads.append({
        "name": name,
        "score": score,
        "quality": quality,
        "type": lead_type,
        "probability": probability,
        "area": area,
        "message": ai_message,
        "user": st.session_state.user ## Save User With Each Lead
        
    })
    pd.DataFrame(st.session_state.leads).to_csv(DB_FILE, index=False) # Save Leads to Database
#--------------------------------------------------------------------------
## 📊 Dashboard | 📋 Leads | 📈 Analytics

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Leads", "Analytics"]
)
# 
st.sidebar.markdown("---")
# Show User in Sidebar
st.sidebar.write(f"👤 {st.session_state.user}") 
# Add Logout Button in Sidebar
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()
# Add demo user logo
st.sidebar.markdown("---")
st.sidebar.write("👤 Demo User")
#--------------------------------------------------------------------------
# Show history (MUST be OUTSIDE button)
## add a button under each lead so the user can quickly copy the AI message. 

# Dashboard metrics
if page == "Dashboard":

    st.title("📊 Dashboard")

    if st.session_state.leads:
        total_leads = len(st.session_state.leads)
        avg_score = sum(l["score"] for l in st.session_state.leads) / total_leads
        top_prob = max(l["probability"] for l in st.session_state.leads)
        high_quality = sum(1 for l in st.session_state.leads if l["quality"] == "High")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Leads", total_leads)
        col2.metric("Avg Score", round(avg_score))
        col3.metric("Top Probability", f"{top_prob}%")
        col4.metric("High Quality", high_quality)

    st.divider()

# Lead History 
if page == "Leads":
    st.title("📋 Leads")

    # Clear history
    if st.button("Clear History"):
        st.session_state.leads = []

    # Search
    search = st.text_input("🔎 Search leads")

    # Add Area Filter UI
    areas = ["All"] + list(set(l["area"] for l in st.session_state.leads))
    selected_area = st.selectbox("📍 Filter by Area", areas)

    # Filter by quality
    filter_option = st.radio(
        "Filter by Quality",
        ["All", "High", "Medium", "Low"],
        horizontal=True
    )

    # Download CSV
    if st.session_state.leads:
        df = pd.DataFrame(st.session_state.leads)

        st.download_button(
            label="📥 Download Leads CSV",
            data=df.to_csv(index=False),
            file_name="ai_leads.csv",
            mime="text/csv"
        )

    # Apply search + filter
    # admin logs in → sees only admin leads
    # agent logs in → sees only agent leads
    #filtered_leads = [
        #lead for lead in st.session_state.leads
        #if lead["user"] == st.session_state.user
    #]
    # Admin Can See All Leads
    if st.session_state.user == "admin":
        filtered_leads = st.session_state.leads
    else:
        filtered_leads = [
            lead for lead in st.session_state.leads
            if lead["user"] == st.session_state.user
        ]




    if search: # Search filter 
        filtered_leads = [
            lead for lead in filtered_leads
            if search.lower() in lead["name"].lower()
            or search.lower() in lead["type"].lower()
        ]

    if filter_option != "All": # quality filter 
        filtered_leads = [
            lead for lead in filtered_leads
            if lead["quality"] == filter_option
        ]

    if selected_area != "All": # Area filter 
        filtered_leads = [
            lead for lead in filtered_leads
            if lead["area"] == selected_area
        ]

    # Sort by probability
    sorted_leads = sorted(
        filtered_leads,
        key=lambda x: x["probability"],
        reverse=True
    )

    # Display leads

    for i, lead in enumerate(sorted_leads):
        with st.container():

            col1, col2, col3 = st.columns([6,1,1]) # Added delete button column + Edit

            with col1:
                # highlight top leads
                if lead["probability"] >= 85: # Add Label “Top Lead”
                    st.success("🔥 Top Priority Lead")

                st.markdown(f"""
                ### 👤 {lead['name']}
                **Score:** {lead['score']}  
                **Quality:** {lead['quality']}  
                **Type:** {lead['type']}
                
                **Area:** {lead['area']}

                **Close Probability:** {lead['probability']}%
                """)

            # EDIT BUTTON
            with col2:
                if st.button("✏️", key=f"edit_{i}"):
                    st.session_state.edit_index = i
                    st.session_state.edit_lead = lead

            # DELETE BUTTON
            with col3:
                if st.button("🗑", key=f"delete_{i}"):
                    st.session_state.leads.remove(lead) # Delete logic
                    pd.DataFrame(st.session_state.leads).to_csv(DB_FILE, index=False) # Save After Delete 
                    st.rerun()

            st.progress(lead["probability"] / 100) # progress bar

            st.info(lead["message"])
            st.code(lead["message"])
            st.divider()

## Add analytics 
if page == "Analytics":
    st.title("📋 Analytics")

    if st.session_state.leads:
        df = pd.DataFrame(st.session_state.leads)

        st.write("### Leads by Quality")
        st.bar_chart(df["quality"].value_counts())

        st.write("### Probability Distribution")
        st.bar_chart(df["probability"])

#--------------------------------------------------------------------------
## Add edit form
if "edit_lead" in st.session_state:

    st.write("## ✏️ Edit Lead")

    edit_name = st.text_input("Name", st.session_state.edit_lead["name"])
    edit_type = st.text_input("Type", st.session_state.edit_lead["type"])

    if st.button("Save Changes"):
        st.session_state.leads[st.session_state.edit_index]["name"] = edit_name
        st.session_state.leads[st.session_state.edit_index]["type"] = edit_type

        del st.session_state.edit_lead
        st.rerun()
#--------------------------------------------------------------------------

# Now each lead shows:

# AI message, Copy-ready text block, Copy button, Toast notification
#--------------------------------------------------------------------------

## Your App Now Has

# ✔ AI scoring
# ✔ Lead classification
# ✔ AI message
# ✔ Lead History
# ✔ Sort by best
# ✔ Clear history
# ✔ Copy-ready messages
# ✔ AI CRM
# ✔ Lead prioritization engine
# ✔ Sales assistant
# ✔ Deal prediction tool
# ✔ Download CSV
# ✔ Probability
# ✔ Search bar
# ✔ Top lead highlight
#--------------------------------------------------------------------------


# python -m streamlit run MVP.py


