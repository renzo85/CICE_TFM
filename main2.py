import getpass
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import json, requests, ssl, os, logging, getpass, sys
from chromedriver_py import binary_path
from datetime import datetime
import time
import json



def GetCredentials():
    credentials = {}
    credentials['linkedin_user'] = input("Please input your linkedin email: ")
    credentials['linkedin_pwd'] = getpass.getpass("Please input your linkedin pwd (cursor wont move while typing): ")
    return credentials

def open_lkdinweb(credentials, driver):

    driver.get(r"https://www.linkedin.com/home")

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'session_key')))
        element = driver.find_element_by_id('session_key')
        element.send_keys(credentials['linkedin_user'])

        elementb = driver.find_element_by_id('session_password')
        elementb.send_keys(credentials['linkedin_pwd'])
        
        elementc = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button')
        elementc.click()
        time.sleep(2)
        
    except NoSuchElementException:
        pass

    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a/div[2]')))
        return "login_success"

    except NoSuchElementException:
        pass

def open_lkdinprf(driver):

    #click on profile information
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a/div[2]')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a/div[2]')
        element.click()
    
    except NoSuchElementException:
        pass
    
    #click on "see more profile introduction button"
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[4]/section/div/span/button')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[4]/section/div/span/button')
        element.click()
                
    except NoSuchElementException:
        pass

    #extract profile introduction information text
    try:
        elementb = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[4]/section/div')
        profile = elementb.text
        return profile
    except NoSuchElementException:
        pass

def extract_name(driver):

    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section[1]/div[2]/div[2]/div/div[1]/h1')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section[1]/div[2]/div[2]/div/div[1]/h1')
        name = element.text
        return name
    except NoSuchElementException:
        pass


def extract_experience(driver):

    #click on "see more experience button"
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/div/button')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/div/button')
        element.click()
                
    except NoSuchElementException:
        pass

    #extract whole list of job experience
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/ul')))
        #extract len from jobs
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/ul')

        items = element.find_elements_by_tag_name("li")
        a = 1
        job = dict()

        while a <= len(items):

            #see more button, in order to extract job functions in a future version
            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/ul/li[{a}]/section/div/div[1]/div/div/span/button')))
                element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/ul/li[{a}]/section/div/div[1]/div/div/span/button')
                element.click()

            except:
                pass

            job [f"position{a}"] = driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/ul/li[{a}]/section/div/div[1]/a/div[2]/h3").text
            job [f"company{a}"] = driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/ul/li[{a}]/section/div/div[1]/a/div[2]/p[2]").text
            job [f"period{a}"] = driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[1]/section/ul/li[{a}]/section/div/div[1]/a/div[2]/div/h4[1]/span[2]").text
            
            a += 1        
        return job

    except NoSuchElementException:
        pass


def extract_education(driver):

    #click on "see more education button"
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[2]/section/div/button')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[2]/section/div/button')
        element.click()
                
    except NoSuchElementException:
        pass

    #extract whole list of education
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[2]/section/ul')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[2]/section/ul')
        
        items = element.find_elements_by_tag_name("li")
        a = 1
        education = dict()
        
        while a < len(items):

            education [f"institution{a}"] = driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[2]/section/ul/li[{a}]/div/div/div[1]/a/div[2]/div/h3").text
            education [f"program{a}"] = driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[2]/section/ul/li[{a}]/div/div/div[1]/a/div[2]/div/p/span[2]").text
            education [f"period{a}"] = driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[2]/span/div/section/div[2]/section/ul/li[{a}]/div/div/div[1]/a/div[2]/p/span[2]").text

            a += 1

        return education
                
    except NoSuchElementException:
        pass


def extract_skills(driver):

    #click on "see more skills button"
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/button')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/button')
        element.click()
                
    except NoSuchElementException:
        pass

    #extract skills
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/ol')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/ol')
        skills = element.text
        return skills
                
    except NoSuchElementException:
        pass

def extract_sector_knowledge(driver):

    #extract knowledge sector
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/div[1]')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/div[1]')
        knowledge_sector = element.text
        return knowledge_sector
                
    except NoSuchElementException:
        pass

def extract_tools(driver):

    #extract tools
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/div[2]')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/div[2]')
        tools = element.text
        return tools

    except NoSuchElementException:
        pass

def extract_pers_skills(driver):

    #extract personal skills
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/div[3]')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/div[3]')
        perskills = element.text
        return perskills

    except NoSuchElementException:
        pass

def extract_languages(driver):

    #extract languages
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/div[4]')))
        element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div[5]/div[3]/div/section/div[2]/div[4]')
        languages = element.text
        return languages

    except NoSuchElementException:
        pass

    

#### Main #### 

cvdict = {
    "name": "",
    "profile_intro": "",
    "job_experience": "",
    "education": "",
    "skills": "",
    "sector_know": "",
    "tools": "",
    "pers_skills": "",
    "languages": "",
    }


credentials = GetCredentials()
driver = webdriver.Chrome(executable_path=binary_path)
driver.maximize_window()

lknd_ln = open_lkdinweb(credentials, driver)

lknd_pf = open_lkdinprf(driver)
cvdict['profile_intro'] = lknd_pf
lknd_nm = extract_name(driver)
cvdict['name'] = lknd_nm
lknd_jobs = extract_experience(driver)
cvdict['job_experience'] = lknd_jobs
lknd_edu = extract_education (driver)
cvdict['education'] = lknd_edu
lknd_skl = extract_skills (driver)
cvdict['skills'] = lknd_skl
lknd_sknow = extract_sector_knowledge (driver)
cvdict['sector_know'] = lknd_sknow
lknd_tools = extract_tools (driver)
cvdict['tools'] = lknd_tools
lknd_pskl = extract_pers_skills (driver)
cvdict['pers_skills'] = lknd_pskl
lknd_lg = extract_languages (driver)
cvdict ['languages'] = lknd_lg



cvfinal = json.dumps(cvdict, indent=4, ensure_ascii=False)
print (cvfinal)

with open ('cv.txt', 'w') as file:
    file.write(cvfinal)

driver.quit()