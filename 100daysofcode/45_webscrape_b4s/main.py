from bs4 import BeautifulSoup
import requests
    
response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
    
news = soup.find_all(class_="titleline")
for heading in news:
    print(heading.find(name="a").get("href"))
    print(heading.find(name="a").getText())
    
scores = soup.find_all(class_="score")
for score in scores:
    print(score.getText().split(" ")[0])




# all_anchor_tags = soup.find_all(name="a")
# for article in all_anchor_tags:
#     print(article.getText())


# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.get("href"))
