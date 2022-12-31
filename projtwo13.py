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

#xpath to emp name search
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("Azarudin")
        time.sleep(4)

#xpath to search button
        driver.find_element(By.XPATH,'//label[text()="Sub Unit"]/following::button[2]').click()
        time.sleep(6)

#xpath to click alice account
        driver.find_element(By.XPATH,'//div[text()="0271"]/following::div[1]').click()
        time.sleep(5)

#xpath to Taxexemptions tab
        driver.find_element(By.XPATH,'//a[text()="Tax Exemptions"]').click()
        time.sleep(4)

#xpath to status tab
        driver.find_element(By.XPATH,"//h6[text()='Federal Income Tax']/following::div[7]").click()
        time.sleep(4)

#xpath to dropdown to status
        driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Married"]').click()
        time.sleep(4)

#xpath to Exemptions tab
        driver.find_element(By.XPATH,"//h6[text()='Federal Income Tax']/following::input[1]").send_keys("12")
        time.sleep(4)

#xpath to state tab
        driver.find_element(By.XPATH,"//h6[text()='State Income Tax']/following::div[7]").click()
        time.sleep(4)

#xpath to state dropdown
        driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Arkansas"]').click()
        time.sleep(4)

#xpath to status tab
        driver.find_element(By.XPATH,"//label[text()='State']/following::div[9]").click()
        time.sleep(4)

#xpath to status dropdown
        driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Married"]').click()
        time.sleep(4)

#xpath to exemptions tab
        driver.find_element(By.XPATH,"//label[text()='State']/following::input[1]").send_keys("22")
        time.sleep(4)

#xpath to unemployement state
        driver.find_element(By.XPATH,"//label[text()='Unemployment State']/following::div[1]").click()
        time.sleep(4)

#xpath to unemployement dropdown
        driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Armed Forces Europe"]').click()
        time.sleep(3)

#xpath to work state
        driver.find_element(By.XPATH,"//label[text()='Work State']/following::div[1]").click()
        time.sleep(3)

#xpath to work state dropdown
        driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Armed Forces Europe"]').click()
        time.sleep(3)

#xpath to save button
        driver.find_element(By.XPATH,"//label[text()='Work State']/following::button[1]").click()
        time.sleep(6)

        print("Successfully updated")
a=name2()
a.name_password()
