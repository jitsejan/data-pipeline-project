import os
import sys
import lxml
from selenium.webdriver.common.by import By


sys.path.append(os.path.abspath(sys.path[0]) + "/../")

from data_crawl.basecrawler import BaseCrawler
import pandas as pd


class CharacterCrawler(BaseCrawler):
    """ Implements the CharacterCrawler class """

    def __init__(self):
        """ Initialize the class """
        super(CharacterCrawler, self).__init__()
        self.url = f"{self.BASE_URL}/characters/"
        self.list_identifier = "div[class='vp-animate']"

    def _get_name(self, elem):
        selector = "h2.txt-color-inherit"
        return self._get_text_from_elem(elem, selector)

    def _get_description(self, elem):
        selector = "div.character-accordion-module--CharacterAccordion__description--"
        return self._get_text_from_elem(elem, selector)

    def _get_image_headshot(self, elem):
        selector = "img.img-headshot"
        return self._get_image_from_elem(elem, selector)

    def _get_image_action(self, elem):
        selector = "img.img-action"
        return self._get_image_from_elem(elem, selector)

    def _get_page_data(self):
        """ Retrieve the data from the page """
        self.browser.get(self.url)
        for elem in self.browser.find_elements(By.CSS_SELECTOR, "div.vp-slide"):
            yield {
                "name": elem.find_element(By.TAG_NAME, "h2").get_attribute("textContent").strip(),
                "description": self._get_description(elem),
                # "image_headshot": self._get_image_headshot(elem),
                # "image_action": self._get_image_action(elem),
                # "copyright": self._get_copyright(tree),
            }

        self.browser.quit()

    def get_data(self):
        """ Get the data and return dataframe """
        frame = pd.DataFrame(self._get_page_data())

        return self._clean_dataframe(frame)
