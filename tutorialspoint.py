from pydoc_data.topics import topics
import sre_compile
from bs4 import BeautifulSoup as bs
import requests
import lxml
import json
name = "html"
url = "https://www.tutorialspoint.com/"+name+"/index.htm"

output = {}
course = "Learn "+name.upper()
description = "CSS is a style sheet language used for describing the presentation of a document written in a markup language. CSS is designed to be used by people who are not familiar with HTML or XML, so there is some basic knowledge of the HTML language required to effectively use CSS."
prerequisite = ["HTML"]
lectures = []
parts = 0
with open("tutorialspoint-{"+name+"}.json", "w") as f:
    res = requests.get(url)
    soup = bs(res.text, "lxml")
    topics = soup.find("ul", {"class": "toc chapters"}).findChildren("a")
    topics.pop(0)
    for topic in topics:
        res = requests.get('https://www.tutorialspoint.com' + topic["href"])
        soup = bs(res.text, "lxml")
        
        t = []
        intro = soup.find("div", {"class": "clearer"}).next_sibling;
        title = "Introduction"
        html = ""
        while True:
            if intro.name == "iframe":
                # get iframe data
                _res = requests.get('https://www.tutorialspoint.com' + intro["src"])
                _soup = bs(_res.text, "lxml")
                _html = _soup.find("body")
                _html = str(_html)
                html += _html.strip()
            if intro.name != "iframe":
                html += str(intro)
            if intro.next_sibling is None or intro.next_sibling.name == "h2":
                break
            
            intro = intro.next_sibling
        parts += 1
        if html.strip() != "":
            t.append({"title": title, "html": html})

        for _topic in soup.find_all("h2"):
            title = _topic.text
            html = ""
            while True:
                _topic = _topic.next_sibling
                if _topic is None or _topic.name == "h2":
                    break
                if _topic.name == "iframe":
                    # get iframe data
                    _res = requests.get('https://www.tutorialspoint.com' + _topic["src"])
                    _soup = bs(_res.text, "lxml")
                    _html = _soup.find("body")
                    _html = str(_html)
                    html += _html.strip()
                    print(_html)
                if _topic.name != "iframe":
                    html += str(_topic)
            parts += 1
            t.append({"title": title, "html": html})
        lectures.append({"title": topic.text.replace(name.upper()+" - ", ""), "parts": t})
    output = {"course": course, "description": description, "parts": parts, "prerequisites": prerequisite, "lectures": lectures}
    json.dump(output, f, indent=4, ensure_ascii=False)
    f.close()
    print("Done")
