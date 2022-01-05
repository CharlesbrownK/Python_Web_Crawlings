from bs4 import BeautifulSoup

with open("index.html", 'r', encoding = 'UTF-8') as f:
    doc = BeautifulSoup(f, 'html.parser')


# tag = doc.find("option")
# tag['color'] = "blue" # tag의 세부정보 변경
# print(tag)
# print(tag.attrs) # tag값을 딕셔너리로 정리

tags = doc.find_all(['option'], value = "Undergraduate")
print(tags)