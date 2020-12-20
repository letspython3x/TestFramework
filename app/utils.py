"""
Created on Sat Dec 19 10:00:00 2020
@author: Priya Garg
"""
from selenium import webdriver

# CONSTANTS
URL = r'https://www.saucedemo.com/'
CHROMEDRIVER_PATH = 'chromedriver.exe'
DOWNLOAD_FOLDER = "download"


def get_browser():
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": DOWNLOAD_FOLDER}
    chromeOptions.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                               options=chromeOptions)
    browser.set_window_size(1000, 1000)
    return browser
