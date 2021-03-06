from templates import GeneralDoc
from utils import helper_try_except, path
import os
import time
from string import punctuation


class FREE(GeneralDoc):
    def __init__(self, driver, row):
        super().__init__(row)
        if os.path.exists(self.clean_title(self.title)+".pdf"):
            print("File Already exists")
        else:
            if self.title:
                self.PDF = self.downloadPDF(driver=driver,
                                            filename=self.title, row=row)
                self.PDF = self.renamePDF(self.PDF, self.title)
                self.attributes["PDF"] = self.PDF
                print()

    def downloadPDF(self, driver, filename, row):
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
            downloaded_file_name = parse(doc.get_attribute("href"))+".pdf"
            if check_name(downloaded_file_name):
                return downloaded_file_name

        return download_file_and_get_name()

    def clean_title(self, title):
        return title.translate(
            {ord(i): ord(" ") for i in punctuation})

    def renamePDF(self, curr_name, title):

        os.rename(os.path.join(path, curr_name),
                  os.path.join(path, self.clean_title(title)+".pdf"))
        return title
