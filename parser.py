import re
from urllib.parse import urlsplit
import pandas as pd
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/home/elias/PycharmProjects/DOU_email_parser/chromedriver')
url = 'https://jobs.dou.ua/companies/?name=%D0%97%D0%B0%D0%BF%D0%BE%D1%80%D0%BE%D0%B6%D1%8C%D0%B5'
browser.get(url)
element = browser.find_element_by_link_text("Больше компаний")
while element:
    try:
        wait = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.LINK_TEXT, 'Больше компаний')))
        element.click()
    except ElementNotInteractableException:
        break

offices_links = []

for office in browser.find_elements_by_link_text('Офисы'):
    offices_links.append(office.get_attribute('href'))

browser.quit()

email_list = set()
base_email = []
for emails in offices_links:
    http = urllib3.PoolManager()
    url = emails
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features="lxml")
    for link in soup.findAll('a', attrs={'href': re.compile("mailto")}):
        if link.get('href') != 'mailto:support@dou.ua':
            parts = urlsplit(link.get('href'))
            base_email.append("{0.path}".format(parts))
            email_list.update(base_email)
df = pd.DataFrame(email_list, columns=["Email"])
df.to_csv('email.csv', index=False)
