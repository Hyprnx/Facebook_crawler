import time

from base import BaseClass
from datetime import date, timedelta
from push_to_mongodb import *
from selenium import webdriver

from resources.clone_acc import clone_acc
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from profile_extractor import ProfileExtractor
from time import sleep
import random


class FacebookAccountGenerator(BaseClass):
    def __init__(self, headless: bool = False):
        super().__init__()
        try:
            self.current_tab = 0
            options = Options()
            self.log.info("Setting headless options")
            options.headless = headless
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("detach", True)
            self.log.info("Initialize Chrome Driver")
            self.driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)

        except BaseException as e:
            self.log.critical(e)
            self.log.info('Initialize failed, aborting')
            self.driver.quit()

    def _open_new_tab(self, url='https:google.com'):
        self.driver.execute_script(f"window.open(\"{url}\",'newTab_{self.current_tab}');")
        self.current_tab += 1
        return self

    def _switch(self, tab_num):
        self._open_new_tab()
        self.driver.switch_to.window(self.driver.window_handles[tab_num])


    def get_random(self):
        self.driver.get('https://10minutemail.com/')
        self._switch(1)
        self.driver.get('https://www.geeksforgeeks.org/')

    def _reg_facebook(self):
        self._switch(0)
        return self


def main():
    generator = FacebookAccountGenerator(headless=False)
    generator._open_new_tab()
    generator._open_new_tab()
    generator._open_new_tab()
    generator._open_new_tab()
    generator._open_new_tab()
    #
    # for i in range(4):
    #     generator._switch(i)
    #     sleep(3)


if __name__ == '__main__':
    main()



