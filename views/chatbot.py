import streamlit as st

st.set_page_config(page_title="Chatbot Assistant", page_icon=":material/smart_toy:", layout="wide")
st.title("Eduboost AI Chatbot")

with st.chat_message(name="assistant"):
    st.write("Selamat datang di Eduboost AI! Jelajahi solusi digital kami untuk peningkatan dan pemerataan pendidikan di Indonesia.\n\n"
             "Ajukan pertanyaan Anda sekarang dan dapatkan informasiyang Anda butuhkan.")

with st.chat_message(name="user"):
    st.write("Berapa lama wajib belajar di Indonesia?")

with st.chat_message(name="assistant"):
    st.write("Berdasarkan Peta Jalan Pendidikan 2025-2045 oleh Bappenas, wajib belajar di Indonesia kini 13 tahun, yaitu 1 tahun pendidkan pra-sekolah dan 12 tahun pendidikan dasar serta menengah.")
    
with st.chat_message(name="user"):
    st.write("Kalau rata-rata lama sekolah di Indonesia sekarang berapa?.")

with st.chat_message(name="assistant"):
    st.write("Rata-rata lama sekolah di Indonesia tahun 2024 ialah 8,85 tahun (Sumber: BPS)")

# Input pengguna untuk pertanyaan
user_question = st.chat_input("Ajukan pertanyaan Anda di sini:", key="user_input")

