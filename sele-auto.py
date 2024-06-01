import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
service=Service(executable_path="C:/Users/kumar/PycharmProjects/pythonProject/venv/selenium/chromedriver.exe")
driver =webdriver.Chrome(service=service,options=option)
driver.get("https://quotes.toscrape.com/")
#hall_input = driver.find_element(By.ID, "htno")
#hall_input.send_keys(4196030130)

#degree_select = Select(driver.find_element(By.ID, "Degree"))
#degree_select.select_by_value("b")  

#submit_button = driver.find_element(By.ID, "btnsubmit")
#submit_button.click()


