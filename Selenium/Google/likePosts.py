from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# username = input("please enter your username : ")
# password = input("please enter your password : ")
username = "username"
password = "password"


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.instagram.com/accounts/login/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

input_element = driver.find_element(By.NAME, "username")
input_element.clear()
input_element.send_keys(username)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

password_element = driver.find_element(By.NAME, "password")
password_element.clear()
password_element.send_keys(password)

password_element.send_keys(Keys.RETURN)


element_with_text = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, '//*[text()="Not Now"]'))
)
# Perform actions on the element
element_with_text.click()


element_with_text1 = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, '//*[text()="Not Now"]'))
)
# Perform actions on the element
element_with_text1.click()

WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Search"]'))
)
# Perform actions on the element
element_with_aria_label = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search"]')
element_with_aria_label.click()

WebDriverWait(driver, 100).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '[aria-label="Search input"]')
    )
)

search_input_element = driver.find_element(
    By.CSS_SELECTOR, '[aria-label="Search input"]'
)

search_input_element.send_keys("avinashavi_282")


WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, '//*[text()="avinashavi_282"]'))
)
# Perform actions on the element
click_input_element = driver.find_element(By.XPATH, '//*[text()="avinashavi_282"]')

click_input_element.click()

time.sleep(5)


WebDriverWait(driver, 200).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_aagu"))
)

click_on_post = driver.find_element(By.CLASS_NAME, "_aagu")
click_on_post.click()

print("clicked post")

# time.sleep(5)

for i in range(30):
    # WebDriverWait(driver, 100).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME, "_aamw"))
    # )

    # driver.find_element(By.CLASS_NAME, "_aamw").click()

    WebDriverWait(driver, 100).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Next"]'))
    )

    driver.find_element(By.CSS_SELECTOR, '[aria-label="Next"]').click()
    # time.sleep(2)


time.sleep(1000)

driver.quit()
