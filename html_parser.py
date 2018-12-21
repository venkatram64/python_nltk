from bs4 import BeautifulSoup

html_doc = open('my_html.html', 'r')
soup = BeautifulSoup(html_doc, 'html.parser')

print("Full text from html")
print(soup.get_text())