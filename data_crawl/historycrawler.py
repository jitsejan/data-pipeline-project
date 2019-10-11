import pandas as pd
from data_crawl.basecrawler import BaseCrawler


class HistoryCrawler(BaseCrawler):
    """ Implements the HistoryCrawler class """

    def __init__(self):
        """ Initialize the class """
        self.url = f"{self.BASE_URL}/history/"

    def _get_name(self, elem):
        selector = "h4.history-tile__name"
        return self._get_text_from_elem(elem, selector)

    def _get_year(self, elem):
        selector = "div.history-tile__desc h1.history-tile__yr"
        return self._get_text_from_elem(elem, selector)

    def _get_release_date(self, elem):
        selector = "span.history-tile__date"
        return self._get_text_from_elem(elem, selector).replace("Released: ", "")

    def _get_platform(self, elem):
        selector = "span.history-tile__platform"
        return self._get_text_from_elem(elem, selector)

    def _get_story(self, elem):
        selector = "div.history-tile__story p"
        return " ".join([par.text_content() for par in elem.cssselect(selector)])

    def _get_page_data(self):
        """ Retrieve the data from the page """
        tree = self._get_tree_from_url(self.url)
        for elem in tree.cssselect("div.history-tile"):
            yield {
                "year": self._get_year(elem),
                "name": self._get_name(elem),
                "release_date": self._get_release_date(elem),
                "platform": self._get_platform(elem),
                "story": self._get_story(elem),
                "copyright": self._get_copyright(tree),
            }

    def _clean_dataframe(self, dataframe):
        """ Clean the dataframe """
        columns = ["release_date", "platform"]
        expand_df = dataframe[columns].apply(lambda x: x.str.split("/"))
        result_df = pd.DataFrame.from_items(
            [
                (index, zipped)
                for index, row in expand_df.iterrows()
                for zipped in zip(*row)
            ],
            orient="index",
            columns=expand_df.columns,
        )
        result_df["release_date"] = pd.to_datetime(result_df["release_date"])
        return dataframe.drop(columns, axis=1).join(result_df)

    def get_data(self):
        """ Get the data and return dataframe """
        frame = pd.DataFrame(self._get_page_data())

        return self._clean_dataframe(frame)
