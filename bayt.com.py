from bs4 import BeautifulSoup as bs
import requests
import lxml
import json

url = "https://www.bayt.com/en/uae/jobs/?page="

output = []

with open("bayt.json", "w") as f:
    for i in range(1, 3):
        res = requests.get(url+str(i), headers={'User-Agent': 'Mozilla/5.0'})
        soup = bs(res.text, "lxml")
        for job in soup.find_all("li", {"class": "has-pointer-d"}):
            link = "https://www.bayt.com"+job.find("a")["href"]
            print(link)
            # get request from link
            res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
            # parse the html
            soup = bs(res.text, "lxml")
            # get the job title
            title = soup.find("h1", {"class": "h3 t-break"}).text.strip()
             # get the job details
            l_details = soup.find("ul", {"class": "list is-basic t-small"})
            company = l_details.findChildren("li")[0].text.strip()
            try:
                city = l_details.findChildren("li")[1].span.findAll("a")[1].text.strip()
                try:
                    city = l_details.findChildren("li")[1].span.findAll("a")[0].text.strip()
                except:
                    country = "Unknown"
            except:
                city = "Unknown"
            try: country = l_details.findChildren("li")[1].span.findAll("a")[1].text.strip()
            except: country = l_details.findChildren("li")[1].span.findAll("a")[0].text.strip()
            date = l_details.findChildren("li")[2].text.strip()
            l_details = soup.find("dl", {"class": "dlist is-spaced is-fitted t-small"})
            # Industry = l_details.findChildren("dd")[0].text.strip()
            # Find dt where the text is "Contract"
            try: industry = l_details.findAll("dt", text="Company Industry")[0].nextSibling.nextSibling.text.strip()
            except: industry = "Unknown"
            try: companyType = l_details.findAll("dt", text="Company Type")[0].nextSibling.nextSibling.text.strip()
            except: industry = "Unknown"
            try: employmentType = l_details.findAll("dt", text="Employment Type")[0].nextSibling.nextSibling.text.strip()
            except: industry = "Unknown"
            try: monthlySalaryRange = l_details.findAll("dt", text="Monthly Salary Range")[0].nextSibling.nextSibling.text.strip()
            except: industry = "Unknown"
            try: jobRole = l_details.findAll("dt", text="Job Role")[0].nextSibling.nextSibling.text.strip()
            except: jobRole = "Unknown"
            try: numberofVacancies = l_details.findAll("dt", text="Number of Vacancies")[0].nextSibling.nextSibling.text.strip()
            except: numberofVacancies = "Unknown"


            # get the job description
            # description = soup.find("div", {"class": "entry-content"}).text
            # get the job location
            # add the job to the output
            output.append({"title": title, "link": link , "company": company, "city": city, "country": country, "date": date, "industry": industry, "companyType": companyType, "employmentType": employmentType, "monthlySalaryRange": monthlySalaryRange, "jobRole": jobRole, "numberofVacancies": numberofVacancies})
    json.dump(output, f, indent=4, ensure_ascii=False)
    f.close()




