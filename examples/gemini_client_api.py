from pathlib import Path
from rich import print
from geminiplayground import GeminiClient
from geminiplayground.schemas import UploadFile

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if __name__ == "__main__":
    gemini_client = GeminiClient()
    files = gemini_client.query_files(limit=5)
    print(files)
