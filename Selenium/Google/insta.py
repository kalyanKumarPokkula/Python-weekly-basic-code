from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Replace these with your Instagram username and password
username = "username"
password = "password"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the username input field to be present
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

# Enter the username
username_input.send_keys(username)

# Find the password input field
password_input = driver.find_element(By.NAME, "password")

# Enter the password
password_input.send_keys(password)

# Submit the form
password_input.send_keys(Keys.RETURN)

# Wait for the login to complete (you might need to adjust this timing)
# WebDriverWait(driver, 10).until(EC.url_contains("https://www.instagram.com/"))

# Now you are logged in, and you can perform further actions


time.sleep(20)
# Remember to close the browser window when done
driver.quit()
