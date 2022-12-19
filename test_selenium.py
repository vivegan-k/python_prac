from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("www.google.com")
driver.implicitly_wait(20)
assert 'Google' in driver.title
elem = driver.find_element(By.NAME, 'Search')
elem.clear()
elem.send_keys('Text to search')
elem.send_keys(Keys.RETURN)
element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")
element = WebDriverWait(driver, 10).until(EC.element_located_to_be_selected)
driver.close()