from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from eclipse2.workspace2.Woundtrack import Controllers
import os
import time

#configure webdriver
chromedriver = os.path.abspath("chromedriver.exe")
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
#use driver to redirect to a website
driver.get("https://app2.woundtrack.com/login")

def login(
        usern,
        userpass):
    
    usern = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/div[2]/form/div[1]/div/input').send_keys(usern)
    userpass = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/div[2]/form/div[2]/div/input').send_keys(userpass)
    time.sleep(2)
    submitbtn = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/div[2]/form/button').click()
    time.sleep(5)
    

    
    
    
    