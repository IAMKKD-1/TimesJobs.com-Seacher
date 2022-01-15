from bs4 import BeautifulSoup
import requests

skill = input("Enter Skill Designation: ")
pref = input("Any prefered location [y/n]: ")
if pref.lower() == 'y':
    location = input("Enter preferred location: ")
else:
    location = ''

link = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={skill.lower().strip()}&txtLocation={location.lower().strip()}'
html_text = requests.get(link)
data = html_text.text

open(f'./Jobs/{skill}-{location}.txt', "w").close()
soup = BeautifulSoup(data, 'lxml')
jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    posted_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in posted_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skills = job.find('span', class_ = 'srp-skills').text.strip().replace('  ','')
        more_info = job.find('ul',class_ = 'list-job-dtl clearfix').li.a['href']

        with open(f'./Jobs/{skill}-{location}.txt','a+') as f:
            f.write(f'Company name: {company_name}\n')
            f.write(f'Required skills: {skills}\n')
            f.write(f'More Info: {more_info}\n')
            f.write('\n\n')
print('File saved')

