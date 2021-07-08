from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Controllers import function_login, function_add_patient, function_assessment
from eclipse2.workspace2.Woundtrack import Controllers
import os
import time
import pyautogui
import autoit


def digital ():

    wound_image = function_login.driver.find_element_by_xpath('//*[@id="myImg"]').click()
    time.sleep(5)
    
    
        