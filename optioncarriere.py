from bs4 import BeautifulSoup as bs
import requests
import lxml
import json

url = "https://www.optioncarriere.ma/emplois-casablanca-113567.html?p="

output = []


with open("optioncarriere.json", "w") as f:
    for i in range(1, 10):
        res = requests.get(url+str(i))
        soup = bs(res.text, "lxml")
        for job in soup.find_all("article", {"class": "job clicky"}):
            link = "https://www.optioncarriere.ma/"+job.find("a")["href"]
            print(link)
            # get request from link
            res = requests.get(link)
            # parse the html
            soup = bs(res.text, "lxml")
            # get the job title
            title = soup.find("h1").text
            # get the job description
            description = soup.find("section", {"class": "content"}).text
            # get the job location
            # add the job to the output
            output.append({"title": title, "link": link , "description": description})
    json.dump(output, f, indent=4, ensure_ascii=False)
    f.close()




