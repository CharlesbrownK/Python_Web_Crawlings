from bs4 import BeautifulSoup

with open("index.html", 'r', encoding = 'UTF-8') as f:
    doc = BeautifulSoup(f, 'html.parser')
    
### 이쁘게 html 원시코드 출력
print(doc.prettify())

### html 태그 내용 변경
### change contents of html
tag = doc.title
tag.string = "김정훈"
print(tag.string)

### html 태그 내용 찾기
### find html tags contents
tags = doc.find("p") # 태그 p라는 이름을 가진 첫 번째 태그 출력 / print first one that called 'p' tag
print(tags)
tags = doc.find_all("p") # 태그 p라는 이름을 가진 모든 태그 출력 / print all of the tag 'p'
print(tags)

### 찾은 html 태그 중, 0번째 index 값 출력
### html tags indexing
tags = doc.find_all("p")[0]
print(tags)

