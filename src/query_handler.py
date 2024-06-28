# query_handler.py
import os
import google.generativeai as genai
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# Database setup
DATABASE_URI = 'sqlite:///lottery_game.db'
engine = create_engine(DATABASE_URI)

# Configure Gemini API using environment variable
api_key_gemini = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key_gemini)
model = genai.GenerativeModel('gemini-pro')

def query_database(query):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))
            return result.fetchall()
    except OperationalError as e:
        print(f"An error occurred: {e}")
        return []

def generate_sql_query(nl_query):
    response = model.generate_content(f"Translate this natural language query into SQL. Use 'lottery_game' as the table name and use the columns 'jackpot' and 'draw_date'. Assume jackpot values are plain numbers: {nl_query}")
    sql_query = response.text.strip()
    # Remove any markdown formatting
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
    return sql_query

def handle_query(nl_query):
    sql_query = generate_sql_query(nl_query)
    print(f"Generated SQL Query: {sql_query}")
    result = query_database(sql_query)
    return result
