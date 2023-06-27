from bs4 import BeautifulSoup

html = "<html><head><title>Hello World</title></head><body><h1>BeautifulSoup Example</h1><p>This is an example of BeautifulSoup in action.</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

print(soup.select_one("h1").text.strip())
