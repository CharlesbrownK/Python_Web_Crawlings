from bs4 import BeautifulSoup
import requests

url = "https://bit.ly/3pQaG7L"

result = requests.get(url)
doc = BeautifulSoup(result.content.decode('utf-8', 'replace'), "html.parser")

prices = doc.find_all(text = "$")
parents = prices[0].parent
answer = parents.strong
print(answer.string)
