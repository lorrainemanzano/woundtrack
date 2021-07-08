from selenium import webdriver
from Controllers import function_login
from selenium.webdriver.common.keys import Keys
from eclipse2.workspace2.Woundtrack import Controllers
import os
import time


def add_patient(
        mrn,
        lname,
        fname,
        no_wounds):
    
    newbtn = function_login.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/div/div/button').click()
    time.sleep(5)
    
    mrn = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[1]/td[2]/div/div/input').send_keys(mrn)
    lname = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[2]/td[2]/div/div/input').send_keys(lname)
    fname = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[3]/td[2]/div/div/input').send_keys(fname)
    no_wounds = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[4]/td[2]/div/div/input').send_keys(no_wounds)
    time.sleep(5)
    
    clinicians = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[5]/td[2]/div/div/div[1]/a/span').click()
    clinicians = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[5]/td[2]/div/div/div[1]/div/ul/li[1]').click()
    time.sleep(5)
    
    add_clinician = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[5]/td[2]/button').click()
    time.sleep(5)
    
    clinician1 = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[5]/td[2]/div[2]/div/div[1]').click()
    clinician1 = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[5]/td[2]/div[2]/div/div[1]/div/ul/li[2]').click()
    time.sleep(3)
    
    savebtn = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[3]/div[1]/button').click()
   
    