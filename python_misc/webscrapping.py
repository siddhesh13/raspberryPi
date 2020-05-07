
from bs4 import BeautifulSoup
import requests
import time
import json
##with open('sample.html') as html_file:
##    soup = BeautifulSoup(html_file, 'lxml')
##
##for article in soup.find_all('div', class_ ='article'):
##    ##print(article)
##
##    headline = article.h2.a.text
##    print(headline)
##    summary = article.p.text
##    print(summary)


india = {
    'Total Cases': 0,
    'Active Cases': 0,
    'Cured': 0,
    'Deaths': 0,
    'Migrated': 0
    }

mah = {
    'Total Cases': 0,
    'Active Cases': 0,
    'Cured': 0,
    'Deaths': 0
    }
mah_dist = {
    "Mumnai": {
        'Total Cases': 0,
        'Active Cases': 0,
        'Cured': 0,
        'Deaths': 0,
        "delta":{
            "Total Cases": 0,
            'Cured': 0,
            'Deaths': 0
            }
        },
    "Pune": {
        'Total Cases': 0,
        'Active Cases': 0,
        'Cured': 0,
        'Deaths': 0,
        "delta":{
            "Total Cases": 0,
            'Cured': 0,
            'Deaths': 0
            }
        },
    "Thane": {
        'Total Cases': 0,
        'Active Cases': 0,
        'Cured': 0,
        'Deaths': 0,
        "delta":{
            "Total Cases": 0,
            'Cured': 0,
            'Deaths': 0
            }
        }
    }
source = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(source,'lxml')
active = soup.find('li', class_ = 'bg-blue')
cured = soup.find('li', class_ = 'bg-green')
deaths = soup.find('li', class_ = 'bg-red')
migrated = soup.find('li', class_ = 'bg-orange')
india['Active Cases'] = active.strong.text
india['Cured'] = cured.strong.text
india['Deaths'] = deaths.strong.text
india['Migrated'] = migrated.strong.text

extract_contents = lambda row: [x.text.replace('\n','') for x in row]
stats = []
all_rows = soup.find_all('tr')

for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if len(stat) == 5:
        stats.append(stat)

for item in stats:
    india['Total Cases'] += int(item[2])
    if item[1] == "Maharashtra":
        mah['Total Cases'] = item[2]
        mah['Active Cases'] = int(item[2]) - int(item[3]) - int(item[4])
        mah['Cured'] = item[3]
        mah['Deaths'] = item[4]
    #print(item[0] + ". " + item[1] + " - " + item[2] + ", " + item[3] + ", " + item[4]) 
#print(india)

state = soup.find('table', class_ = 'table table-striped')
#print(state.tbody.text)



response = requests.get("https://api.covid19india.org/state_district_wise.json")
time.sleep(2)
state_data = response.json()
time.sleep(2)
##print(state_data["Maharashtra"]["districtData"]["Mumbai"])
##print(state_data["Maharashtra"]["districtData"]["Pune"])
##print(state_data["Maharashtra"]["districtData"]["Thane"])
##
##time.sleep(2)



print("India: ")
print(india)
print("Maharashtra: ")
print(mah)

district = ["Mumbai", "Pune", "Thane"]
for d in district:
    if d in state_data["Maharashtra"]["districtData"]:
        mah_dist[d] = state_data["Maharashtra"]["districtData"][d]
        del mah_dist[d]['notes']
        print(d + ": ")
        print(mah_dist[d])
        










