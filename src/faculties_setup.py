import requests
from bs4 import BeautifulSoup
import sqlite3

class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(path)
        self.cursor = self.db.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def commit(self):
        self.db.commit()

db = DBclass('data.db')

url = 'https://www.iiit.ac.in/people/faculty/'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

faculty_entries = soup.find('table', id="faculty")
faculty_entries = faculty_entries.find_all('tr')

for entry in faculty_entries:
    data=entry.find_all('td')
    data=data[1]
    name=data.find('h3', class_="name").text
    designation_and_study=data.find('p').text
    designation_and_study.strip()
    designation_and_study=designation_and_study.split('\n')
    designation=(designation_and_study[1].strip())
    
    study=(designation_and_study[2].strip())

    research_areas=data.find_all('p')
    research_areas=research_areas[1].text.split('\n')
    research_areas=research_areas[2].strip()
    
    research_center=data.find_all('p')
    research_center=research_center[2].find('a')
    research_center=research_center.text
    
    query_for_insert=f"INSERT INTO faculty (name, designation, study, research_areas, research_center) VALUES ('{name}', '{designation}', '{study}', '{research_areas}', '{research_center}');"
    print(query_for_insert)
    try:
        db.execute(query_for_insert)
        db.commit()
    except:
        continue