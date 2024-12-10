import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
from crewai_tools import WebsiteSearchTool
from pydantic import Field
from langchain_community.utilities import GoogleSerperAPIWrapper

# Set up your SERPER_API_KEY key in an .env file, eg:
# SERPER_API_KEY=<your api key>
load_dotenv()

class SearchTool(BaseTool):
    name: str = "Search"
    description: str = "Useful for search-based queries. Use this to find current information about markets, companies, and trends."
    search: GoogleSerperAPIWrapper = Field(default_factory=GoogleSerperAPIWrapper)

    def _run(self, query: str) -> str:
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"
        
        

# Daftar URL yang ingin Anda tambahkan
websites = [
    'https://smkn3-sby.sch.id/',
    'https://www.instagram.com/official.smkn3sby/?hl=en',
    'https://dapo.kemdikbud.go.id/sekolah/B5FC8FF06E3499DB9EAB',
    'https://referensi.data.kemdikbud.go.id/tabs.php?npsn=20532195',
    'https://smkn3-sby.sch.id/visi-misi-smk-negeri-3-surabaya/',
    'https://smkn3-sby.sch.id/struktur-organisasi/',
    'https://smkn3-sby.sch.id/fasilitas/',
    'https://smkn3-sby.sch.id/gtk/',
    'https://smkn3-sby.sch.id/bisnis-konstruksi-dan-properti-bkp/',
    'https://smkn3-sby.sch.id/desain-pemodelan-informasi-bangunan-dpib/',
    'https://smkn3-sby.sch.id/teknik-audio-video-tav/',
    'https://smkn3-sby.sch.id/teknik-instalasi-tenaga-listrik-titl/',
    'https://smkn3-sby.sch.id/teknik-kendaraan-ringan-otomotif-tkro/',
    'https://smkn3-sby.sch.id/teknik-pemesinan-tpm/',
    'https://smkn3-sby.sch.id/multimedia-mm/',
    
]

# Membuat daftar alat pencarian untuk setiap situs web
tool = WebsiteSearchTool(websites=websites)

