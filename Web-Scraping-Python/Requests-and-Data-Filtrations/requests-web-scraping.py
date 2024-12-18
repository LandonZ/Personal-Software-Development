from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    #need url and maybe some parameters. Returns html response object
    times_jobs_url = ('https://m.timesjobs.com/mobile/jobs-search-result.html?'
                      'txtKeywords=python&cboWorkExp1=-1&txtLocation=')
    #get the text of the html
    html_text = requests.get(times_jobs_url).text
    #put the html text into BeautifulSoup object
    soup = BeautifulSoup(html_text, 'lxml')

    #get all the jobs from job list
    jobs = soup.find_all('div', class_="srp-listing")

    #loop through all jobs. ONLY WANT JOBS WITH LESS THAN 20 DAYS
    amount_of_days = 20
    #use enumerate so can have index iterating too for job counter
    for index, job in enumerate(jobs):
        # -- FINDING PUBLISHED_DATE --
        # published "days" ago is first word.
        published_date = job.find('span', class_='posting-time').text.split(' ')[0]
        if int(published_date) <= amount_of_days:

            # --  GET COMPANY NAME --
            #company name inside span tag with certain class name.
            #strip the whitespace
            company_name = job.find('span', class_='srp-comp-name').text.strip()
            # -- FINDING KEY SKILLS NEEDED FOR JOB --
            #List of skills
            skills = (job.find('div', class_='srp-keyskills').
                      find_all('a'))
            display_skills = ''
            for skill in skills:
                display_skills += skill.text + ', '
            display_skills = display_skills[:-2].strip()

            # -- GETTING THE LINK FOR EACH JOB --
            # inside the <a> href tag in each div
            # these components are dictionaries. So just call the 'href' key
            more_info = job.a['href']

            # FILTERING OUT JOBS WITH UNFAMILIAR SKILLS
            if unfamiliar_skill not in display_skills:
                #open posts directory and file name of what # post it is.
                with open(f'posts/{index}.txt', 'w') as file:
                    # \n for newline character
                    file.write(f"Company Name: {company_name} \n")
                    file.write(f"Required Skills: {display_skills} \n")
                    file.write(f"Published Date: {published_date} days ago \n")
                    file.write(f"More Info: {more_info}")
                print(f'File saved: {index}')

if __name__ == '__main__':
    # FILTERING OUT UNFAMILIAR SKILLS
    print("Put some skill that you are not familiar with.")
    unfamiliar_skill = input('>')
    print(f"Filtering out {unfamiliar_skill}")
    while True:
        find_jobs()
        #sleep for 10 minutes until run function again
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)