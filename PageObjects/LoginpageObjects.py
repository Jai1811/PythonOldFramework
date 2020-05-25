from enum import Enum

class loginPage(Enum):
    EmailOrPhonetextbox = "//*[@id='email']",
    PassWordtextbox ="//*[@id='pass']",
    loginbutton = "//*[@id='u_0_2']"



    def __init__(self,locator):
        self.locator=locator


    def getXpath(self,locator):

        return locator

