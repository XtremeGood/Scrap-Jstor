from urllib.parse import urljoin
from templates import GeneralDoc
from utils import helper_try_except, path
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
from string import punctuation

class FREE(GeneralDoc):
    def __init__(self, driver, row):
        super().__init__(row)
        
        if self.title:
            self.PDF = self.self.makePDF(driver=driver,
                                    filename=self.title, row=row)
            self.attributes["PDF"] = self.renamePDF(self.PDF)

    def makePDF(self, driver, filename, row):
        def parse(string):
            return string.split(".pdf?")[0].split("/")[-1]

        def check_name(downloaded_file_name):
            while not os.path.exists(
                    os.path.join(path, downloaded_file_name)):
                time.sleep(1)
            else:
                return True

        @helper_try_except
        def download_file_and_get_name():
            doc = row.find_element_by_xpath(
                ".//a[@class='pdfLink button']")
            doc.click()
            return parse(doc.get_attribute("href"))+".pdf"

        return download_file_and_get_name()

    def renamePDF(self, curr_name, title):
        os.rename(os.path.join(path, curr_name), os.path.join(path, title))
        return title+".pdf"