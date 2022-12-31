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

#xpath to username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(2)

#xpath to password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(2)

#xpath to login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(4)

#xpath for PIM
        PIM_xpath='//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM=driver.find_element(By.XPATH,PIM_xpath).click()
        time.sleep(4)

#xpath for ADD
        ADD_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        ADD=driver.find_element(By.XPATH,ADD_xpath).click()
        time.sleep(4)

#xpath for FIRSTNAME
        FIRSTNAME_xpath='//input[@placeholder="First Name"]'
        FIRSTNAME=driver.find_element(By.XPATH,FIRSTNAME_xpath).send_keys("Azarudin")
        time.sleep(4)

#xpath for MIDDLENAME
        MIDDLENAME_xpath='//input[@placeholder="Middle Name"]'
        MIDDLENAME=driver.find_element(By.XPATH,MIDDLENAME_xpath).send_keys("Mohamed")
        time.sleep(4)

#xpath for LASTNAME
        LASTNAME_xpath='//input[@placeholder="Last Name"]'
        LASTNAME=driver.find_element(By.XPATH,LASTNAME_xpath).send_keys("Asharaf")
        time.sleep(4)

#xpath for submit
        submit_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit = driver.find_element(By.XPATH, submit_xpath).click()
        time.sleep(7)

#xpath to salary
        driver.find_element(By.XPATH,'//a[text()="Immigration"]/following::div[2]').click()
        time.sleep(4)

#xpath to assigned salary tab
        driver.find_element(By.XPATH,'//h6[text()="Assigned Salary Components"]/following::button[1]').click()
        time.sleep(4)

#xpath to salary component
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Basic Salary")
        time.sleep(4)

#xpath to pay grade
        driver.find_element(By.XPATH,'//label[text()="Pay Grade"]/following::div[3]').click()
        time.sleep(4)

#xpath to Grade1 dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Grade 1"]').click()
        time.sleep(4)

#xpath to pay frequency
        driver.find_element(By.XPATH,'//label[text()="Pay Frequency"]/following::div[3]').click()
        time.sleep(4)

#xpath to frequency dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Monthly"]').click()
        time.sleep(4)

#xpath to Currency tab
        driver.find_element(By.XPATH,'//label[text()="Currency"]/following::div[3]').click()
        time.sleep(4)

#xpath to currency dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="United States Dollar"]').click()
        time.sleep(4)

#xpath to Amount tab
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input').send_keys("55000")
        time.sleep(4)

#xpath to comments tab
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/textarea').send_keys("Salary Amount")
        time.sleep(4)

#xpath to IDDD toggle
        driver.find_element(By.XPATH,'//p[text()="Include Direct Deposit Details"]/following::div[1]').click()
        time.sleep(4)

#xpath to acc number
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input').send_keys("500100234129820")
        time.sleep(4)

#xpath to acc type
        driver.find_element(By.XPATH,'//label[text()="Account Type"]/following::div[3]').click()
        time.sleep(3)

#xpath to Savings dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Savings"]').click()
        time.sleep(3)

#xpath to routing no
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input').send_keys("2345")
        time.sleep(3)

#xpath to Amount tab
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input').send_keys("40000")
        time.sleep(3)

#xpath to save tab
        driver.find_element(By.XPATH,'//label[text()="Amount"]/following::button[2]').click()
        time.sleep(8)

        print("Salary Details has been updated")
a=name2()
a.name_password()
