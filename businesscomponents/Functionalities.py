import properties
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from CommonFunction.Commonfunctions import Commonfunctions
from PageObjects import LoginpageObjects
import os
from selenium import webdriver
import configparser
from jproperties import Properties
from pyjavaproperties import Properties

# from CommonFunction.Commonfunctions import Commonfunctions
from PageObjects.LoginpageObjects import loginPage


class Functionalities(Commonfunctions):
    # p = Properties()
    # with open('properties.txt', "r") as f:
    #     p.load(f, "utf-8")
    # def logintoFacebook(self):
    #     self.getURl(p.read(self,URL))
    #     print(loginPage.EmailOrPhonetextbox)
    #     # self.FindElement(loginPage.EmailOrPhonetextbox.getXpath())


    p = Properties()
    p.load(open('properties.properties'))
    p.list()
    print(p)
    print(p.items())
    print(p['URL'])
    p['name3'] = 'changed = value'

# elem = driver.find_element_by_xpath(self,'')  # Find the search box
#
# elem.send_keys('seleniumhq' + Keys.RETURN)
# # driver.sleep(1000)
# driver.quit()