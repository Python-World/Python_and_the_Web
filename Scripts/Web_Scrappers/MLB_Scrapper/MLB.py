import pandas as pd 
import re 
import requests 
from bs4 import BeautifulSoup 
url  = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1"
page = requests.get (url)
soup= BeautifulSoup(page.text,'html.parser')
row=soup.find('tr',attrs = {'class': 'oddrow player-10-33039'})
for data in row.find_all('td'):
    print (data.get_text())
    
header = soup.find('tr', attrs ={'class':'colhead'})
columns= [col.get_text() for col in header.find_all('td')]
final_df=pd.DataFrame(columns=columns)
print(final_df)

for i in range(1,331,50):
    url  = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1"
    page = requests.get (url)
    soup= BeautifulSoup(page.text,'html.parser')
    players=soup.find('tr',attrs = {'class': re.compile('row player-10-')})
    for player in players:
        stats=[stat.get_text() for stat in players.find_all('td')]
        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns= columns
        final_df= pd.concat([final_df,temp_df],ignore_index=True)
print(final_df)

final_df.to_csv(r"storage/emulated/0/mlb_stats.csv",sep=',', encoding='utf-8')
