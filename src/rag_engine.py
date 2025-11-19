import google.generativeai as genai
from .config import GEMINI_API_KEY
from .models import Employee
from sqlalchemy import text
from .database import SessionLocal

genai.configure(api_key=GEMINI_API_KEY)
MODEL = genai.GenerativeModel("gemini-2.5-flash")

def nl_to_sql(query: str) -> str:
    prompt = f"""
You are an expert SQL generator.

TABLE employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    department TEXT,
    salary FLOAT
);

RULES:
- Return only SQL.
- SQL must be SELECT only.
- No delete/update/insert/drop.
- If unsure return:
  SELECT * FROM employees LIMIT 0;

User query:
\"\"\"{query}\"\"\"
"""
    try:
        response = MODEL.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"-- ERROR generating SQL: {e}"


def run_sql(sql: str):
    session = SessionLocal()
    try:
        return session.execute(text(sql)).fetchall()
    except Exception as e:
        return f"SQL ERROR: {e}"
    finally:
        session.close()


def format_results(result):
    if isinstance(result, str):
        return result

    if not result:
        return "No results."

    return "\n".join(str(dict(row._mapping)) for row in result)
