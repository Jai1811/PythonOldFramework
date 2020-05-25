from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from businesscomponents import Functionalities
import os
from selenium import webdriver

chromedriver = "D:\downloads chrome\Pythonwebasedapptesting\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")
# driver.quit()

function = Functionalities()




driver.get('https://www.facebook.com/')
driver.maximize_window()
print(driver.title)

# elem = driver.find_element_by_xpath(self,'')  # Find the search box
#
# elem.send_keys('seleniumhq' + Keys.RETURN)
# # driver.sleep(1000)
# driver.quit()