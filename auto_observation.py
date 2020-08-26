import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import logging
from logging import INFO, getLogger, basicConfig
basicConfig(filename='logger.log', level=logging.INFO)


class auto_observation:
    def __init__(self, wait=2):
        self.wait_time = 2  # 遷移待機
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def watch_start(self, url, interval=20, lim=1000):
        count = 0
        while True:
            self.driver.get(url)
            res = self.driver.find_elements_by_xpath(
                "/html/body/div[2]/div[2]/div[4]/div[5]/div[1]/div[2]/div/div/div/div/div/form/div/div[1]/div/div/div/div[2]/div[5]"
            )
            if len(res) == 0:
                getLogger().info("no switch found")
            else:
                getLogger().info("switch has been found")
            if count > lim:
                break
            time.sleep(interval)
            count += 1

    def quit(self):
        self.driver.quit()
