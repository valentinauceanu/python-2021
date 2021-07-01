# pip & virtual environment
# web scraping
# proces de obtinere de informatii
import requests
from bs4 import BeautifulSoup

url = 'https://lpf.ro/liga-1'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

stage_table = soup.find(class_ = 'clasament_general white-shadow etape_meciuri')
# print(stage_table.prettify())
team_rows = stage_table.find_all(class_ = 'echipa-etapa-1')
#print(teams_cell)
teams = []
for team in team_rows:
    team_cell = team.find('a')
    team_name = team_cell.find(class_ = 'hiddenMobile').text.strip()
    teams.append(team_name)


print(teams)