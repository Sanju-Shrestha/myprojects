from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')              # disables the sandbox for the browser
    options.add_argument('--headless')                # Runs the browser in headless mode i.e. it operates without a GUI.
    options.add_argument('--disable-gpu')             # Disables GPU hardware acceleration, which is useful for headless mode.
    options.add_argument('--disable-dev-shm-usage')   # Reduces the amount of memory shared between the browser and other processes.
    driver = webdriver.Chrome(options=options)
    return driver

def different_league_data(url):
    driver = web_driver()
    driver.get(url)
    
    try:
        # We identify the table element using the table id and then extract its HTML
        elem = driver.find_element(By.ID, "stats_standard")
        table_html = elem.get_attribute('outerHTML')

        # Parsing the HTML using BeautifulSoup
        soup = BeautifulSoup(table_html, 'html.parser')
        table = soup.find('table')
        
        # Using StringIO to wrap the HTML string
        html_string = str(table)
        # Using pandas to read the HTML table
        df = pd.read_html(StringIO(html_string))[0]
        
    except Exception as e:
        print(f"An error occurred: {e}")
        df = pd.DataFrame()  # Return an empty DataFrame in case of error
        
    finally:
        driver.quit()   # WebDriver is closed regardless of whether an error occurs.
    
    return df

# # Scrape data from Premier League
# premier_league_data = different_league_data("https://fbref.com/en/comps/9/stats/Premier-League-Stats")
# df_data1 = pd.DataFrame(premier_league_data)

# # Scrape data from Serie A
# serie_a_data = different_league_data("https://fbref.com/en/comps/11/stats/Serie-A-Stats")
# df_data2 = pd.DataFrame(serie_a_data)

# # Combine data from both leagues
# combined_data = pd.concat([df_data1, df_data2])

# combined_data.to_csv('data/raw/data_collection_raw.csv',index=False)

def collect_multiple_leagues(urls):
    all_data = []
    for url in urls:
        league_data = different_league_data(url)
        all_data.append(league_data)
    combined_data = pd.concat(all_data, ignore_index=True)
    return combined_data

# List of league URLs
urls = [
    "https://fbref.com/en/comps/9/stats/Premier-League-Stats",          # English Premeir League
    "https://fbref.com/en/comps/11/stats/Serie-A-Stats",                # Italian Serie A
    "https://fbref.com/en/comps/12/stats/La-Liga-Stats",                # Spanish La Liga
    "https://fbref.com/en/comps/13/stats/Ligue-1-Stats",                # French Ligue 1
    "https://fbref.com/en/comps/20/stats/Bundesliga-Stats",             # German Bundesliga
    "https://fbref.com/en/comps/22/stats/Major-League-Soccer-Stats",    # USA MLS
    "https://fbref.com/en/comps/23/stats/Eredivisie-Stats",             # Netherlands Eredivisie
    "https://fbref.com/en/comps/32/stats/Primeira-Liga-Stats",          # Portuguese Primeira Liga
]

# Scrape data from multiple leagues
combined_data = collect_multiple_leagues(urls)

# Save the combined data to a CSV file
combined_data.to_csv('data/raw/data_collection_raw.csv', index=False)

print("Data has been successfully scraped and saved to data/raw/data_collection_raw.csv")