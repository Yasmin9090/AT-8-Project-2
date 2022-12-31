from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class name2():
    def name_password(self):
        driver=webdriver.Edge()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)

#username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(2)

#password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(2)

#login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(4)

#PIM
        PIM_xpath='//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM=driver.find_element(By.XPATH,PIM_xpath).click()
        time.sleep(4)

#ADD
        ADD_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        ADD=driver.find_element(By.XPATH,ADD_xpath).click()
        time.sleep(4)

#FIRSTNAME
        FIRSTNAME_xpath='//input[@placeholder="First Name"]'
        FIRSTNAME=driver.find_element(By.XPATH,FIRSTNAME_xpath).send_keys("Azarudin")
        time.sleep(4)

#MIDDLENAME
        MIDDLENAME_xpath='//input[@placeholder="Middle Name"]'
        MIDDLENAME=driver.find_element(By.XPATH,MIDDLENAME_xpath).send_keys("Mohamed")
        time.sleep(4)

#LASTNAME
        LASTNAME_xpath='//input[@placeholder="Last Name"]'
        LASTNAME=driver.find_element(By.XPATH,LASTNAME_xpath).send_keys("Asharaf")
        time.sleep(4)

#submit
        submit_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit = driver.find_element(By.XPATH, submit_xpath).click()
        time.sleep(7)

#job tab
        driver.find_element(By.XPATH,'//a[text()="Immigration"]/following::div[1]').click()
        time.sleep(4)

#joined date
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("2018-04-11")
        time.sleep(4)

#job title
        driver.find_element(By.XPATH,'//label[text()="Job Title"]/following::div[3]').click()
        time.sleep(4)

#job title1
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Account Assistant"]').click()
        time.sleep(4)

#job cat header
        driver.find_element(By.XPATH,'//label[text()="Job Category"]/following::div[3]').click()
        time.sleep(4)

#job category
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Craft Workers"]').click()
        time.sleep(4)

#subunit header
        driver.find_element(By.XPATH,'//label[text()="Sub Unit"]/following::div[3]').click()
        time.sleep(4)

#subunit dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Administration"]').click()
        time.sleep(4)

#location header
        driver.find_element(By.XPATH,'//label[text()="Location"]/following::div[3]').click()
        time.sleep(4)

#location dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="New York Sales Office"]').click()
        time.sleep(4)

#emp status header
        driver.find_element(By.XPATH,'//label[text()="Employment Status"]/following::div[3]').click()
        time.sleep(4)

#emp status dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Full-Time Contract"]').click()
        time.sleep(4)

#ECD toggle
        driver.find_element(By.XPATH,'//label[text()="Employment Status"]/following::div[7]').click()
        time.sleep(4)

#contract startdate
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input').send_keys("2020-02-10")
        time.sleep(4)

#contract enddate
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input').send_keys("2022-02-15")
        time.sleep(4)

#save button
        driver.find_element(By.XPATH,'//label[text()="Contract Details"]/following::button[1]').click()
        time.sleep(4)

a=name2()
a.name_password()
