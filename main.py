import config
import requests
from bs4 import BeautifulSoup
#import lxml
import smtplib


# REQUEST SET-UP
URL = "https://www.amazon.com/neabot-Grooming-Suction-Professional-Clippers/dp/B093KRX2K1/ref=sxin_16_pa_sp_search_thematic_sspa?content-id=amzn1.sym.10e6d77b-0012-4a6b-b8f0-1618f27938ee%3Aamzn1.sym.10e6d77b-0012-4a6b-b8f0-1618f27938ee&crid=21JDMESLCF7NL&cv_ct_cx=dog+vacuum+brush+for+shedding+grooming&keywords=dog+vacuum+brush+for+shedding+grooming&pd_rd_i=B093KRX2K1&pd_rd_r=ee453a0f-0779-4a63-8b89-277f11191bad&pd_rd_w=eyhXN&pd_rd_wg=FUVhS&pf_rd_p=10e6d77b-0012-4a6b-b8f0-1618f27938ee&pf_rd_r=FM9NBTMKKRVY2RD544GJ&qid=1694285464&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=dog+vacuum%2Caps%2C129&sr=1-2-2b34d040-5c83-4b7f-ba01-15975dfb8828-spons&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


# EMAIL SET-UP
MY_EMAIL = config.EMAIL_FROM
TO_EMAIL = config.EMAIL_TO
SMTP = "smtp.gmail.com"
PASSWORD = config.APP_PASS


# CODE
response = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price_whole = float(soup.find(name="span", class_="a-price-whole").getText())
price_cent = float("." + soup.find(name="span", class_="a-price-fraction").getText())
price = price_whole + price_cent

if price < 75:
    with smtplib.SMTP_SSL(SMTP, port=465) as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL,
                            msg=f"Subject:ALERT🚨\n\nDog Vacuum on Amazon is now ${price}!".encode("utf-8"))