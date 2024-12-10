from crewai import Task
from llm import llm
from agents import Agents
from tools import SearchTool, tool

class Tasks:
    def __init__(self, input):
        self.input = input

    def task1(self):
        return Task(
            description=f"carilah informasi mengenai SMK NEGERI 3 SURABAYA yang akurat dan tidak bertele-tele berdasarkan dari pertanyaan yang dimasukkan dari {self.input}, gunakan [SearchTools(), tool] yang disediakan untuk mencari berbagai informasi dari berbagai sumber terutama sumber data pendidikan, contohnya antara lain: 'https://smkn3-sby.sch.id/', 'https://www.instagram.com/official.smkn3sby/?hl=en', 'https://dapo.kemdikbud.go.id/sekolah/B5FC8FF06E3499DB9EAB', 'https://referensi.data.kemdikbud.go.id/tabs.php?npsn=20532195', 'https://smkn3-sby.sch.id/visi-misi-smk-negeri-3-surabaya/', 'https://smkn3-sby.sch.id/struktur-organisasi/', 'https://smkn3-sby.sch.id/fasilitas/', 'https://smkn3-sby.sch.id/gtk/', 'https://smkn3-sby.sch.id/bisnis-konstruksi-dan-properti-bkp/', 'https://smkn3-sby.sch.id/desain-pemodelan-informasi-bangunan-dpib/', 'https://smkn3-sby.sch.id/teknik-audio-video-tav/', 'https://smkn3-sby.sch.id/teknik-instalasi-tenaga-listrik-titl/', 'https://smkn3-sby.sch.id/teknik-kendaraan-ringan-otomotif-tkro/', 'https://smkn3-sby.sch.id/teknik-pemesinan-tpm/', 'https://smkn3-sby.sch.id/multimedia-mm/', 'https://smkn3-sby.sch.id/ekskul/', 'https://smkn3-sby.sch.id/agenda/' ",
            expected_output=f"memngumpulkan informasi yang akurat mengenai smk negeri 3 surabaya berdasarkan dari pertanyaan yang dimasukkan dari {self.input}, kemudian meneliti informasi tersebut menjadi jawaban yang akurat dan tidak bertele-tele",
            agent= Agents().Agent1(),
            tools=[SearchTool(), tool]
        )
    def task2(self):
        return Task(
            description=f"carilah jawaban yang akurat, rinci, jelas, detail dan tidak bertele-tele dari pertanyaan yang dimaksukkan dari {self.input} terkait dengan SMK NEGERI 3 SURABAYA, gunakan informasi yang disediakan dan didapatkan dari agent1 dan task1 untuk mencari jawabannya",
            expected_output=f"jawaban yang akurat, rinci, jelas, detail dan rinci dari pertanyaan yang diberikan dari {self.input} \n- jawaban :\npenjelasan jawaban \n kemudian pertanyaan yang mungkin serupa dan dapat ditawarkan terkait jawaban yang diberikan",
            agent= Agents().Agent2(),
        )
