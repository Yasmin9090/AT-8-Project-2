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
        MIDDLENAME=driver.find_element(By.XPATH,MIDDLENAME_xpath).send_keys("M")
        time.sleep(4)

        #LASTNAME
        LASTNAME_xpath='//input[@placeholder="Last Name"]'
        LASTNAME=driver.find_element(By.XPATH,LASTNAME_xpath).send_keys("Mohamed")
        time.sleep(4)

        #submit
        submit_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit = driver.find_element(By.XPATH, submit_xpath).click()
        time.sleep(7)

        #nickname
        driver.find_element(By.XPATH,'//label[text()="Nickname"]/following::input[1]').send_keys("Azar")
        time.sleep(3)

        #other ID
        driver.find_element(By.XPATH,'//label[text()="Other Id"]/following::input[1]').send_keys("4156985")
        time.sleep(3)

        #driving licence number
        driver.find_element(By.XPATH,'''//label[text()="Driver's License Number"]/following::input[1]''').send_keys("10002000")
        time.sleep(3)

        #licence expiry date
        driver.find_element(By.XPATH,'//label[text()="License Expiry Date"]/following::input[1]').send_keys("2025-10-25")
        time.sleep(3)

        #SSN number
        driver.find_element(By.XPATH,'//label[text()="SSN Number"]/following::input[1]').send_keys("5000")
        time.sleep(3)

        #SIN number
        driver.find_element(By.XPATH,'//label[text()="SIN Number"]/following::input[1]').send_keys("2000")
        time.sleep(3)

        #Nationality
        driver.find_element(By.XPATH,'//label[text()="Nationality"]/following::div[2]').click()
        time.sleep(3)

        #Indian
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Indian"]').click()
        time.sleep(3)

        #Marital status
        driver.find_element(By.XPATH,'//label[text()="Marital Status"]/following::div[3]').click()
        time.sleep(3)

        #Married
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Married"]').click()
        time.sleep(3)

        #DOB
        driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::input[1]').send_keys("1992-05-03")
        time.sleep(3)

        #Gender
        driver.find_element(By.XPATH,'//label[text()="Gender"]/following::span[1]').click()
        time.sleep(3)

        #Military service
        service=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input').send_keys("No")
        time.sleep(3)

        #smoker
        driver.find_element(By.XPATH,'//label[text()="Smoker"]/following::i[1]').click()
        time.sleep(3)

        #save
        driver.find_element(By.XPATH,'//label[text()="Military Service"]/following::button[1]').click()
        time.sleep(6)

        #blood group
        driver.find_element(By.XPATH,'//label[text()="Blood Type"]/following::div[3]').click()
        time.sleep(3)

        #AB+
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="AB+"]').click()
        time.sleep(3)

        #save
        driver.find_element(By.XPATH,'//label[text()="Military Service"]/following::button[2]').click()
        time.sleep(5)
        print("Successfully created")

a=name2()
a.name_password()