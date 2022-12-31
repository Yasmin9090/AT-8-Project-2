from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class name2():
    def name_password(self):
        driver=webdriver.Chrome()
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

#admin tab
        admin_xpath='//a[@href="/web/index.php/admin/viewAdminModule"]'
        admin=driver.find_element(By.XPATH,admin_xpath).click()
        time.sleep(4)

#user management
        user_management_xpath='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
        usermanagement=driver.find_element(By.XPATH,user_management_xpath).click()
        time.sleep(4)

#users tab
        users_xpath='//a[@href="#"]'
        users=driver.find_element(By.XPATH,users_xpath).click()
        time.sleep(3)

#userrole
        userrole_xpath='//label[text()="User Role"]/following::div[3]'
        userrole=driver.find_element(By.XPATH,userrole_xpath).click()
        time.sleep(3)

#select Admin dropdown
        dropdown_admin_xpath='//div[@role="listbox"]//span[text()="Admin"]'
        drpadmin=driver.find_element(By.XPATH,dropdown_admin_xpath).click()
        time.sleep(3)

#select status
        status_xpath='//label[text()="Status"]/following::div[3]'
        status=driver.find_element(By.XPATH,status_xpath).click()
        time.sleep(3)

#select Enabled dropdown
        dropdown_enabled_xpath='//div[@role="listbox"]//span[text()="Enabled"]'
        drpenabled=driver.find_element(By.XPATH,dropdown_enabled_xpath).click()
        time.sleep(3)

#userrole
        userrole_xpath = '//label[text()="User Role"]/following::div[3]'
        userrole = driver.find_element(By.XPATH, userrole_xpath).click()
        time.sleep(3)

#ESS in the userrole
        ESS_xpath='//div[@role="listbox"]//span[text()="ESS"]'
        ESS=driver.find_element(By.XPATH,ESS_xpath).click()
        time.sleep(3)

#select status
        status_xpath = '//label[text()="Status"]/following::div[3]'
        status = driver.find_element(By.XPATH, status_xpath).click()
        time.sleep(3)

#select Disabled dropdown
        dropdown_disabled_xpath='//div[@role="listbox"]//span[text()="Disabled"]'
        drpdisabled=driver.find_element(By.XPATH,dropdown_disabled_xpath).click()
        time.sleep(3)

a=name2()
a.name_password()
