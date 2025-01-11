import streamlit as st

# URL of your Looker Studio dashboard
url = "file:///F:/spark/qgis/qgisweb/aksesibilitas_pendidikan/index.html"  # Replace with your Looker Studio URL

# Use Streamlit's full page width
st.set_page_config(layout="wide")

# # Embed the dashboard using an iframe that takes the full screen
# st.components.v1.iframe(url, width=1100, height=1600)  # Adjust dimensions if needed
