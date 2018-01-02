from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the Mend home page
driver.get("https://www.mendfamily.com/")

wait = WebDriverWait(driver, 10)

# find the element with the name attribute name
inputName = driver.find_element_by_name("name")

# type in name
inputName.send_keys("John Doe")

# find the element that's name attribute email
inputEmail = driver.find_element_by_name("email")

# type in email
inputEmail.send_keys("john.doe@abc.com")

# click start button to start the chat
btnStart = driver.find_element_by_class_name("chatlio-btn")

driver.quit()
