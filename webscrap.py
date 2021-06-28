import requests
from bs4 import BeautifulSoup
book_name=(input(""))
url=f"https://www.amazon.in/Kaaval-Kottam/dp/B076G3JLZV/ref=sr_1_3?crid=2B4CW0H1XM59L&dchild=1&keywords={book_name}&qid=1624869987&sprefix=kaaval+%2Caps%2C356&sr=8-3#detailBullets_feature_div"
headers= ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
page=requests.get(url=url,headers=headers)
soup = BeautifulSoup(page.content,'lxml')
c = soup.find("div",id="detailBulletsWrapper_feature_div").text
print(c)
