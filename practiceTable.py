from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import time 

# https://chercher.tech/practice/table

driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")

# driver.get("https://chercher.tech/practice/table")

url = "https://nmtt.gov.in/programs/cesme/PMMMNMTT-2019-100001?type=archived"

driver.get(url)
driver.maximize_window()

ele = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[*]")

print(len(ele))

driver.close()
