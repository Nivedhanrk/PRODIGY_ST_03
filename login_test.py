from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome browser
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Positive Test Case 
def positivelogin():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory" in driver.current_url
    driver.back()

#  Negative Test Case: Wrong Username 
def wrongusername():
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    assert "Epic sadface" in driver.page_source

#  Negative Test Case: Empty Fields
def empty_fields():
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    assert "Epic sadface" in driver.page_source

# Run tests
positive_login()
wrong_username()
empty_fields()

# Close browser
driver.quit()
