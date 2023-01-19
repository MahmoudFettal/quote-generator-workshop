import requests
import json
import re

from bs4 import BeautifulSoup
from unidecode import unidecode

data = requests.get("https://www.codeitbro.com/best-quotes-about-software-development/")
soup = BeautifulSoup(data.text, "html.parser")

# defining regex and extraction functions
quote_expression = re.compile(r"\".+\"")
author_expression = re.compile(r"- .+")

author = lambda x: author_expression.findall(x)[-1][2:].replace("- ", "").split("\"")[-1].strip() if author_expression.findall(x) else "Anonymous"
quote  = lambda x: quote_expression.findall(x)[0].replace("\"", "").strip() if quote_expression.findall(x) else "Nothing"

# extracting the quotes
quotes = soup.find_all("p").copy()
quotes = [i.findAll(text=True) for i in quotes if len(i.findAll('strong')) == 1]
#quotes = [unidecode(i[1]) for i in quotes if i[0].isdigit()]
#quotes = [{"quote": quote(i), "author": author(i)} for i in quotes]

#with open("tech_quotes.json", "w", encoding="utf-8") as file:
#    json.dump(quotes, file)
