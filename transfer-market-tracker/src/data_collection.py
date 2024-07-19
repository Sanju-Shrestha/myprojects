from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()

driver.get("Insert the website link here")   # udpate required

players = driver.find_elements(By.XPATH,"#Update the XPATH here#/td[1]/a")

nations = driver.find_elements(By.XPATH,"#Update the XPATH here#/td[2]/a/span/span")

positions = driver.find_elements(By.XPATH,"#Update the XPATH here#/td[3]")

squads = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[4]/a")

ages = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[5]")

borns = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[6]")

MPs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[7]")

starts = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[8]")

minutes = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[9]")

nineties = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[10]")

Glss = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[11]")

Asts = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[12]")

GAs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[13]")

G_PKs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[14]")

PKs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[15]")

PKatts = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[16]")

CrdYs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[17]")

CrdRs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[18]")

xGs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[19]")

npxGs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[20]")

xAGs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[21]")

npxG_xAGs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[22]")

PrgCs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[23]")

PrgPs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[24]")

PrgRs = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[25]")

Gls_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[26]")

Ast_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[27]")

GA_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[28]")

G_PK_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[29]")

GA_PK_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[30]")

xG_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[31]")

xAG_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[32]")

xG_xAG_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[33]")

npxG_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[34]")

npxG_xAG_per90s = driver.find_elements(By.XPATH, "#Update the XPATH here#/td[35]")


# for postion in positions:
#     print(postion.text)


result = []

for i in range(len(players)):
    temporary_data = {
        'Player': players[i].text,
        'Nation': nations[i].text,
        'Position': positions[i].text,
        'Squad': squads[i].text,
        'Age': ages[i].text,
        'Born': borns[i].text,
        'MP': MPs[i].text,
        'Starts': starts[i].text,
        'Min': minutes[i].text,
        '90s': nineties[i].text,
        'Gls': Glss[i].text,
        'Ast': Asts[i].text,
        'G+A': GAs[i].text,
        'G-PK': G_PKs[i].text,
        'PK': PKs[i].text,
        'PKatt': PKatts[i].text,
        'CrdY': CrdYs[i].text,
        'CrdR': CrdRs[i].text,
        'xG': xGs[i].text,
        'npxG': npxGs[i].text,
        'xAG': xAGs[i].text,
        'npxG+xAG': npxG_xAGs[i].text,
        'PrgC': PrgCs[i].text,
        'PrgP': PrgPs[i].text,
        'PrgR': PrgRs[i].text,
        'Gls_per90': Gls_per90s[i].text,
        'Ast_per90': Ast_per90s[i].text,
        'G+A_per90': GA_per90s[i].text,
        'G-PK_per90': G_PK_per90s[i].text,
        'G+A-PK_per90': GA_PK_per90s[i].text,
        'xG_per90': xG_per90s[i].text,
        'xAG_per90': xAG_per90s[i].text,
        'xG+xAG_per90': xG_xAG_per90s[i].text,
        'npxG_per90': npxG_per90s[i].text,
        'npxG+xAG_per90': npxG_xAG_per90s[i].text
        }
    
    result.append(temporary_data)

df_data = pd.DataFrame(result)
df_data.to_csv('data/raw/Premier-League-Data.csv',index=False)

