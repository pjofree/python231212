# 웹 서버에 요청
import requests
# 크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

# 검색이 용이한 객체
soup = BeautifulSoup(response.text, "html.parser")
posts = soup.find_all("div", attrs = {"class":"card-desc"})

# 파일에 저장
f = open("dangn.txt", "wt", encoding="utf-8")

for post in posts:
    title = post.find("h2", attrs = {"class":"card-title"})
    price = post.find("div", attrs = {"class":"card-price"})
    addr = post.find("div", attrs = {"class":"card-region-name"})
    
    title = title.text.strip().replace("\n", "")
    price = price.text.strip().replace("\n", "")
    addr = addr.text.strip().replace("\n", "")

    print("{0}, {1}, {2}".format(title, price, addr))
    f.write(f"{title}, {price}, {addr}\n")

f.close()



#     <div class="cards-wrap">
#       <article class="card-top ">
#   <a class="card-link " data-event-label="687653900" href="/articles/687653900">
#     <div class="card-photo ">
#         <img alt="냉장고 LG" src="https://dnvefa72aowie.cloudfront.net/origin/article/202312/bb686a6132a93b125b24ec020a0e70bc721b8c45a37314e00e088e1931a8d118.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp" />
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">냉장고 LG</h2>
#       <div class="card-price ">
#         50,000원
#       </div>
#       <div class="card-region-name">
#         광주 북구 운암3동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 8
#           </span>
#         ∙
#         <span>
#             채팅 18
#           </span>
#       </div>
#     </div>