from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)                                        # Its used to keep the browser open after the process has ended.
service=Service(executable_path="give/path/to/your/downloaded/chromedriver.exe")     # Its important to give the path of "chromedriver.exe" file. 
driver =webdriver.Chrome(service=service,options=option)
driver.get("https://quotes.toscrape.com/")

