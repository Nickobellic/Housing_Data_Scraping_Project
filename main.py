import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

GOOGLE_FORMS_URL = "created_google_form_link"
GOOGLE_CHROME_DRIVER = r"chromedriver.exe_file_directory"

driver = webdriver.Chrome(service=Service(GOOGLE_CHROME_DRIVER))

access = requests.get(url="https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.61473855379776%2C%22north%22%3A37.93549644337129%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accepted-Language': 'en-US,en;q=0.9', 'Connection':'keep-alive', 'Cookie':'PHPSESSID=trgop3geu13sveegd6f8u87hj2'}).content
price = []
address = []
links = []
soup = BeautifulSoup(access, 'html.parser')
price_scrape = soup.select('span[data-test="property-card-price"]') # ul li article div div div span[data-test="property-card-price"]
address_scrape = soup.select('address[data-test="property-card-addr"]')
link_scrape = soup.select('a[data-test="property-card-link"]')
for i in price_scrape:
    price.append(i.text[0:6])
for i in address_scrape:
    address.append(i.text)
for i in link_scrape:
    links.append(f"https://www.zillow.com{i.get('href')}")

for i in range(len(price)):
    driver.get(GOOGLE_FORMS_URL)
    add = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add.send_keys(address[i])
    pri = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pri.send_keys(price[i])
    lin = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    lin.send_keys(links[i])
    submit = driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
    submit.click()
    time.sleep(2)






