
from abc import ABCMeta
from urllib.parse import urljoin
from utils import helper_try_except


class GeneralDoc:

    def __init__(self, row):
        self.title = self.scrape_title(row)
        self.authors = self.scrape_authors(row)
        self.citation = self.scrape_citation(row)
        self.topics = self.scrape_topics(row)
        self.pagelink = self.scrape_pagelink(row)
        self.attributes = dict(
            TITLE=self.title,
            AUTHORS=self.authors,
            CITATION=self.citation,
            TOPICS=self.topics,
            PAGE_LINK=self.pagelink
        )

    @helper_try_except
    def scrape_title(self, ele):

        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        name = current_tag.text
        return name

    @helper_try_except
    def scrape_authors(self, ele):
        current_tag = ele.find_elements_by_xpath(
            ".//div[@class='contrib']//descendant::a")
        authors = [j.text for j in current_tag]
        return authors

    @helper_try_except
    def scrape_citation(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='src break-word']")
        citation = current_tag.text
        return citation

    @helper_try_except
    def scrape_topics(self, ele):
        current_tag = ele.find_elements_by_xpath(
            ".//div[@class='topic-evaluation-pane mtm']//descendant::a")
        tags = [j.text for j in current_tag]
        return tags

    @helper_try_except
    def scrape_pagelink(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        href = current_tag.get_attribute("href")
        url = urljoin(ele.parent.current_url, href)
        return url
