import streamlit as st
import requests
from streamlit_lottie import st_lottie

# --- ASSETS ---
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_animation_cover = "https://lottie.host/58de6174-3193-4132-aa17-de25448c4d57/0OOJLckCRH.json"
icon1 = "images/student.png"
icon2 = "images/users-class.png"



# --- PAGE CONFIG ---
logo = "images/logo.png"
st.set_page_config(page_title="Eduboost AI", page_icon=logo, layout="wide")



# --- HEADER SECTION ---
# Check if wide mode is enabled (side navigation is shown or not)
wide_mode = st.get_option("theme.base") != "dark"

# Adjust layout based on mode
if wide_mode:
    with st.container():
        col1, col2, col3 = st.columns([3, 5, 1])  # Three columns for wide mode

        # Left column for animation
        with col1:
            st_lottie(lottie_animation_cover, height=300, key="cover-animation")

        # Middle column for text
        with col2:
            st.markdown(
                """
                <div style="text-align: center;">
                    <h1 style="margin-bottom: 10px;">Eduboost AI</h1>
                    <h3 style="margin-bottom: 5px;">
                        Solusi Digital Terpadu untuk Meningkatkan
                        Kualitas dan Pemerataan Pendidikan
                    </h3>
                    <h4 style="
                        font-size: 20px; 
                        margin: 0; 
                        display: inline-block; 
                        background-color: #FFD700; 
                        padding: 10px 3px 10px 20px; 
                        border-radius: 5px; 
                        color: #000;
                    ">Menuju Indonesia Emas 2045</h4>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Right column (empty for now, can be used later if needed)
        with col3:
            pass

else:
    # Compact layout for narrow mode (side navigation enabled)
    with st.container():
        col1, col2 = st.columns([1, 5])  # Two columns when side navigation is shown

        # Left column for animation
        with col1:
            st_lottie(lottie_animation_cover, height=200, key="cover-animation")

        # Right column for text
        with col2:
            st.markdown(
                """
                <div style="text-align: left;"> <!-- Align text to the left -->
                    <h1 style="margin-bottom: 10px;">Eduboost AI</h1>
                    <h3 style="margin-bottom: 5px;">
                        Solusi Digital Terpadu untuk Meningkatkan
                        Kualitas dan Pemerataan Pendidikan
                    </h3>
                    <h4 style="
                        font-size: 20px; 
                        margin: 0; 
                        display: inline-block; 
                        background-color: #FFD700; 
                        padding: 10px 3px 10px 20px; 
                        border-radius: 5px; 
                        color: #000;
                    ">Menuju Indonesia Emas 2045</h4>
                </div>
                """,
                unsafe_allow_html=True
            )

# # --- CUSTOM CSS FOR DARK & LIGHT MODE ---
st.markdown("""
    <style>
    /* Kotak */
    .stat-box {
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 10px;
        transition: background-color 0.3s ease, color 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* Menjaga jarak antara elemen di dalam */
        height: 300px; /* Set tinggi kotak tetap */
        max-width: 100%; /* Agar tidak melebar */
    }

    /* Light Mode */
    @media (prefers-color-scheme: light) {
        .stat-box {
            background-color: #4f4f4f; /* Abu-abu gelap */
            color: #ffffff; /* Teks putih */
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        }
    }

    /* Dark Mode */
    @media (prefers-color-scheme: dark) {
        .stat-box {
            background-color: #d9d9d9; /* Abu-abu terang */
            color: #000000; /* Teks hitam */
            box-shadow: 2px 2px 8px rgba(255, 255, 255, 0.1);
        }
    }

    /* Ikon */
    .stat-icon {
        margin-bottom: 10px;
        width: 40px;
        height: 40px;
        margin-top: 10px; /* Memberi jarak antar ikon dan teks */
    }

    /* Teks */
    .stat-text {
        font-size: 30px;
        margin-bottom: 5px;
        margin-top: 15px;
        font-weight: bold;
    }
    
    .number-text {
        font-size: 20px !important;
        font-weight: bold;
        margin-bottom: 0px;
    }
            
    .number-subtext {
        font-size: 15px;
        margin-top: 0px;
    }

    .stat-subtext {
        font-size: 15px;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- STATISTICS SECTION ---
with st.container():
    st.write("")  # Ini akan memberikan jarak antar elemen
    col1, col2, col3, col4, col5 = st.columns(5)

    # Isi masing-masing kotak
    with col1:
        
        st.markdown(
            """
            <div class="stat-box">
                <p class="stat-text">Rata-Rata Lama Sekolah</p>
                <p class="number-text">8,85</p>
                <p class="number-subtext">Tahun</p>
                <p class="stat-subtext">Sumber: <br>BPS (2024)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="stat-box">
                <p class="stat-text">Jumlah <br> Siswa</p>
                <p class="number-text">39</p>
                <p class="number-subtext">Juta</p>
                <p class="stat-subtext">Sumber:<br>Kemendikbud (2024)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="stat-box">
                <p class="stat-text">Angka Putus Sekolah</p>
                <p class="number-text">0,18</p>
                <p class="number-subtext">Persen</p>
                <p class="stat-subtext">Sumber:<br>Kemendikbud (2024)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="stat-box">
                <p class="stat-text">Kerusakan Kelas SMP</p>
                <p class="number-text">27.121</p>
                <p class="number-subtext">Rusak Berat</p>
                <p class="stat-subtext">Sumber: <br>Kemendikbud (2024)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            """
            <div class="stat-box">
                <p class="stat-text">Kerusakan Kelas SMA</p>
                <p class="number-text">10.692</p>
                <p class="number-subtext">Rusak Berat</p>
                <p class="stat-subtext">Sumber: <br>Kemendikbud (2024)</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# Section 3: Pentingnya 1000 HPK (Hari Pertama Kehidupan)
st.write("---")
st.header("Solusi Unggulan Eduboost AI")
st.markdown("")
causes = {
    "Segmetasi kebutuhan sumber daya pendidikan": (
        "Pemodelan ***machine learning*** digunakan untuk melakukan **segmentasi geospasial kebutuhan sumber daya pendidikan** secara akurat. Dengan pendekatan berbasis data ini, pemerintah dapat dengan mudah mengidentifikasi kebutuhan alokasi sumber daya pendidikan di berbagai wilayah, memastikan keputusan yang lebih tepat sasaran dan berdampak maksimal."
    ),
    "Analisis aksesibilitas fasilitas pendidikan": (
        "Dengan ***isochrone analysis***, aksesibilitas pendidikan dipetakan dan dianalisis secara mendalam untuk memvisualisasikan area yang dapat dijangkau dalam waktu atau jarak tertentu dari fasilitas pendidikan. Eduboost AI menghadirkan solusi ini untuk mengidentifikasi kesenjangan akses, mendukung perencanaan berbasis data, dan mewujudkan pemerataan pendidikan yang lebih baik."
    ),
    "Dashboard analytics": (
        "Dashboard analytics menyediakan fitur pemantauan komprehensif untuk mendukung pemangku kepentingan dalam mencapai target program prioritas pendidikan. "
    ),
    "Asisten AI": (
        "Dukungan asisten AI berbasis teknologi Generative AI dalam bentuk chatbot membantu memberikan akses informasi secara cepat, serta memberikan rekomendasi kebijakan yang tepat untuk mendukung tercapainya target pembangunan pendidikan Indonesia. "
        
    )
}

# Menampilkan informasi tentang setiap cause dengan expander dan progress bar
for i, (cause, explanation) in enumerate(causes.items()):
    with st.expander(cause):
        st.write(explanation)
        st.progress((i + 1) * 20)

st.markdown("""
    <hr>
    <footer style="text-align:center; font-size:14px; color:gray;">
        <p>Eduboost AI | Solusi Digital untuk Pendidikan Indonesia Emas 2045</p>
        <p>© 2025 Eduboost AI. Semua hak cipta dilindungi.</p>
    </footer>
    """, unsafe_allow_html=True)

