from selenium import webdriver
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def iOS(device_group, test_runName):
    driver=webdriver.Chrome('../files/chromedriver.exe')
    wait=WebDriverWait(driver, 30)
    wait2=WebDriverWait(driver, 1800)
    driver.maximize_window()
    driver.get('https://cloud.testdroid.com')
    driver.implicitly_wait(90)
    wait.until(EC.visibility_of_element_located((By.ID, "login-email")))
    driver.find_element_by_id('login-email').send_keys('vinayak.kpv@gmail.com')
    driver.find_element_by_id('login-password').send_keys('bitbar@123')
    driver.find_element_by_id('login-submit').click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='iOS Test']")))
    driver.find_element_by_xpath("//a[text()='iOS Test']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@title='Create new test run']")))
    driver.find_element_by_xpath("//div[@title='Create new test run']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Click to choose or upload file')]")))
    time.sleep(4)

    driver.find_element_by_xpath("//button[contains(text(),'Click to choose or upload file')]").click()
    time.sleep(5)
    try:
        
        driver.find_element_by_xpath("//span[text()='match.apk']").click()
        driver.find_element_by_xpath("//a[text()=' Delete']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='Yes']").click()
        time.sleep(10)
    except:
        print "ipa file not present"
    try:
        driver.find_element_by_xpath("//span[text()='tests.zip']").click()
        driver.find_element_by_xpath("//a[text()=' Delete']").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//h3[text()='Delete file'])[2]/../..//button[text()='Yes']").click()
        time.sleep(10)
    except:
        print "zip file not present"
    driver.find_element_by_xpath("//input[@type='file']").send_keys(PATH('../match.apk'))
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Upload file')]")))
    driver.find_element_by_xpath("//input[@type='file']").send_keys(PATH('../tests.zip'))
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Upload file')]")))
    print 'process completed level 1'
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='match.apk']")))
    
    driver.find_element_by_xpath("//span[text()='match.apk']").click()
    time.sleep(3)
    
    action=ActionChains(driver)
    action.key_down(Keys.CONTROL).perform()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='tests.zip']")))
    driver.find_element_by_xpath("//span[text()='tests.zip']").click()
    action.key_up(Keys.CONTROL).perform()
    time.sleep(3)    
    
    
    driver.find_element_by_xpath("//button[text()='Use selected']").click()
    time.sleep(5)
    print 'process completed level 2'

    
    select=Select(driver.find_element_by_xpath("//b[text()='Use existing device group']/..//select"))
    select.select_by_visible_text(device_group)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Click here to expand')]")))
    driver.find_element_by_xpath("//div[contains(text(),'Click here to expand')]").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Test Run X']")))
    time.sleep(2)
    driver.find_element_by_xpath("//input[@placeholder='Test Run X']").clear()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@placeholder='Test Run X']").send_keys(test_runName)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Create new test run']")))
    driver.find_element_by_xpath("//button[text()='Create new test run']").click()
    wait2.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='FINISHED']")))
    
def Android(device_group, test_runName):
    driver=webdriver.Chrome('../files/chromedriver.exe')
    wait=WebDriverWait(driver, 30)
    wait2=WebDriverWait(driver, 1800)
    driver.maximize_window()
    driver.get('https://cloud.testdroid.com')
    driver.implicitly_wait(90)
    wait.until(EC.visibility_of_element_located((By.ID, "login-email")))
    driver.find_element_by_id('login-email').send_keys('vinayak.kpv@gmail.com')
    driver.find_element_by_id('login-password').send_keys('bitbar@123')
    driver.find_element_by_id('login-submit').click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Android Test']")))
    driver.find_element_by_xpath("//a[text()='Android Test']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@title='Create new test run']")))
    driver.find_element_by_xpath("//div[@title='Create new test run']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Click to choose or upload file')]")))
    time.sleep(4)
    
    driver.find_element_by_xpath("//button[contains(text(),'Click to choose or upload file')]").click()
    time.sleep(5)
    try:
        
        driver.find_element_by_xpath("//span[text()='match.apk']").click()
        driver.find_element_by_xpath("//a[text()=' Delete']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='Yes']").click()
        time.sleep(10)
    except:
        print "apk file not present"
    try:
        driver.find_element_by_xpath("//span[text()='tests.zip']").click()
        driver.find_element_by_xpath("//a[text()=' Delete']").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//h3[text()='Delete file'])[2]/../..//button[text()='Yes']").click()
        time.sleep(10)
    except:
        print "zip file not present"
    driver.find_element_by_xpath("//input[@type='file']").send_keys(PATH('../match.apk'))
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Upload file')]")))
    driver.find_element_by_xpath("//input[@type='file']").send_keys(PATH('../tests.zip'))
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Upload file')]")))
    print 'process completed level 1'
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='match.apk']")))
    
    driver.find_element_by_xpath("//span[text()='match.apk']").click()
    time.sleep(3)
    
    action=ActionChains(driver)
    action.key_down(Keys.CONTROL).perform()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='tests.zip']")))
    driver.find_element_by_xpath("//span[text()='tests.zip']").click()
    action.key_up(Keys.CONTROL).perform()
    time.sleep(3)    
    
    
    driver.find_element_by_xpath("//button[text()='Use selected']").click()
    time.sleep(5)
    print 'process completed level 2'
    
    
    select=Select(driver.find_element_by_xpath("//b[text()='Use existing device group']/..//select"))
    select.select_by_visible_text(device_group)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Click here to expand')]")))
    driver.find_element_by_xpath("//div[contains(text(),'Click here to expand')]").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Test Run X']")))
    time.sleep(2)
    driver.find_element_by_xpath("//input[@placeholder='Test Run X']").clear()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@placeholder='Test Run X']").send_keys(test_runName)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Create new test run']")))
    driver.find_element_by_xpath("//button[text()='Create new test run']").click()
    wait2.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='FINISHED']")))
    