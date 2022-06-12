from bs4 import BeautifulSoup as bs
import requests
import lxml
import json

url = "https://www.dreamjob.ma/emploi/page/"

output = []


with open("output.json", "w") as f:
    for i in range(1, 2):
        res = requests.get(url+str(i))
        soup = bs(res.text, "lxml")
        for job in soup.find_all("article", {"class": "jeg_post"}):
            link = job.find("a")["href"]
            # get request from link
            res = requests.get(link)
            # parse the html
            soup = bs(res.text, "lxml")
            # get the job title
            title = soup.find("h1", {"class": "jeg_post_title"}).text
            # get the job description
            description = soup.find("div", {"class": "entry-content"}).text
            # get the job location
            # add the job to the output
            output.append({"title": title, "link": link , "description": description})
    json.dump(output, f, indent=4, ensure_ascii=False)
    f.close()


