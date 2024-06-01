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
driver.find_element(By.LINK_TEXT, "Login").click()                                   #Automatically clicks login 
time.sleep(3)                                                                        #to load the webpage

user=driver.find_element(By.ID,"username")                                          
password=driver.find_element(By.ID,"password")
user.send_keys('admin')                                                              #Automatically types 'admin' in 'username'inputfield
password.send_keys('password')                                                       #Automatically types 'password' in 'password' inputfield
driver.find_element(By.CSS_SELECTOR,"input.btn-primary").click()

#driver.quit()                                                                        # Use it if you want to close webdriver page after complition of automaiton




