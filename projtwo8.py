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

#button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(4)

#myinfo tab
        driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewMyDetails"]').click()
        time.sleep(3)

#dependents tab
        driver.find_element(By.XPATH,'//a[text()="Emergency Contacts"]/following::div[1]').click()
        time.sleep(4)

#ADD button
        driver.find_element(By.XPATH,'//h6[text()="Assigned Dependents"]/following::button[1]').click()
        time.sleep(4)

#name
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Ryaan")
        time.sleep(4)

#Relationship
        driver.find_element(By.XPATH,'//label[text()="Relationship"]/following::div[3]').click()
        time.sleep(4)

#dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Child"]').click()
        time.sleep(4)

#DOB
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input').send_keys("2028-12-13")
        time.sleep(4)

# save button
        driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::button[2]').click()
        time.sleep(7)

a=name2()
a.name_password()

