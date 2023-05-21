import requests
from bs4 import BeautifulSoup
import pandas as pd
 
url = "https://www.cda.pl/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
 
items = soup.find_all("div", {"class" : "krl-cov krl-cov-th"})
 
# print(items)
 
results = []
 
for item in items:

    image_tag = item.find("img", {"class" : "profile thumb"})
    imageURL = image_tag.get("src")
    title = item.find("span", {"class" : "link-title"}).text.strip()
    premium = item.find("span", {"class" : "flag-video-premium"}).text.strip()
 
    result = {
        "imageURL" : imageURL,
        "title" : title,
        "premium" : premium
    }
 
    results.append(result)
 
df = pd.DataFrame(results)
 
df.to_csv("Flask CDA/CDA/tw.csv", index = False)