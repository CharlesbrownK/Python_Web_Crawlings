from bs4 import BeautifulSoup

with open("index.html", 'r', encoding = 'UTF-8') as f:
    doc = BeautifulSoup(f, 'html.parser')
    
### 이쁘게 html 원시코드 출력
print(doc.prettify())

### change html tag contents
tag = doc.title
tag.string = "Charles Brown"
print(tag.string)

### find html tag content
tags = doc.find("p") # print first one that is named 'p'
print(tags)
tags = doc.find_all("p") # print all of the 'p' tags
print(tags)

### 찾은 html 태그 중, 0번째 index 값 출력
### html tags indexing
tags = doc.find_all("p")[0]
print(tags)
