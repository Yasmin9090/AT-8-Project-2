from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class name2():
    def name_password(self):
        driver=webdriver.Edge()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        time.sleep(3)
        driver.maximize_window()
        time.sleep(3)

#username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(3)

#password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(3)

#login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(5)

#myinfo tab
        driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewMyDetails"]').click()
        time.sleep(3)

#Emergency contact details tab
        driver.find_element(By.XPATH,'//a[text()="Contact Details"]/following::div[1]').click()
        time.sleep(4)

#Assigned emergency details
        driver.find_element(By.XPATH,'//h6[text()="Assigned Emergency Contacts"]/following::button[1]').click()
        time.sleep(4)

#name
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Ayaan")
        time.sleep(4)

#Relationship
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("Friend")
        time.sleep(4)

#home telephone
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input').send_keys("147852963")
        time.sleep(4)

#mobile
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input').send_keys("9874155879")
        time.sleep(4)

#work telephone
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input').send_keys("5698746546")
        time.sleep(4)

#save
        driver.find_element(By.XPATH,'//label[text()="Mobile"]/following::button[2]').click()
        time.sleep(6)


a=name2()
a.name_password()
