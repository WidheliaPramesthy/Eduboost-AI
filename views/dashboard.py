import streamlit as st
import plotly.express as px
import pandas as pd

# Set up the page
st.set_page_config(page_title="Dashboard Pendidikan Indonesia", page_icon=":material/team_dashboard:", layout="wide")
st.title("Dashboard Pendidikan di Indonesia")

# Data untuk Pie Chart - Persentase Putus Sekolah
dropout_data = ['SD', 'SMP', 'SMA']
dropout_percentages = [62.54, 25.05, 13.41]

# Kolom untuk menampilkan 3 Chart berdampingan
c1, c2, c3 = st.columns(3)

# Bar Chart Jumlah Siswa per Jenjang Pendidikan
with c1:
    school_data = {'Jenjang': ['SD', 'SMP', 'SMA'], 'Jumlah Siswa': [24064711, 9966118, 5311490]}
    df_school = pd.DataFrame(school_data)
    fig1 = px.bar(df_school, x='Jenjang', y='Jumlah Siswa', color='Jenjang', 
                  color_discrete_map={'SD': '#0368c9', 'SMP': '#5d97c4', 'SMA': '#83c9ff'},
                  #labels={'Jumlah Siswa': 'Jumlah Siswa', 'Jenjang': 'Jenjang Pendidikan'},
                  title="Jumlah Siswa")
    st.plotly_chart(fig1, use_container_width=True)

# Bar Chart Rata-rata Lama Sekolah per Jenis Kelamin
with c2:
    gender_data = {'Jenis Kelamin': ['Laki-laki','Perempuan'],
                   'Rata-rata Lama Sekolah (Tahun)': [ 9.43,9.01]}
    df_gender = pd.DataFrame(gender_data)
    fig2 = px.bar(df_gender, x='Jenis Kelamin', y='Rata-rata Lama Sekolah (Tahun)', color='Jenis Kelamin',
                  color_discrete_map={ 'Laki-laki': '#0368c9','Perempuan': '#ff2d2c'},
                  #labels={'Rata-rata Lama Sekolah (Tahun)': 'Rata-rata Lama Sekolah (Tahun)', 'Jenis Kelamin': 'Jenis Kelamin'},
                  title="Rata-rata Lama Sekolah Per Jenis Kelamin")
    st.plotly_chart(fig2, use_container_width=True)

# Pie Chart Persentase Putus Sekolah
with c3:
    fig3 = px.pie(values=dropout_percentages, names=dropout_data, title="Persentase Putus Sekolah")
    st.plotly_chart(fig3, use_container_width=True)

# Menambahkan gambar peta
st.subheader("Peta Aksesibilitas Pendidikan")
st.image("images/isochrone.png", caption="Peta Aksesibilitas Pendidikan", use_container_width=True)

st.markdown("""
    <hr>
    <footer style="text-align:center; font-size:14px; color:gray;">
        <p>Eduboost AI | Solusi Digital untuk Pendidikan Indonesia Emas 2045</p>
        <p>© 2025 Eduboost AI. Semua hak cipta dilindungi.</p>
    </footer>
    """, unsafe_allow_html=True)
