import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

text = requests.get('https://www.se.rit.edu/~swen-261/00/schedule-spring-2perTR-NEW-project.html').text

today = datetime.today().strftime('%m-%d-%Y')

with open(f'logs/{today}-oss.html', 'w') as f:
    f.write(text)
