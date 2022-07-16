from bs4 import BeautifulSoup as bs
import requests
import lxml
import json

url = "https://m.apkpure.com/discover?page="

output = []

max = 2
with open("output.json", "w") as f:
    precent = 0
    j = 0
    for i in range(1, max+1):
        res = requests.get(url+str(i), headers={'User-Agent': 'Mozilla/5.0'})
        soup = bs(res.text, "lxml")
        jobs_count = len(soup.find_all("li", {"class": "app-item"}))
        # print(jobs_count)
        for job in soup.find_all("li", {"class": "app-item"}):
            link = "https://m.apkpure.com"+job.find("a")["href"]
            # print(link)
            # get request from link
            res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
            # parse the html
            soup = bs(res.text, "lxml")
            # get the job title
            title = soup.find("h1").text
            # get the job description
            description = soup.find("div", {"class": "description"}).text
            download = "https://m.apkpure.com"+job.find("a", {"class": "app-download"})["href"]
            res = requests.get(download, headers={'User-Agent': 'Mozilla/5.0'})
            soup = bs(res.text, "lxml")
            download = soup.find("a", {"id": "download_link"})["href"]
            # get the job location
            # add the job to the output
            output.append({"title": title, "link": link , "description": description, "download":download})
            j += 1
            precent = (j/jobs_count)*100 /max
            print("\r"+str(round(precent, 2))+"%", end="")
    json.dump(output, f, indent=4, ensure_ascii=False)
    f.close()



