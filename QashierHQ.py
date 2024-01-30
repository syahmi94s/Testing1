from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://hq.qashier.com/#/login")
time.sleep(2)

#enter username password
username = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div/form/label[1]/div/div[1]/div[1]/input").send_keys("syahmi94s@gmail.com")
time.sleep(2)
password = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div/form/label[2]").send_keys("Testing94$")
time.sleep(2)
login = driver.find_element(By.CLASS_NAME, "block")
login.click()
time.sleep(10)

#Add staff
staff = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/aside/div/div/div[6]/div/div/div[1]/div[2]/i").click()
time.sleep(2)
staff2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/aside/div/div/div[6]/div/div/div[2]/div/a[1]/div[3]/div/div").click()
time.sleep(5)
addstaff = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/main/div[4]/div[1]/div[2]/button").click()
time.sleep(2)
name = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/form/div[1]/div/label[1]").send_keys("sarah")
hour = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/form/div[1]/div/label[2]/div/div/div/input").send_keys(20)
id = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/form/div[1]/div/label[3]/div/div[1]/div[1]/input").send_keys(1234)
time.sleep(5)
confirm = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/form/div[2]/button/span[2]").click()
time.sleep(5)

#Check for staff
if driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/main/div[4]/div[2]/table/tbody/tr/td[1]").is_displayed():
    print("Staff added succesfully")
else:
    print("staff not added")

driver.quit()