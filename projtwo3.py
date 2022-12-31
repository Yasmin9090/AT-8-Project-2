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

        #create details toggle
        createdetails_xpath='//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]'
        toggle=driver.find_element(By.XPATH,createdetails_xpath).click()
        time.sleep(4)

        #username
        username_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        name=driver.find_element(By.XPATH,username_xpath).send_keys("Azarudin Mohamed Asharaf")
        time.sleep(5)

        #Radio button
        radio_button_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        radio=driver.find_element(By.XPATH,radio_button_xpath).click()
        time.sleep(3)

        #password
        pwrd_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
        pwrd=driver.find_element(By.XPATH,pwrd_xpath).send_keys("Guvi@123456")
        time.sleep(3)

        #confirm password
        cnfm_pwrd_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
        cnfmpwrd=driver.find_element(By.XPATH,cnfm_pwrd_xpath).send_keys("Guvi@123456")
        time.sleep(4)

        #submit
        submit_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit=driver.find_element(By.XPATH,submit_xpath).click()
        time.sleep(4)

        print("New Employee Record has been Created")
a=name2()
a.name_password()