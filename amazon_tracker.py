import requests
from bs4 import BeautifulSoup
import smtplib

# ------------------------------------------------------- INSTRUCTIONS--------------------------------
# Get The url link of the product you want your bot to check every day
# Use http://myhttpheader.com/ to get the ACCEPT_LANGUAGE and USER_AGENT of your web browser so you can use it as
# you header values

# Use you own email address and password for it and make sure you allow less secure apps on your email account for it to
# it to work

# check the smtp of your email address whether yahoo, gmail or any email services you are using

# Google is smtp.gmail.com
# Yahoo is smtp.mail.yahoo.com
# Outlook is smtp-mail.outlook.com
# -------------------------------------------------------------------------------------------------------

TARGET_PRICE = YOUR_TARGET_PRICE
URL_LINK_PRODUCT = "URL LINK OF THE PRODUCT YOU WANT TO TRACK"
ACCEPT_LANGUAGE = "YOUT ACCEPT LANGUAGE"
USER_AGENT = "YOUR USER AGENT"

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}
response = requests.get(url=URL_LINK_PRODUCT, headers=headers)
amazon_site = response.text

soup = BeautifulSoup(amazon_site, "html.parser")
price_tag = soup.find(name="span", id="priceblock_ourprice").getText().split("$")[1].split(",")
price_figure = float("".join(price_tag))
product_name = soup.find(name="span", id="productTitle").getText().lstrip().rstrip()

if TARGET_PRICE > price_figure:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="YOUR EMAIL", password="YOUR PASSWORD")
        connection.sendmail(from_addr="YOUR EMAIL",
                            to_addrs="RECEIVERS EMAIL ADDRESS",
                            msg=f"Subject: Amazon Tracker\n\n{product_name} is {price_figure} {URL_LINK_PRODUCT}"
                            )
