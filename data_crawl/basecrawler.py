""" data_crawl/basecrawler.py """
import lxml.html
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseCrawler:
    """ Implements the BaseCrawler class """

    BASE_URL = "https://mario.nintendo.com"
    DRIVER_PATH = "/Users/jitsejan/.wdm/drivers/geckodriver/macos/v0.30.0/geckodriver"


    def __init__(self):
        self._browser = webdriver.Firefox(executable_path=self.DRIVER_PATH)  

    def _get_page_data(self):
        """ Retrieve the data from the page """
        raise NotImplementedError

    def _get_image_from_elem(self, elem, selector):
        """ Retrieve the image from a selector """
        return self.BASE_URL + elem.cssselect(selector)[0].get("src")

    def get_data(self):
        """ Get the data and return dataframe """
        raise NotImplementedError("get_data() is not implemented")

    def _get_copyright(self, elem):
        selector = "div.footer-main__links__legal p"
        return self._get_text_from_elem(elem, selector)

    def _get_text_from_elem(self, elem, selector):
        """ Retrieve the text from a selector """
        selected_text = self._get_selector(elem, selector)
        print(dir(selected_text))
        return selected_text.text if selected_text else None

    @property
    def browser(self):
        return self._browser

    @staticmethod
    def _get_tree_from_url(url):
        resp = requests.get(url)
        return lxml.html.fromstring(resp.content)

    @staticmethod
    def _clean_dataframe(dataframe):
        """ Clean the dataframe """
        return dataframe

    @staticmethod
    def _get_selector(elem, selector):
        """ Retrieve the selector from an element """
        return elem.find_element(By.CSS_SELECTOR, selector)
