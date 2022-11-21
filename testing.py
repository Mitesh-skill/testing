from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# add Chrome extention  from this https://chromedriver.chromium.org/downloads add file path
driver = webdriver.Chrome(executable_path=("/Users/miteshdilipsarjare/Downloads/chromedriver.exec",chrome_options=chrome_options ))
driver.maximize_window()

driver.get("https://app.skill-edge.com/#/")
# driver.get("https://www.facebook.com/login/")

# time.sleep(90)


driver.find_element(By.ID, "formBasicEmail").send_keys("@gmail.com")
driver.find_element(By.ID, "formBasicPassword").send_keys("Password")

driver.find_element(By.CLASS_NAME, "login-btn btn btn-secondary").click()
