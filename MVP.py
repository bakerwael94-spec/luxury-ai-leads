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
import datetime
# Add email function
import smtplib
from email.mime.text import MIMEText
import hashlib # Import hashlib 
import random
import sqlite3
#--------------------------------------------------------------------------


st.sidebar.image("logo.png", width=150)
st.sidebar.title("Luxury AI")
st.sidebar.caption("Real Estate Lead Intelligence")

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
# Create Hash Function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
#--------------------------------------------------------------------------
# Create send function 
# This function sends a password reset email with a verification code to the user 📧🔐
def send_reset_email(to_email, code):
    msg = MIMEText(f"Your password reset code is: {code}")
    msg["Subject"] = "Password Reset Code"
    msg["From"] = "bakerwael94@gmail.com"
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("bakerwael94@gmail.com", "ctytmfqcquuncuas")
    server.send_message(msg)
    server.quit()
#--------------------------------------------------------------------------   
# Create database
# We upgrade to a real database (SQLite — simple & powerful)
# conn = connection to database 🔌
# cursor = tool to run SQL commands 🛠️
conn = sqlite3.connect("leads.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER,
    quality TEXT,
    type TEXT,
    probability INTEGER,
    area TEXT,
    message TEXT,
    user TEXT
)
""")

conn.commit() # save changes to the database permanently 💾
#--------------------------------------------------------------------------   
# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    plan TEXT,
    email TEXT
)
""")

conn.commit()
#--------------------------------------------------------------------------
# Save leads permanently (so they don’t disappear when app refreshes)
# simple CSV database (fastest + reliable).

DB_FILE = "leads_db.csv" # create database file
#--------------------------------------------------------------------------
# Reset code storage
if "reset_code" not in st.session_state:
    st.session_state.reset_code = None
#--------------------------------------------------------------------------
## Step 1 — Track App Usage

# We count: total logins, leads created and active users

if "stats" not in st.session_state:  # initialization
    st.session_state.stats = {
        "logins": 0,
        "leads_created": 0
    }
#--------------------------------------------------------------------------
# Create send function
def send_upgrade_email(user):
    try:
        msg = MIMEText(f"User '{user}' requested Pro upgrade.")
        msg["Subject"] = "Upgrade Request"
        msg["From"] = "bakerwael94@gmail.com"
        msg["To"] = "bakerwael94@gmail.com"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.ehlo()
        server.login("bakerwael94@gmail.com", "ctytmfqcquuncuas")
        server.send_message(msg)
        server.quit()

        print("EMAIL SENT")

    except Exception as e:
        print("ERROR:", e)
#--------------------------------------------------------------------------
# Add Free Limit
# Free users → 5 leads/day
# Later → Pro unlimited
FREE_LIMIT = 5
#--------------------------------------------------------------------------
# 🔐 Login
# Username
# Password
# Login button

# Only after login → show app.

# Add Users
#USERS = {
    #"admin": "1234",
    #"agent": "1234"
#}
# Add User Plans
USER_PLANS = {
    "admin": "pro",
    "agent": "free"
}
# Create Login State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# initialize trial / This code stores the start date of a trial in Streamlit session state 📅
if "trial_start" not in st.session_state:
    st.session_state.trial_start = datetime.date.today()

# Login Screen
if not st.session_state.logged_in:

    auth_mode = st.radio("Select", ["Login", "Sign Up", "Forgot Password"])

    if auth_mode == "Sign Up":

        st.subheader("Create Account")

        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")
        email = st.text_input("Email")

        if st.button("Create Account"):

            cursor.execute(
                "SELECT * FROM users WHERE username=?",
                (new_user,)
            )
            # cursor.execute(...) → search database
            # fetchone() → get first result
            # existing → store result
            existing = cursor.fetchone()

            if existing:
                st.error("User already exists")
            else:
                cursor.execute(
                    "INSERT INTO users (username, password, plan, email) VALUES (?, ?, ?, ?)",
                    (new_user, hash_password(new_pass), "free", email) # Hash Password on Signup
                )

                conn.commit()

                st.success("Account created. You can login now.")
    

    if auth_mode == "Login":

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            cursor.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, hash_password(password)) # Hash Password on Login
            )

            user = cursor.fetchone()

            if user:
                st.session_state.logged_in = True
                st.session_state.user = user[0]
                st.session_state.plan = user[2]
                st.rerun()
            else:
                st.error("Invalid username or password")
     
    if auth_mode == "Forgot Password": # Forgot Password (Email)

        st.subheader("Reset Password")

        reset_user = st.text_input("Username")

        if st.button("Send Code"):

            cursor.execute(
                "SELECT email FROM users WHERE username=?",
                (reset_user,)
            )

            user = cursor.fetchone()
            
            if user:
                code = str(random.randint(100000, 999999))
                st.session_state.reset_code = code
                st.session_state.reset_user = reset_user
                
                send_reset_email(user[0], code)
                st.success("Reset code sent to your email")
            else:
                st.error("User not found")
        # Verify code + reset
        code_input = st.text_input("Enter Code")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Confirm Reset"):

            if code_input == st.session_state.reset_code:

                cursor.execute(
                    "UPDATE users SET password=? WHERE username=?",
                    (hash_password(new_pass), st.session_state.reset_user)
                )

                conn.commit()

                st.success("Password updated")
            else:
                st.error("Invalid code")

    st.stop()
#-------------------------------------------------------------------------- 
## start as FREE
## get 7-day PRO trial
## after trial → back to FREE
####
# Day 1–7:
# Plan = TRIAL → unlimited
# After 7 days:
# Plan = FREE → limited

# Admin:
# Plan = PRO → unlimited forever
TRIAL_DAYS = 7
# Calculate Trial Days
today = datetime.date.today()
trial_days_used = (today - st.session_state.trial_start).days
# Give trial access 
if st.session_state.plan == "free" and trial_days_used < TRIAL_DAYS:
    st.session_state.plan = "trial"
#--------------------------------------------------------------------------
## Load Existing Leads on App Start
#if "leads" not in st.session_state:
    #if os.path.exists(DB_FILE):
        #st.session_state.leads = pd.read_csv(DB_FILE).to_dict("records")
    #else:
        #st.session_state.leads = []
# Load Leads From DB
#cursor.execute("SELECT * FROM leads")
#rows = cursor.fetchall()

#columns = ["id", "name", "score", "quality", "type", "probability", "area", "message", "user"]

#st.session_state.leads = [dict(zip(columns, row)) for row in rows]


def load_leads():
    cursor.execute("SELECT * FROM leads")
    rows = cursor.fetchall()

    columns = ["id","name","score","quality","type","probability","area","message","user"]

    return [dict(zip(columns, row)) for row in rows]

## Upgrade User to Pro When payment succeeds:
cursor.execute(
    "UPDATE users SET plan='pro' WHERE username=?",
    (st.session_state.user,)
)

conn.commit()
#--------------------------------------------------------------------------        
# 🔐 OpenAI client


# This is for the App UI (safer)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]) 
#--------------------------------------------------------------------------
# Head title
st.title("🏡 Luxury AI Lead Intelligence Analyzer")
st.caption("AI-powered luxury real estate lead scoring & follow-up")
#--------------------------------------------------------------------------
# 🧠 Initialize memory / store leads in memory (no database yet) / Store leads + history
if "leads" not in st.session_state:  ## st.session_state: Streamlit memory (stores values between reruns)
    st.session_state.leads = load_leads()
#--------------------------------------------------------------------------
# 📝 Inputs
name = st.text_input("Client Name")
budget = st.number_input("Budget (AED)", value=1000000)
area = st.text_input("Preferred Area")
timeline = st.selectbox("Timeline", ["1 month", "3 months", "6 months"])
message = st.text_area("Client Message")
#--------------------------------------------------------------------------
## Show Limit Warning in Main UI
if st.session_state.plan == "free":
    st.info(f"Free Plan: {FREE_LIMIT} leads limit")
#--------------------------------------------------------------------------
# 🚀 Analyze Button

if st.button("Analyze Lead"):

    # Count User Leads
    user_leads = [
        lead for lead in st.session_state.leads
        if lead["user"] == st.session_state.user   
    ]
    # Block When Limit Reached
    if st.session_state.plan == "free" and len(user_leads) >= FREE_LIMIT:
        st.warning("Free plan limit reached. Upgrade to Pro.")
        st.stop()
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

    # 💾 Save lead
    cursor.execute("""
    INSERT INTO leads (name, score, quality, type, probability, area, message, user)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        score,
        quality,
        lead_type,
        probability,
        area,
        ai_message,
        st.session_state.user ## Save User With Each Lead
    ))
    st.session_state.stats["leads_created"] += 1 ## Count Leads
    conn.commit()

    st.session_state.leads = load_leads()

    #pd.DataFrame(st.session_state.leads).to_csv(DB_FILE, index=False) # Save Leads to Database
#--------------------------------------------------------------------------


## 📊 Dashboard | 📋 Leads | 📈 Analytics

page = st.sidebar.radio(
    "Navigation",
    ["Home","Dashboard", "Leads", "Analytics", "Pricing"]
)
# 
st.sidebar.markdown("---")
# Show User in Sidebar
st.sidebar.write(f"👤 {st.session_state.user}") 
# Show Plan in Sidebar
st.sidebar.write(f"Plan: {st.session_state.plan.upper()}")
## Show Upgrade Message for Free Users
if st.session_state.plan == "free":
    st.sidebar.warning("Free Plan limited to 5 leads")

## Add Upgrade Button
#if st.session_state.plan == "free":
    #if st.sidebar.button("🚀 Upgrade to Pro"):
        #st.sidebar.info("Contact admin to upgrade your account")

#if st.sidebar.button("🚀 Upgrade to Pro"):
    #send_upgrade_email(st.session_state.user)
    #st.sidebar.success("Upgrade request sent")

PRO_LINK = "https://buy.stripe.com/test_8x24gy95I9s5duR1Qz8AE00"

#if st.sidebar.button("🚀 Upgrade to Pro"):
    #st.markdown(f"[Click here to upgrade]({PRO_LINK})")
st.sidebar.link_button("🚀 Upgrade to Pro", PRO_LINK)

# Add Logout Button in Sidebar
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()
# Add demo user logo
st.sidebar.markdown("---")
st.sidebar.write("👤 Demo User")
# Show Trial Banner
if st.session_state.plan == "trial":
    remaining = TRIAL_DAYS - trial_days_used
    st.sidebar.success(f"Trial Active: {remaining} days left")
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

        # Show Usage Dashboard
        st.subheader("📊 Usage Stats")

        col1, col2 = st.columns(2)
        col1.metric("Total Logins", st.session_state.stats["logins"])
        col2.metric("Leads Created", st.session_state.stats["leads_created"])

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
                    #st.session_state.leads.remove(lead) # Delete logic
                    #pd.DataFrame(st.session_state.leads).to_csv(DB_FILE, index=False) # Save After Delete 
                    #st.rerun()
                    cursor.execute("DELETE FROM leads WHERE id=?", (lead["id"],))
                    conn.commit()

                    st.session_state.leads = load_leads()
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

if page == "Pricing":

    st.title("💳 Pricing Plans")

    col1, col2 = st.columns(2)

    # Free Plan
    with col1:
        st.subheader("🆓 Free Plan")
        st.write("✔ Up to 5 leads")
        st.write("✔ Basic AI messages")
        st.write("✔ Dashboard access")
        st.write("❌ No priority support")

        st.button("Current Plan" if st.session_state.plan == "free" else "Select Free")

    # Pro Plan
    with col2:
        st.subheader("🚀 Pro Plan")
        st.write("✔ Unlimited leads")
        st.write("✔ Advanced AI messaging")
        st.write("✔ Full analytics")
        st.write("✔ Priority support")

        if st.session_state.plan == "pro":
            st.success("You are on Pro Plan")
        else:
            if st.button("Upgrade to Pro"):
                st.info("Contact admin to upgrade (payment integration coming soon)")

if page == "Home":

    st.title("🏡 Luxury AI")
    st.subheader("AI-Powered Real Estate Lead Intelligence")

    st.write("""
    Close more deals with AI-driven insights.
    Analyze leads, predict conversions, and generate high-end follow-ups instantly.
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("⚡ Faster Deals", "3x")
    col2.metric("🎯 Higher Conversion", "+40%")
    col3.metric("🤖 AI Automation", "24/7")

    st.divider()

    st.subheader("Why Luxury AI?")

    st.write("""
    ✔ Smart lead scoring  
    ✔ AI-generated follow-ups  
    ✔ Deal probability prediction  
    ✔ CRM dashboard  
    ✔ Multi-user platform  
    """)

    st.divider()

    if st.session_state.plan == "free":
        st.warning("Start your free trial now 🚀")

        if st.button("Get Started"):
            st.success("Go to Leads page to begin")
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


