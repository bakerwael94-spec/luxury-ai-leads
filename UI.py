
## You now have:

# AI message generator ✅
# Lead scoring ✅
# Lead classification ✅
# Lead history memory ✅
# Working UI ✅

## That’s already a mini CRM with AI assistant. ##

USERS = {  ## Add Users
    "admin": "1234",
    "agent": "1234"
}


## Save leads permanently (so they don’t disappear when app refreshes)

## We’ll use a simple CSV database (fastest + reliable).

import pandas as pd 
import os

DB_FILE = "leads_db.csv" ## Create Database File

import streamlit as st
from openai import OpenAI


if "logged_in" not in st.session_state: ## Create Login State
    st.session_state.logged_in = False

## Load Existing Leads on App Start

if "leads" not in st.session_state:
    if os.path.exists(DB_FILE):
        st.session_state.leads = pd.read_csv(DB_FILE).to_dict("records")
    else:
        st.session_state.leads = []



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



st.set_page_config(
    page_title="Luxury AI",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Luxury AI Lead Intelligence")
st.caption("AI-powered real estate lead scoring & follow-up")
st.markdown("### AI-powered luxury real estate lead scoring")

#st.sidebar.title("🏡 Luxury AI")
#st.sidebar.caption("Lead Intelligence Platform")

st.sidebar.title("🏡 Luxury AI")
st.sidebar.markdown("---")
st.sidebar.caption("Lead Intelligence Platform")

st.sidebar.markdown("---")  ## Add Logout Button in Sidebar

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()



st.sidebar.write(f"👤 {st.session_state.user}")


# 🔐 OpenAI client
client = OpenAI(api_key="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")  # replace with your real key



# 🧠 Initialize memory
if "leads" not in st.session_state:
    st.session_state.leads = []

st.title("🏡 Luxury AI Lead Analyzer")

# 📝 Inputs
name = st.text_input("Client Name")
budget = st.number_input("Budget (AED)", value=1000000)
area = st.text_input("Preferred Area")
timeline = st.selectbox("Timeline", ["1 month", "3 months", "6 months"])
message = st.text_area("Client Message")

# 🚀 Analyze Button
if st.button("Analyze Lead"):

    # 🔹 Scoring
    score = 0

    if budget > 5000000:
        score += 50

    if "investment" in message.lower():
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
    st.session_state.leads.append({
        "name": name,
        "score": score,
        "quality": quality,
        "type": lead_type,
        "probability": probability,
        "area": area,
        "message": ai_message,
        "user": st.session_state.user
        
    })

pd.DataFrame(st.session_state.leads).to_csv(DB_FILE, index=False) # Save Leads to Database

# ✅ Show history (MUST be OUTSIDE button)

#st.write("## 📋 Lead History")

#for lead in st.session_state.leads:
    #st.write(lead)


#########################################################3

## convert it into clean cards like a real product

    ### python -m streamlit run UI.py

import pandas as pd

#tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📋 Leads", "📈 Analytics"]) ## Create Tabs

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Leads", "Analytics"]
)

st.sidebar.markdown("---")
st.sidebar.write("👤 Demo User")

#with tab2:  ## Move Lead History Into Tab2

if page == "Leads":
    st.title("📋 Leads")

#st.write("## 📋 Lead History")

if st.button("Clear History"):
    st.session_state.leads = []  ## Clear History" Button

# Dashboard metrics
#if st.session_state.leads:   ## Add Stats Section

    #total_leads = len(st.session_state.leads)
    #avg_score = sum(l["score"] for l in st.session_state.leads) / total_leads
    #top_prob = max(l["probability"] for l in st.session_state.leads)
    #high_quality = sum(1 for l in st.session_state.leads if l["quality"] == "High")

    #col1, col2, col3, col4 = st.columns(4)

    #col1.metric("Total Leads", total_leads)
    #col2.metric("Avg Score", round(avg_score))
    #col3.metric("Top Probability", f"{top_prob}%")
    #col4.metric("High Quality", high_quality)
    #st.divider()

#with tab1:  ## Move Dashboard Metrics Into Tab1

    #if st.session_state.leads:

        #total_leads = len(st.session_state.leads)
        #avg_score = sum(l["score"] for l in st.session_state.leads) / total_leads
        #top_prob = max(l["probability"] for l in st.session_state.leads)
        #high_quality = sum(1 for l in st.session_state.leads if l["quality"] == "High")

        #col1, col2, col3, col4 = st.columns(4)

        #col1.metric("Total Leads", total_leads)
        #col2.metric("Avg Score", round(avg_score))
        #col3.metric("Top Probability", f"{top_prob}%")
        #col4.metric("High Quality", high_quality)

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

## Add Analytics (Tab3)
#with tab3:

    #if st.session_state.leads:
        #df = pd.DataFrame(st.session_state.leads)

        #st.write("### Leads by Quality")
        #st.bar_chart(df["quality"].value_counts())

        #st.write("### Probability Distribution")
        #st.bar_chart(df["probability"])

if page == "Analytics":

    st.title("📈 Analytics")

    if st.session_state.leads:
        df = pd.DataFrame(st.session_state.leads)

        st.write("### Leads by Quality")
        st.bar_chart(df["quality"].value_counts())

        st.write("### Probability Distribution")
        st.bar_chart(df["probability"])


search = st.text_input("🔎 Search leads")  ## Add Search Box

################### Add Area Filter UI

areas = ["All"] + list(set(l["area"] for l in st.session_state.leads))  

selected_area = st.selectbox("📍 Filter by Area", areas)

####################

filter_option = st.radio(   ## Add Filter Buttons
    "Filter by Quality",
    ["All", "High", "Medium", "Low"],
    horizontal=True
)


# download button
if st.session_state.leads:
    df = pd.DataFrame(st.session_state.leads)

    st.download_button(
        label="📥 Download Leads CSV",
        data=df.to_csv(index=False),
        file_name="ai_leads.csv",
        mime="text/csv"
    )



# 🔥 sort leads by highest probability

#sorted_leads = sorted(
   # st.session_state.leads,
  #  key=lambda x: x["probability"],
   # reverse=True
#)

# Apply search + filter

#filtered_leads = st.session_state.leads

filtered_leads = [
    lead for lead in st.session_state.leads
    if lead["user"] == st.session_state.user
]

## If you want admin to see everything:
#if st.session_state.user == "admin":
    #filtered_leads = st.session_state.leads
#else:
   # filtered_leads = [
        #lead for lead in st.session_state.leads
       # if lead["user"] == st.session_state.user
   # ]


# search filter
if search:
    filtered_leads = [
        lead for lead in filtered_leads
        if search.lower() in lead["name"].lower()
        or search.lower() in lead["type"].lower()
    ]

# quality filter
if filter_option != "All":
    filtered_leads = [
        lead for lead in filtered_leads
        if lead["quality"] == filter_option
    ]

#filtered_leads = st.session_state.leads

#if search:
   # filtered_leads = [
        #lead for lead in filtered_leads
        #if search.lower() in lead["name"].lower()
       # or search.lower() in lead["type"].lower()
    #]

# area filter
if selected_area != "All":
    filtered_leads = [
        lead for lead in filtered_leads
        if lead["area"] == selected_area
    ]

sorted_leads = sorted(  ## Sort by probability

    filtered_leads,
    key=lambda x: x["probability"],
    reverse=True
)

#########################################################
## # Display leads

#for lead in sorted_leads:
    #with st.container():

        # highlight top leads
        #if lead["probability"] >= 85:
            #st.success("🔥 Top Priority Lead")

        #st.markdown(f"""
        ### 👤 {lead['name']}
        #**Score:** {lead['score']}  
        #**Quality:** {lead['quality']}  
        #**Type:** {lead['type']}

        #**Close Probability:** {lead['probability']}%
        #""")

        #st.progress(lead["probability"] / 100) ## visual probability bar
        
        #st.info(lead["message"])
        #st.code(lead["message"])
        #st.divider()
        


################################################################################33


#for i, lead in enumerate(sorted_leads):
    #with st.container():

        #col1, col2 = st.columns([6,1])

        #with col1:
            # highlight top leads
            #if lead["probability"] >= 85:
                #st.success("🔥 Top Priority Lead")

            #st.markdown(f"""
            ### 👤 {lead['name']}
            #**Score:** {lead['score']}  
            #**Quality:** {lead['quality']}  
            #**Type:** {lead['type']}

            #**Close Probability:** {lead['probability']}%
            #""")

        #with col2:
            #if st.button("🗑", key=f"delete_{i}"):
                #st.session_state.leads.remove(lead)
                #st.rerun()

        #st.progress(lead["probability"] / 100)

        #st.info(lead["message"])
        #st.code(lead["message"])
        #st.divider()
        
## You built:  AI → CRM → UI → History → Messaging
## AI Sales Assistant v1
## AI Lead Intelligence Platform v1

###########################################################
## Edit Lead ✏️ ##

for i, lead in enumerate(sorted_leads):
    with st.container():

        col1, col2, col3 = st.columns([6,1,1])

        with col1:
            if lead["probability"] >= 85:
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
                st.session_state.leads.remove(lead)
                pd.DataFrame(st.session_state.leads).to_csv(DB_FILE, index=False) # Save After Delete

                st.rerun()

        st.progress(lead["probability"] / 100)

        st.info(lead["message"])
        st.code(lead["message"])
        st.divider()
###########################################################33

if "edit_lead" in st.session_state:

    st.write("## ✏️ Edit Lead")

    edit_name = st.text_input("Name", st.session_state.edit_lead["name"])
    edit_type = st.text_input("Type", st.session_state.edit_lead["type"])

    if st.button("Save Changes"):
        st.session_state.leads[st.session_state.edit_index]["name"] = edit_name
        st.session_state.leads[st.session_state.edit_index]["type"] = edit_type

        del st.session_state.edit_lead
        st.rerun()

### python -m streamlit run UI.py
## MVP Level 1 complete

## AI SaaS platform structure ---- after adding the login

#You now have:

#Login screen
#User session
#Logout button
#Multi-page app
#AI backend
#CRM leads
#Analytics dashboard
#Filters + search
#Download CSV

#This is now a complete AI SaaS MVP

#Perfect — now we make each user see only their own leads.
#This turns your app into multi-user SaaS.

#Right now:

#admin sees all leads
#agent sees all leads

#We fix that.