from charactercrawler import CharacterCrawler
from historycrawler import HistoryCrawler


def main():
    """ Main functionality """
    ccrawler = CharacterCrawler()
    hcrawler = HistoryCrawler()

    print(ccrawler.get_data())
    print(hcrawler.get_data())


if __name__ == "__main__":
    main()
