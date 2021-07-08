from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Controllers import function_login, function_add_patient
from eclipse2.workspace2.Woundtrack import Controllers
import os
import time
import pyautogui

def pin(woundtime): 
    
    #Clicking New Assessment button
    time.sleep(5)
    newa = function_login.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div[2]/button').click()
    
    time.sleep(5)
    
    #Adding of time
    woundtime = function_login.driver.find_element_by_xpath('//*[@id="ti"]').send_keys(woundtime)   
    
    #Plotting of wound pin    
    pyautogui.doubleClick(493, 626)
    time.sleep(5)
    yesbtn = function_login.driver.find_element_by_xpath('//*[@id="coorask"]/div/button[1]').click()


    #Filling out wound parameters 
def parameters():

    #Selecting parameters  
    time.sleep(10)  
    # function_login.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    wlocation = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[3]/span/fieldset/table-inputs/div/div[1]/input').click()
    time.sleep(10)
    wlocationlist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[3]/span/fieldset/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(10)  
    
    
    wtype = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[4]/span/fieldset/table-inputs/div/div[1]/input').click()
    time.sleep(10)
    wtypelist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[4]/span/fieldset/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(10)
    
    
    stages = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[1]/input').click()
    time.sleep(5)
    stageslist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    granulation_tissue = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[1]/input').click()
    time.sleep(5)
    granulationlist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    necrotic_tissue = function_login.driver.find_element_by_xpath('/html/body/section/section/data/section/div/div/div/div/div/div[2]/form/div/fieldset/div/div/div/div/div/div[8]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[1]/input').click()
    time.sleep(5)
    necroticlist = function_login.driver.find_element_by_xpath('/html/body/section/section/data/section/div/div/div/div/div/div[2]/form/div/fieldset/div/div/div/div/div/div[8]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    coverage = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]/span/table-inputs/div/div[1]/input').click() 
    time.sleep(5)
    coveragelist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    xamount = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[1]/input').click()
    time.sleep(5)
    xamountlist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    xtype = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]/span/table-inputs/div/div[1]/input').click()
    time.sleep(5)
    xtypelist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    edges = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]/span/table-inputs/div/div[1]/input').click()
    time.sleep(5)
    edgeslist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    periwound = function_login.driver.find_element_by_xpath('//*[@id="perH"]').click()
    time.sleep(5)
    periwoundlist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]/table-column-periwound/div/div[2]/div[2]/ul/li[1]').click()
    time.sleep(10)
    
    
    healingstat = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]/span/table-inputs/div/div[1]/input').click()
    time.sleep(5)
    healingstatlist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    pain = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]/span/table-inputs/div/div[1]/input').click()
    time.sleep(5)
    painlist = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]/span/table-inputs/div/div[2]/ul/li[2]').click()
    time.sleep(5)
    
    
    other_ob = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[17]/div/textarea').send_keys("Lorem epsum dolor")
    time.sleep(5)
   
    
    
    