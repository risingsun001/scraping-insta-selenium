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
