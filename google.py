from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# cap = DesiredCapabilities.FIREFOX.update({["platform"] :"LINUX"}    )
binary = FirefoxBinary("/Users/sandeep/Downloads/geckodriver")
#driver = webdriver.Chrome(executable_path='/Users/sandeep/Downloads/chromedriver')
driver = webdriver.Remote(command_executor='localhost/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)

driver.get("https://www.google.com")
time.sleep(5)
ele = driver.find_element(By.XPATH, '//*[@href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/"]')
f = open("/Testing.txt", "w+")
if ele.is_displayed() == True :
    f.write(" PASS ")
else:
    f.write(" FAIL ")

f.close()

driver.quit()

