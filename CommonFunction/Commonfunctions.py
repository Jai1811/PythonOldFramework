from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  Select

import os
from selenium import webdriver

class Commonfunctions(object):

    chromedriver = r"D:\downloads chrome\Pythonwebasedapptesting\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    def getURl(self,URL):
        self.driver.get(URL)

    def getTitle(self):
        self.driver.title

    def maximize(self):
        self.driver.maximize_window()

    def minimize(self):
        self.driver.minimize_window()

    def FindElement(self,Xpath):
        self.driver.find_element_by_xpath(self,Xpath)

    def closebrowser(self):
        self.closebrowser()

    def navigateback(self):
        self.driver.back()

    def navigateforward(self):
        self.driver.forward()

    def  sendkeys(self, xpath, sendvalue):
        self.driver.find_element_by_xpath(xpath).send_keys(sendvalue)

    def click(self, Xpath):
        self.driver.find_element_by_xpath().click()

    def isEnabled(self,xpath):
       boolean= self.driver.find_element_by_xpath(xpath).is_enabled()
       return boolean

    def isDisplayed(self,xpath):
       boolean= self.driver.find_element_by_xpath(xpath).is_displayed()
       return boolean

    def isSelected(self,xpath):
       boolean= self.driver.find_element_by_xpath(xpath).is_selected()
       return boolean

    def clear(self,xpath):
        self.driver.find_element_by_xpath(xpath)

    def selectdropdownvaluebyinex(self,xpath,index):
        driver = webdriver.Chrome("D:\downloads chrome\Pythonwebasedapptesting\chromedriver")
        select = Select(driver.find_element_by_xpath(xpath))
        select.select_by_index(index)


    def selectdropdownvaluebyvalue(self,xpath,text):
        driver = webdriver.Chrome("D:\downloads chrome\Pythonwebasedapptesting\chromedriver")
        select = Select(driver.find_element_by_xpath(xpath))
        select.select_by_visible_text(text)

    def selectdropdownvaluebyvisibletext(self, xpath, text):
        driver = webdriver.Chrome("D:\downloads chrome\Pythonwebasedapptesting\chromedriver")
        select = Select(driver.find_element_by_xpath(xpath))
        select.select_by_visible_text(text)

    def deselectalloptions(self, xpath):
        driver = webdriver.Chrome("D:\downloads chrome\Pythonwebasedapptesting\chromedriver")
        select = Select(driver.find_element_by_xpath(xpath))
        select.deselect_all()

    def allselectedoptions(self, xpath):
        driver = webdriver.Chrome("D:\downloads chrome\Pythonwebasedapptesting\chromedriver")
        select = Select(driver.find_element_by_xpath(xpath))
        options = select.all_selected_options
        return options

    def switchtowindow(self, window):
        self.driver.switch_to_window(window)

    def  switchtoframe(self, frame):
        self.driver.switch_to_frame(frame)

    def switchtodefaultframe(self):
        self.driver.switch_to_default_content()

    def dismisstalert(self):
        self.driver.switch_to_alert().dismiss()

    def acceptalert(self):
        self.driver.switch_to_alert().accept()

    def explicitwait(self,xpath):
        try:

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(xpath))

        finally:
            self.driver.quit()

    def imflicitwait(self,seconds):
        self.driver.implicitly_wait(seconds)

    def fullscreen(self):
        self.driver.fullscreen_window()

    def screenshot(self):
        self.driver.get_screenshot_as_png()

    def savescreenshot(self):
        self.driver.save_screenshot()


