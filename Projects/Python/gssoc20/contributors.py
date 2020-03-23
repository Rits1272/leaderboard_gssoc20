from project_list import links
import requests
from bs4 import BeautifulSoup as bs
import pprint

print(links)
extract_part = []
for i in links:
    extract = i.split('/')[-2] + '/' + i.split('/')[-1]
    extract_part.append(extract)

total_projects = len(extract_part)
counter = 0

for e_part in extract_part:
    counter += 1
    URL = f'https://api.github.com/repos/{e_part}/stats/contributors'
    page = requests.get(URL).json()

    print("Fetching contributors for : ",e_part)
    done = round((counter/total_projects)*100)
    print(f"{done}% done")
    f = open('gssoc_peeps.txt', 'a')
    for i in page:
        try:
            f.write(i['author']['login'])
        except:
            print("ERROR FETCHING -> ", e_part)
        f.write('\n')
    f.close()