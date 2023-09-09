import sqlite3

conn = sqlite3.connect('web_search.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link VARCHAR(100)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS search_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link_id INTEGER,
        keyword VARCHAR(100),
        frequency INTEGER,
        FOREIGN KEY (link_id) REFERENCES links (id)
    )
''')

conn.commit()
conn.close()
import requests
from bs4 import BeautifulSoup

def search_page(link, keyword):
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        frequency = text.lower().count(keyword.lower())
        return frequency
    except Exception as e:
        print(f"Помилка під час пошуку на {link}: {e}")
        return 0
