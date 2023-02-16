import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

text = requests.get('https://www.se.rit.edu/~swen-261/00/schedule-spring-2perTR-NEW-project.html').text


with open(f'logs/current-oss.html', 'w') as f:
    f.write(text)
