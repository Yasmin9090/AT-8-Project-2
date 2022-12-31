from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class name2():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)

        #username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(4)

        #password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(4)

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

        #personal details tab
        personal_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
        print(driver.find_element(By.XPATH,personal_xpath).accessible_name)
        time.sleep(3)

        #contact details tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a').accessible_name)
        time.sleep(2)

        #emergency contacts tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a').accessible_name)
        time.sleep(2)

        #dependents tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a').accessible_name)
        time.sleep(2)

        #Immigration tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a').accessible_name)
        time.sleep(2)

        #Job tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').accessible_name)
        time.sleep(2)

        #salary tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a').accessible_name)
        time.sleep(2)

        #tax exemption tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a').accessible_name)
        time.sleep(2)

        #Report to tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a').accessible_name)
        time.sleep(2)

        #qualifications tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a').accessible_name)
        time.sleep(2)

        #memberships tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a').accessible_name)
        time.sleep(2)

a=name2()
a.name_password()