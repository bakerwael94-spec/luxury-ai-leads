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
from openai import OpenAI  # ✔
import streamlit as st # Import library as stremlit app  # ✔
import pandas as pd   ## This imports Pandas library for working with tables / CSV / Excel / data .... read/write CSV  # ✔
import os  # ✔
import datetime  # ✔
# Add email function
import smtplib  # ✔
from email.mime.text import MIMEText  # ✔
import hashlib # Import hashlib   # ✔
import random  # ✔
import sqlite3  # ✔
#--------------------------------------------------------------------------
def safe_float(value):
    try:
        if isinstance(value, str):
            value = value.replace("AED", "").replace(",", "").strip()
        return float(value)
    except:
        return 0
#--------------------------------------------------------------------------
#Add Sidebar Title
st.sidebar.image("logo.png", width=150)  # ✔
st.sidebar.title("Luxury AI")  # ✔
st.sidebar.caption("Real Estate Lead Intelligence Platform")  # ✔
st.sidebar.markdown("---")  # ✔
#--------------------------------------------------------------------------
st.set_page_config(  # ✔
    page_title="Luxury AI",  # ✔
    page_icon="🏡",  # ✔
    layout="wide"  # ✔
)
#--------------------------------------------------------------------------
# Create Hash Function
def hash_password(password):  # ✔
    return hashlib.sha256(password.encode()).hexdigest()  # ✔
#--------------------------------------------------------------------------
# Create send function 
# This function sends a password reset email with a verification code to the user 📧🔐
def send_reset_email(to_email, code): # ✔
    msg = MIMEText(f"Your password reset code is: {code}")  # ✔
    msg["Subject"] = "Password Reset Code"  # ✔
    msg["From"] = "bakerwael94@gmail.com"  # ✔
    msg["To"] = to_email  # ✔

    server = smtplib.SMTP("smtp.gmail.com", 587)  # ✔
    server.starttls()  # ✔
    server.login("bakerwael94@gmail.com", "ctytmfqcquuncuas")  # ✔
    server.send_message(msg)  # ✔
    server.quit()  # ✔
#--------------------------------------------------------------------------   
# Create database
# We upgrade to a real database (SQLite — simple & powerful)
# conn = connection to database 🔌
# cursor = tool to run SQL commands 🛠️
conn = sqlite3.connect("leads.db", check_same_thread=False)  # ✔
cursor = conn.cursor()  # ✔

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
    user TEXT,
    date TEXT
)
""")
# Add pipeline/revenue columns if they do not exist
try:
    cursor.execute("ALTER TABLE leads ADD COLUMN stage TEXT")
except:
    pass

try:
    cursor.execute("ALTER TABLE leads ADD COLUMN property_value REAL")
except:
    pass

try:
    cursor.execute("ALTER TABLE leads ADD COLUMN commission_rate REAL")
except:
    pass

try:
    cursor.execute("ALTER TABLE leads ADD COLUMN expected_commission REAL")
except:
    pass


try:
    cursor.execute("ALTER TABLE leads ADD COLUMN ai_strategy TEXT")
except:
    pass


try:
    cursor.execute("ALTER TABLE leads ADD COLUMN follow_up_date TEXT")
except:
    pass


try:
    cursor.execute("ALTER TABLE leads ADD COLUMN follow_up_status TEXT")
except:
    pass


try:
    cursor.execute("ALTER TABLE leads ADD COLUMN followup_message TEXT")
except:
    pass

conn.commit() # save changes to the database permanently 💾  # ✔


st.write("Database path:", os.path.abspath("leads.db"))

cursor.execute("PRAGMA table_info(leads)")
st.write(cursor.fetchall())

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
# Add monthly usage columns if they do not exist
try:
    cursor.execute("ALTER TABLE users ADD COLUMN email TEXT")
except:
    pass

try:
    cursor.execute("ALTER TABLE users ADD COLUMN usage_month TEXT")
except:
    pass

try:
    cursor.execute("ALTER TABLE users ADD COLUMN monthly_leads INTEGER DEFAULT 0")
except:
    pass

conn.commit()  # ✔
#--------------------------------------------------------------------------  
# Save Requests (Database)
cursor.execute("""
CREATE TABLE IF NOT EXISTS demo_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    company TEXT,
    email TEXT,
    message TEXT
)
""")

conn.commit()  # ✔
#--------------------------------------------------------------------------
# Save leads permanently (so they don’t disappear when app refreshes)
# simple CSV database (fastest + reliable).

# DB_FILE = "leads_db.csv" # create database file  # ✔
#--------------------------------------------------------------------------
# Reset code storage
if "reset_code" not in st.session_state:  # ✔
    st.session_state.reset_code = None  # ✔
#--------------------------------------------------------------------------
## Step 1 — Track App Usage

# We count: total logins, leads created and active users

if "stats" not in st.session_state:  # initialization  # ✔
    st.session_state.stats = {  # ✔
        "logins": 0,  # ✔
        "leads_created": 0  # ✔
    }  # ✔
#--------------------------------------------------------------------------
# Create send function
def send_upgrade_email(user): # ✔
    try:  # ✔
        msg = MIMEText(f"User '{user}' requested Pro upgrade.")  # ✔
        msg["Subject"] = "Upgrade Request"  # ✔
        msg["From"] = "bakerwael94@gmail.com"  # ✔
        msg["To"] = "bakerwael94@gmail.com"  # ✔

        server = smtplib.SMTP("smtp.gmail.com", 587)  # ✔
        server.starttls()  # ✔
        server.ehlo()  # ✔
        server.login("bakerwael94@gmail.com", "ctytmfqcquuncuas")  # ✔
        server.send_message(msg)  # ✔
        server.quit()  # ✔

        print("EMAIL SENT")  # ✔

    except Exception as e:  # ✔
        print("ERROR:", e)  # ✔
#--------------------------------------------------------------------------
# Add Free Limit
# Free users → 5 leads/day
# Later → Pro unlimited
# FREE_LIMIT = 5
PLAN_LIMITS = {  # ✔
    "free": 5,  # ✔
    "pro": 999999,  # ✔
    "trial": 999999  # ✔
}
# Admin:
# Plan = PRO → unlimited forever
TRIAL_DAYS = 7  # ✔
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
# USER_PLANS = {
    # "admin": "pro",
    # "agent": "free"
# }

# Create Login State
if "logged_in" not in st.session_state:  # ✔
    st.session_state.logged_in = False  # ✔

# Login Screen
if not st.session_state.logged_in:  # ✔

    auth_mode = st.radio("Select", ["Login", "Sign Up", "Forgot Password"])  # ✔

    if auth_mode == "Sign Up":  # ✔

        st.subheader("Create Account")  # ✔

        new_user = st.text_input("Username")  # ✔
        new_pass = st.text_input("Password", type="password")  # ✔
        email = st.text_input("Email") # ✔

        if st.button("Create Account"):  # ✔

            cursor.execute(  # ✔
                "SELECT * FROM users WHERE username=?",  # ✔
                (new_user,)  # ✔
            )
            # cursor.execute(...) → search database
            # fetchone() → get first result
            # existing → store result
            existing = cursor.fetchone()  # ✔

            if existing:  # ✔
                st.error("User already exists")  # ✔
            else:  # ✔
                cursor.execute(  # ✔
                    "INSERT INTO users (username, password, plan, email) VALUES (?, ?, ?, ?)",  # ✔
                    (new_user, hash_password(new_pass), "free", email) # Hash Password on Signup  # ✔
                )

                conn.commit()  # ✔

                st.success("Account created. You can login now.")  # ✔
    

    if auth_mode == "Login":  # ✔

        username = st.text_input("Username")  # ✔
        password = st.text_input("Password", type="password")  # ✔

        if st.button("Login"):  # ✔

            cursor.execute(  # ✔
                "SELECT * FROM users WHERE username=? AND password=?",  # ✔
                (username, hash_password(password)) # Hash Password on Login  # ✔
            )

            user = cursor.fetchone()  # ✔

            if user:  # ✔
                st.session_state.logged_in = True  # ✔
                st.session_state.user = user[0]  # ✔
                st.session_state.plan = user[2]  # ✔
              # initialize trial / This code stores the start date of a trial in Streamlit session state 📅

                if "trial_start" not in st.session_state:  # ✔
                    st.session_state.trial_start = datetime.date.today()  # ✔
                   ## # Calculate Trial Days
                today = datetime.date.today()  # ✔
                trial_days_used = (today - st.session_state.trial_start).days  # ✔
                   ## # Give trial access
                if st.session_state.plan == "free" and trial_days_used < TRIAL_DAYS:  # ✔
                    st.session_state.plan = "trial"  # ✔

                # -------- Monthly Reset Logic --------
                current_month = today.strftime("%Y-%m")

                cursor.execute(
                    "SELECT usage_month, monthly_leads FROM users WHERE username=?",
                    (st.session_state.user,)
                )

                usage_data = cursor.fetchone()

                if usage_data:
                    usage_month, monthly_leads = usage_data

                if usage_month != current_month:
                    cursor.execute(
                        "UPDATE users SET usage_month=?, monthly_leads=? WHERE username=?",
                        (current_month, 0, st.session_state.user)
                    )
                    conn.commit()
    # ------------------------------------

                st.rerun()  # ✔
            else:  # ✔
                st.error("Invalid username or password")  # ✔
     
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

    columns = [
        "id", "name", "score", "quality", "type", "probability",
        "area", "message", "user", "stage", "property_value",
        "commission_rate", "expected_commission", "ai_strategy", "follow_up_date", "follow_up_status", "followup_message"
    ]

    return [dict(zip(columns, row)) for row in rows]

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
follow_up_date = st.date_input("Next Follow-Up Date")
#--------------------------------------------------------------------------
stage = st.selectbox(
    "Pipeline Stage",
    ["New Lead", "Contacted", "Viewing Scheduled", "Negotiation", "Closed Won", "Closed Lost"]
)

property_value = st.number_input("Property Value (AED)", min_value=0, value=8000000)

commission_rate = st.number_input("Commission Rate (%)", min_value=0.0, value=2.0)

expected_commission = property_value * commission_rate / 100
#--------------------------------------------------------------------------
# 🚀 Analyze Button

if st.button("Analyze Lead"):

    # Count User Leads
    #user_leads = [
        #lead for lead in st.session_state.leads
        #if lead["user"] == st.session_state.user   
    #]
    user_plan = st.session_state.plan
    limit = PLAN_LIMITS.get(user_plan, 5)

    cursor.execute(
        "SELECT monthly_leads FROM users WHERE username=?",
        (st.session_state.user,)
    )

    monthly_leads = cursor.fetchone()[0] or 0

    if monthly_leads >= limit:
        st.warning("Monthly limit reached. Upgrade to Pro.")
        st.stop()

    remaining = limit - monthly_leads

    if user_plan == "free":
        st.info(f"Monthly free leads remaining: {remaining}")


    # Block When Limit Reached
    #if st.session_state.plan == "free" and len(user_leads) >= FREE_LIMIT:
        #st.warning("Free plan limit reached. Upgrade to Pro.")
        #st.stop()
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

    strategy_prompt = f"""
    You are a senior luxury real estate sales strategist in Dubai.

    Lead details:
    Name: {name}
    Area: {area}
    Budget: {budget}
    Timeline: {timeline}
    Lead type: {lead_type}
    Lead quality: {quality}
    Close probability: {probability}%
    Pipeline stage: {stage}
    Property value: AED {property_value}
    Expected commission: AED {expected_commission}

    Give a short deal strategy with:
    1. Next best action
    2. Negotiation strategy
    3. When to push or wait
    4. Main risk
    """

    strategy_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": strategy_prompt}
        ]
    )

    ai_strategy = strategy_response.choices[0].message.content



    # 💬 Show AI message
    st.write("### AI Suggested Message:")
    st.success(ai_message)
  
    with st.expander("📊 View AI Strategy"):
        st.write(ai_strategy)


    # 💾 Save lead
    cursor.execute("""
    INSERT INTO leads (
        name, score, quality, type, probability, area, message, user,
        stage, property_value, commission_rate, expected_commission, ai_strategy, follow_up_date, follow_up_status
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        score,
        quality,
        lead_type,
        probability,
        area,
        ai_message,
        st.session_state.user,
        stage,
        property_value,
        commission_rate,
        expected_commission,
        ai_strategy,
        follow_up_date.strftime("%Y-%m-%d"),
        "Pending"
    ))

    st.session_state.stats["leads_created"] += 1 ## Count Leads

    # Increase monthly usage after lead is saved
    cursor.execute(
        "UPDATE users SET monthly_leads = monthly_leads + 1 WHERE username=?",
        (st.session_state.user,)
    )

    conn.commit()
    st.session_state.leads = load_leads()

    #pd.DataFrame(st.session_state.leads).to_csv(DB_FILE, index=False) # Save Leads to Database
#--------------------------------------------------------------------------


## 📊 Dashboard | 📋 Leads | 📈 Analytics

page = st.sidebar.radio(
    "Navigation",
    ["Home","Dashboard", "Leads", "Analytics", "Pricing", "Admin"]
)
# 
PRO_LINK = "https://buy.stripe.com/test_8x24gy95I9s5duR1Qz8AE00"

st.sidebar.markdown("---")
# Show User in Sidebar
st.sidebar.write(f"👤 {st.session_state.user}") 
# Show Plan in Sidebar
st.sidebar.write(f"Plan: {st.session_state.plan.upper()}")
## Sidebar (Plan + Upgrade UI)
if st.session_state.plan == "free":
    st.sidebar.warning("Free Plan limited to 5 leads")
    st.sidebar.link_button("🚀 Upgrade to Pro", PRO_LINK)

if st.session_state.plan == "trial":
    today = datetime.date.today()
    trial_days_used = (today - st.session_state.trial_start).days
    remaining = max(0, TRIAL_DAYS - trial_days_used)

    st.sidebar.success(f"Trial: {remaining} days left")
## usage display in sidebar
cursor.execute(
    "SELECT monthly_leads FROM users WHERE username=?",
    (st.session_state.user,)
)
monthly_leads = cursor.fetchone()[0] or 0

limit = PLAN_LIMITS.get(st.session_state.plan, 5)

st.sidebar.write(f"Usage: {monthly_leads}/{limit}")




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

        # Show Usage Dashboard
        st.subheader("📊 Usage Stats")

        col1, col2 = st.columns(2)
        col1.metric("Total Logins", st.session_state.stats["logins"])
        col2.metric("Leads Created", st.session_state.stats["leads_created"])

    
        st.divider()
        st.subheader("💰 Pipeline & Revenue")

        # Load leads
        leads = st.session_state.leads

        

        # Total pipeline value
        total_value = sum(safe_float(l.get("property_value")) for l in leads)

        # Expected commission
        total_commission = sum(safe_float(l.get("expected_commission")) for l in leads)

        # Closed deals
        closed_deals = [l for l in leads if l.get("stage") == "Closed Won"]
        closed_revenue = sum(safe_float(l.get("expected_commission")) for l in closed_deals)


        col1, col2, col3 = st.columns(3)

        col1.metric("Total Pipeline Value", f"AED {total_value:,.0f}")
        col2.metric("Expected Commission", f"AED {total_commission:,.0f}")
        col3.metric("Closed Revenue", f"AED {closed_revenue:,.0f}")

        st.divider()
        st.subheader("📊 Pipeline Overview")

        pipeline_stages = [
            "New Lead",
            "Contacted",
            "Viewing Scheduled",
            "Negotiation",
            "Closed Won",
            "Closed Lost"
        ]

        stage_counts = {
            stage: sum(1 for l in st.session_state.leads if l.get("stage") == stage)
            for stage in pipeline_stages
        }

        cols = st.columns(len(pipeline_stages))

        for col, stage in zip(cols, pipeline_stages):
            col.metric(stage, stage_counts[stage])

        pipeline_df = pd.DataFrame({
        "Stage": list(stage_counts.keys()),
        "Count": list(stage_counts.values())
        })

        st.bar_chart(
            pipeline_df.set_index("Stage")
        )

        st.divider()
        st.subheader("⏰ Follow-Up Reminders")

        today = datetime.date.today()

        pending_followups = []

        for lead in st.session_state.leads:
            if lead.get("follow_up_date") and lead.get("follow_up_status") != "Done":
                try:
                    follow_date = datetime.datetime.strptime(
                        str(lead["follow_up_date"]).split(" ")[0],
                        "%Y-%m-%d"
                    ).date()
                except:
                    continue  # skip bad/empty dates
    

                pending_followups.append({
                    "Name": lead["name"],
                    "Area": lead["area"],
                    "Stage": lead["stage"],
                    "Follow-Up Date": lead["follow_up_date"],
                    "Status": "Overdue" if follow_date < today else "Pending"
                })

        if pending_followups:
            df_followups = pd.DataFrame(pending_followups)
            st.dataframe(df_followups)
        else:
            st.success("No pending follow-ups 🎉")

# Lead History 
if page == "Leads":

  
    # Leads page: show only
    limit = PLAN_LIMITS.get(st.session_state.plan, 5)

    cursor.execute(
        "SELECT monthly_leads FROM users WHERE username=?",
        (st.session_state.user,)
    )

    monthly_leads = cursor.fetchone()[0] or 0
    remaining = max(0, limit - monthly_leads)

    if st.session_state.plan == "free":
        st.info(f"Free Plan: {remaining} leads remaining this month")

        st.info(f"Usage: {monthly_leads}/{limit}")
        progress = monthly_leads / limit if limit > 0 else 0
        st.progress(progress)


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

                **Stage:** {lead['stage']}

                **Property Value:** AED {safe_float(lead.get('property_value')):,.0f}  
                **Expected Commission:** AED {safe_float(lead.get('expected_commission')):,.0f}


                **Close Probability:** {lead['probability']}%

                **Next Follow-Up:** {lead['follow_up_date']}

                **Follow-Up Status:** {lead['follow_up_status']}
                """)
                today = datetime.date.today()

                if lead.get("follow_up_date") and lead.get("follow_up_status") != "Done":
                    try:
                        follow_date = datetime.datetime.strptime(
                            str(lead["follow_up_date"]).split(" ")[0],
                            "%Y-%m-%d"
                        ).date()
                        if follow_date < today:
                            st.error("⚠️ Follow-up overdue")

                    except:
                        pass  # skip bad date values
                st.progress(lead["probability"] / 100) # progress bar

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

            

            st.info(lead["message"])
            st.code(lead["message"])
            if lead.get("ai_strategy"):
                st.write("### 🧠 AI Deal Strategy")
                st.warning(lead["ai_strategy"])

            if lead.get("followup_message"):
                st.write("### 📲 Saved Follow-Up Message")
                st.success(lead["followup_message"])
                st.code(lead["followup_message"])

            if st.button("🤖 Generate Follow-Up Message", key=f"followup_{lead['id']}"):

                followup_prompt = f"""
                You are a luxury real estate broker in Dubai.

                Lead:
                Name: {lead['name']}
                Area: {lead['area']}
                Stage: {lead['stage']}
                Type: {lead['type']}
                Quality: {lead['quality']}
                Close Probability: {lead['probability']}%
                Follow-Up Date: {lead['follow_up_date']}
                Follow-Up Status: {lead['follow_up_status']}

                Write a short WhatsApp follow-up message.
                Make it premium, natural, and not pushy.
                If the follow-up is overdue, gently create urgency.
                """

                followup_response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": followup_prompt}
                    ]
                )

                followup_message = followup_response.choices[0].message.content

                cursor.execute(
                    "UPDATE leads SET followup_message=? WHERE id=?",
                    (followup_message, lead["id"])
                )

                conn.commit()

                st.session_state.leads = load_leads()

                st.write("### 📲 Follow-Up Message")
                st.success(followup_message)
                st.code(followup_message)
                  # existing button (mark done)
            if lead.get("follow_up_status") != "Done":
                if st.button("✅ Mark Follow-Up Done", key=f"done_{lead['id']}"):
                    cursor.execute(
                        "UPDATE leads SET follow_up_status=? WHERE id=?",
                        ("Done", lead["id"])
                    )
                    conn.commit()

                    st.session_state.leads = load_leads()
                    st.rerun()
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
      
    ## Add Contact Section
    st.divider()  
    st.subheader("📩 Request Demo")  

    name = st.text_input("Your Name")
    company = st.text_input("Company")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Request Demo"): 

        cursor.execute("""
        INSERT INTO demo_requests (name, company, email, message)
        VALUES (?, ?, ?, ?) 
        """, (name, company, email, message))

        conn.commit()

        st.success("Request received. We will contact you.")

    st.divider()
    st.subheader("💬 What Our Users Say")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        ⭐⭐⭐⭐⭐  
        "This tool helped me identify serious buyers instantly.  
        I closed 2 deals in one week."  
        — Ahmed, Dubai Broker
        """)

    with col2:
        st.info("""
        ⭐⭐⭐⭐⭐  
        "The AI follow-up messages are amazing.  
        Saves me hours every day."  
        — Sarah, Real Estate Agent
        """)

    st.divider()
    st.subheader("🎥 Product Demo Coming Soon")

    st.info("""
    A short demo video will be added soon showing how Luxury AI analyzes leads,
    predicts deal probability, and generates premium follow-up messages.
    """)

if page == "Admin":

    if st.session_state.user != "admin":
        st.error("Access denied")
        st.stop()

    st.title("📊 Admin Panel")
    st.subheader("Demo Requests")

    cursor.execute("SELECT * FROM demo_requests")
    rows = cursor.fetchall()

    columns = ["ID", "Name", "Company", "Email", "Message"]

    if rows:
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df)
    else:
        st.info("No demo requests yet")

    st.divider()
    st.subheader("📈 Platform Analytics")  ## Add Analytics to Admin Panel
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM leads")
    total_leads = cursor.fetchone()[0]
    cursor.execute("""
    SELECT user, COUNT(*) as total
    FROM leads
    GROUP BY user
    ORDER BY total DESC
    """)

    usage = cursor.fetchall()

    col1, col2 = st.columns(2)

    col1.metric("Total Users", total_users)
    col2.metric("Total Leads", total_leads)

    if usage:
        df = pd.DataFrame(usage, columns=["User", "Leads"])
        st.dataframe(df)



    delete_id = st.number_input("Delete request ID", step=1)

    if st.button("Delete Request"):
        cursor.execute("DELETE FROM demo_requests WHERE id=?", (delete_id,))
        conn.commit()
        st.success("Deleted")
        st.rerun()


    st.divider()
    st.subheader("👤 User Management") ## User Management (Admin can create/delete users) 👤

    new_user = st.text_input("Username") ## Create User (Admin)
    new_pass = st.text_input("Password", type="password")
    new_plan = st.selectbox("Plan", ["free", "pro"])

    if st.button("Create User"):

        cursor.execute(
            "INSERT INTO users (username, password, plan) VALUES (?, ?, ?)",
            (new_user, hash_password(new_pass), new_plan)
        )

        conn.commit()

        st.success("User created")

    cursor.execute("SELECT username, plan FROM users") ## Show Users
    users = cursor.fetchall()

    df_users = pd.DataFrame(users, columns=["Username", "Plan"])
    st.dataframe(df_users)

    delete_user = st.text_input("Delete Username")  ## Delete User

    if st.button("Delete User"):
        cursor.execute(
            "DELETE FROM users WHERE username=?",
            (delete_user,)
        )

        conn.commit()

        st.success("User deleted")
        st.rerun()

    upgrade_user = st.text_input("Upgrade Username")

    if st.button("Make Pro"):
        cursor.execute(
            "UPDATE users SET plan='pro' WHERE username=?",
            (upgrade_user,)
        )
        conn.commit()

        st.success("User upgraded to PRO")

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


