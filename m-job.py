from bs4 import BeautifulSoup as bs
import requests
import lxml
import json

url = "http://m-job.ma/recherche?page="

output = []


with open("m-job.json", "w") as f:
    for i in range(1, 4):
        res = requests.get(url+str(i))
        soup = bs(res.text, "lxml")
        for job in soup.find_all("div", {"class": "offer-box"}):
            link = job.find("a")["href"]
            print(link)
            # get request from link
            res = requests.get(link)
            # parse the html
            soup = bs(res.text, "lxml")
            # get the job title
            title = soup.find("h1").text
            # get the job description
            description = soup.find("div", {"class": "the-content"}).text
            # get the job location
            location = soup.find("div", {"class": "location"}).text.strip()
            # get the job type
            l_details = soup.find("ul", {"class": "list-details"})
            company = l_details.findChildren("li")[0].h3.text.strip()
            contract = l_details.findChildren("li")[1].h3.text.strip()
            salary = l_details.findChildren("li")[2].h3.text.strip()
            # get the job date
            date = soup.find("div", {"class": "bottom-content"}).text.replace("L'offre a été publiée il y a", "").replace(" avant sur le site.", "").strip()
            # add the job to the output
            output.append({"title": title, "link": link , "description": description, "location": location, "company": company, "contract": contract, "salary": salary, "date": date})
    json.dump(output, f, indent=4, ensure_ascii=False)
    f.close()




