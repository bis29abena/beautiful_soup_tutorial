from bs4 import BeautifulSoup

with open("website.html") as files:
    content = files.read()

soup = BeautifulSoup(content, "html.parser")
# # This provides a list
# paragraph_tags = soup.find_all(name="p")
# # This also provides a list
# anchor_tags = soup.find_all(name="a")
#
# for tags in anchor_tags:
#     # Getting the text of the tags.
#     print(tags.getText())
#     # Getting the values of any of the attributes
#     print(tags.get("href"))

# finds the tags with a specific (id attribute) with its value
# heading = soup.findAll(name="h1", id="name")
# print(heading[0].getText())

# finds the tags with a specific (class attribute) with its value
# heading3 = soup.find(name="h3", class_="heading")
# print(heading3.getText())

# Using selectors
# select = soup.select(selector="p em")
# print(select[0].getText())

# using selectors for class
# select = soup.select_one(selector=".heading")
# print(select)

# using selectors for id
# select = soup.select_one(selector="#name")
# print(select)