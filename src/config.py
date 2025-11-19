import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if not GEMINI_API_KEY:
    raise ValueError("Set GEMINI_API_KEY in .env")

if not DATABASE_URL:
    raise ValueError("Set DATABASE_URL in .env")
