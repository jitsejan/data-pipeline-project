from data_crawl.charactercrawler import CharacterCrawler
from data_crawl.historycrawler import HistoryCrawler

from data_storage.minioconnector import MinioConnector

import os

def main():
    """ Main functionality """
    ccrawler = CharacterCrawler()
    hcrawler = HistoryCrawler()
    mc = MinioConnector()

    # Write character data
    characters = ccrawler.get_data()
    print(characters)
    # mc.write_dataframe_to_csv('characters.csv', characters)
    # # Write history data
    # history = hcrawler.get_data()
    # mc.write_dataframe_to_csv('history.csv', history)

if __name__ == "__main__":
    main()
