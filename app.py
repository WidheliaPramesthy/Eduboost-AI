import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    page="views/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
chatbot_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/smart_toy:"
)

map_page = st.Page(
    page="views/map.py",
    title="Peta Aksesibilitas Pendidikan",
    icon=":material/team_dashboard:"
)

dashboard_page = st.Page(
    page="views/dashboard.py",
    title="Dashboard Analytics",
    icon=":material/team_dashboard:"
)


# --- NAVIGATION SETUP ---
pg = st.navigation(pages=[home_page, dashboard_page, chatbot_page], expanded=False)

# --- RUN NAVIGATION ---
pg.run()
