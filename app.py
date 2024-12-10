import streamlit as st
import base64
from agents import Agents
from tasks import Tasks
from llm import llm
from crewai import Crew, Process

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

local_image1_base64 = get_base64_image("media/gambar.png") 
local_image2_base64 = get_base64_image("media/hebat.png")
local_image3_base64 = get_base64_image("media/seameo.png")
local_image4_base64 = get_base64_image("media/pens.png")
local_image5_base64 = get_base64_image("media/gema.png")

box_style = f"""
<style>
.gradient-box {{
    background: white;
    border-radius: 10px;
    width: 100%;
    height: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 3s ease-in-out;
}}
.gradient-box img {{
    margin: 0 5px;
    opacity: 0.8;
    height: 100px;
}}
</style>
"""

st.markdown(box_style, unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="gradient-box">
        <img src="data:image/png;base64,{local_image1_base64}" alt="Local Logo 1">
        <img src="data:image/png;base64,{local_image2_base64}" alt="Local Logo 2">
        <img src="data:image/png;base64,{local_image3_base64}" alt="Local Logo 2">
        <img src="data:image/png;base64,{local_image4_base64}" alt="Local Logo 2">
        <img src="data:image/png;base64,{local_image5_base64}" alt="Local Logo 2">
    </div>
    """, unsafe_allow_html=True
)

st.title("💬 STIGABAYA AI")
st.caption("🚀 Sebuah AI Smart School Streamlit yang didukung oleh OpenAI dan CrewAI.")
                    
import streamlit as st
from crewai import Crew, Process
from agents import Agents
from tasks import Tasks

# Header dan Informasi Pengguna
st.header("Informasi Pengguna")
name = st.text_input("Nama Lengkap :", placeholder="Masukkan Nama Lengkap...")
phone = st.text_input("Nomor Telepon :", placeholder="Masukkan Nomor Telepon...")
category = st.selectbox(
    "Kategori Identitas :",
    [
        "Pilih Kategori Identitas...",
        "Guru",
        "Siswa/Siswi",
        "Orang Tua/Wali",
        "Masyarakat Umum",
    ],
)

# Validasi Input Pengguna
if not name or not phone or category == "Pilih Kategori Identitas...":
    st.warning("❕ Pastikan semua data pengguna telah diisi dengan benar.")
else:
    st.success("✅ Data pengguna lengkap.")

    # Input Pertanyaan
    with st.container():
        st.header("Pertanyaan Terkait SMKN 3 Surabaya")
        input_question = st.text_input(
            "Silahkan masukkan pertanyaan:",
            placeholder="Contoh: Apa program keahlian yang tersedia di SMKN 3 Surabaya?",
        )
        insert_button = st.button("Cari!")

    # Chatting dan Proses Pencarian
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Apa yang ingin ditanyakan?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if insert_button:
        if not input_question:
            st.error("❌ Pertanyaan tidak boleh kosong.")
        else:
            try:
                tugas = Tasks(input_question)
                crew = Crew(
                    agents=[Agents().Agent1(), Agents().Agent2()],
                    tasks=[tugas.task1(), tugas.task2()],
                    process=Process.sequential
                )

                with st.spinner("Sedang mencari informasi..."):
                    agent_response = str(crew.kickoff())

                # Tambahkan ke sesi chat
                st.session_state["messages"].append({"role": "user", "content": input_question})
                st.chat_message("user").write(input_question)
                st.session_state["messages"].append({"role": "assistant", "content": agent_response})
                st.chat_message("assistant").write(agent_response)

            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
