import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
from sqlalchemy import create_engine

'''
For Web scrapping, i'll be using fbref website
https://fbref.com
'''  

url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'

# Sending a get request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

# Starting the data extraction
players = [] # List to store player data

# Within the website we need find the table with player stats
# Finding the comment containing the table with player stats
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for comment in comments:
    if 'table_container' in comment:
        table_soup = BeautifulSoup(comment, 'html.parser')
        table = table_soup.find('table', {'id': 'stats_standard'})
        break


# Checkinf if the table was found
  
if table is not None:
    # Traversing through the table with player stats
    tbody = table.find('tbody')
    if tbody:
        for row in tbody.find_all('tr'):
            th_player = row.find('th', {'data-stat': 'player'})
            if th_player:
                name = th_player.text.strip()
                position = row.find('td', {'data-stat': 'position'})
                if position:
                    position = position.text.strip()
                else:
                    position = 'Unknown'

                age = row.find('td', {'data-stat': 'age'})
                if age:
                    age = age.text.strip()
                else:
                    age = 'Unknown'

                club = row.find('td', {'data-stat': 'team'})
                if club:
                    club = club.text.strip()
                else:
                    club = 'Unknown'

                appearances = row.find('td', {'data-stat': 'games'})
                if appearances:
                    appearances = appearances.text.strip()
                else:
                    appearances = '0'

                goals = row.find('td', {'data-stat': 'goals'})
                if goals:
                    goals = goals.text.strip()
                else:
                    goals = '0'

                assists = row.find('td', {'data-stat': 'assists'})
                if assists:
                    assists = assists.text.strip()
                else:
                    assists = '0'

                players.append({
                    'Name': name,
                    'Age': age,
                    'Position': position,
                    'Club': club,
                    'Appearances': appearances,
                    'Goals': goals,
                    'Assists': assists
                })
            else:
                print("Player name not found for a row. Skipping.")
    else:
        print("Table body not found.")
        
else:
    print("Table not found.")

# Converting the list of players into a DataFrame
df = pd.DataFrame(players)

# Save data in CSV format
csv_path = 'data/raw/fbref_player_stats.csv'
df.to_csv(csv_path, index=False)

# Creating a connection to an SQLite database
engine = create_engine('sqlite:///data/raw/players_data.db')

# Save DataFrame to SQL database
df.to_sql('player_stats', engine, if_exists='replace', index=False)