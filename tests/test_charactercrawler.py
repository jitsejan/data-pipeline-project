import data_crawl

class TestCharacterCrawler:
    """ Defines the tests for the base class for the CharacterCrawler """

    def test_derived_class_get_data_is_called_twice(self, mocker, charactercrawler):
        """ Test if the derived class get data function is called twice """
        mocked_get_data = mocker.patch("data_crawl.charactercrawler.CharacterCrawler.get_data", autospec=True)
        result_one = charactercrawler.get_data()
        result_two = charactercrawler.get_data()

        assert mocked_get_data.call_count == 2
