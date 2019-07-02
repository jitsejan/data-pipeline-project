import os
import sys

sys.path.append(os.path.abspath(sys.path[0]) + "/../")

from data_crawl.basecrawler import BaseCrawler
import pandas as pd


class CharacterCrawler(BaseCrawler):
    """ Implements the CharacterCrawler class """

    def __init__(self):
        """ Initialize the class """
        self.url = f"{self.BASE_URL}/characters/"
        self.list_identifier = "ul.characters li.characters__item"

    def _get_name(self, elem):
        selector = "h2.characters__name"
        return self._get_text_from_elem(elem, selector)

    def _get_description(self, elem):
        selector = "p.characters__description"
        return self._get_text_from_elem(elem, selector)

    def _get_image_headshot(self, elem):
        selector = "img.img-headshot"
        return self._get_image_from_elem(elem, selector)

    def _get_image_action(self, elem):
        selector = "img.img-action"
        return self._get_image_from_elem(elem, selector)

    def _get_page_data(self):
        """ Retrieve the data from the page """
        tree = self._get_tree_from_url(self.url)
        for elem in tree.cssselect(self.list_identifier):
            yield {
                "name": self._get_name(elem),
                "description": self._get_description(elem),
                "image_headshot": self._get_image_headshot(elem),
                "image_action": self._get_image_action(elem),
                "copyright": self._get_copyright(tree),
            }

    def get_data(self):
        """ Get the data and return dataframe """
        frame = pd.DataFrame(self._get_page_data())

        return self._clean_dataframe(frame)
