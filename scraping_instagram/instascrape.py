# -*- coding: utf-8 -*-
import os
import sys
sys.excepthook = sys.__excepthook__
from random import randrange
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
from time import sleep


#import username and password for insta  or can be modified to be read from command line

USER = 'username'
SECRET_PASS = 'password'

    def __init__(self,user,pw):
        self.user = user
        self.actionChains = ActionChains
        #self.firefox = webdriver.Firefox()

        profile = webdriver.FirefoxProfile()

        #add geo location setting to a differnt lat long
        profile.set_preference("geo.prompt.testing", True)
        profile.set_preference("geo.prompt.testing.allow", True)
        profile.set_preference("geo.provider.testing", True)
      
        profile.set_preference("geo.provider.network.url", 'data:application/json,{"location": {"lat": 6.589, "lng": 106.84}, "accuracy": 27000.0}')


