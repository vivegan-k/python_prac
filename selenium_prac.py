from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
elem = driver.find_element(By.ID, 'id1')
elem = WebDriverWait(driver, 10).until(EC.element_located_to_be_selected(By.NAME, 'test'))
elem.clear()
elem.send_keys(Keys.RETURN)
driver.close()