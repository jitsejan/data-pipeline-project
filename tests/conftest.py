import lxml.html
import os
import pytest
import sys
sys.path.append(os.path.abspath(sys.path[0]) + "/../")
from data_crawl.basecrawler import BaseCrawler
from data_crawl.charactercrawler import CharacterCrawler


@pytest.fixture(scope="session")
def basecrawler():
    return BaseCrawler()


@pytest.fixture(scope="session")
def charactercrawler():
    return CharacterCrawler()


@pytest.fixture(scope="session")
def elem():
    return lxml.html.fromstring("<fake><element></element></fake>")

