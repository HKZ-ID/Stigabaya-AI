from crewai import Agent
from llm import llm

class Agents:
    def __init__(self):
        pass
    def Agent1(self):
        return Agent(
            role="Administrator SMK Negeri 3 Surabaya",  #Masukkan pekerjaan agen disini
            goal="Mencari informasi segala hal terkait Sekolah Menengah Kejuruan, terutama SMK Negeri 3 Surabaya", #Masukkan goal dari pekerja
            backstory="Kamu adalah seorang expert dan ahli administrator yang bertugas memilah informasi segala hal mengenai persekolahan di SMK Negeri 3 Surabaya,informasi itu termasuk Akademik, Prestasi, Ekstra kulikuler dan lain sebagainya", #berikan latar belakang pekerja
            allow_delegation=False,
            verbose=True,
            llm = llm
        )
    def Agent2(self):
        return Agent(
            role="Penulis Jawaban Administratif",  #Masukkan pekerjaan agen disini
            goal="Memberikan jawaban terkait dari pertanyaan Administratif dan Umum terkait SMK Negeri 3 Surabaya", #Masukkan goal dari pekerja
            backstory="kamu adalah seorang expert dan ahli pemberi jawaban administratif yang memberikan jawaban yang tidak bertele-tele dan akurat untuk kejelasan informasi yang tepat", #berikan latar belakang pekerja
            allow_delegation=False,
            verbose=True,
            llm = llm
        )
