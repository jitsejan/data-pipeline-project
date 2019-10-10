import data_crawl

class TestCharacterCrawler:
    """ Defines the tests for the base class for the CharacterCrawler """

    def test_derived_class_get_data_is_called_twice(self, mocker, charactercrawler):
        """ Test if the derived class get data function is called twice """
        mocked_get_data = mocker.patch("data_crawl.charactercrawler.CharacterCrawler.get_data", autospec=True)
        result_one = charactercrawler.get_data()
        result_two = charactercrawler.get_data()

        assert mocked_get_data.call_count == 2

    def test_init_url_is_set(self, charactercrawler):
        """ Test that the URL is set during init """
        expected = "https://mario.nintendo.com/characters/"
        actual = charactercrawler.url

        assert expected == actual

    def test_init_list_identifier_is_set(self, charactercrawler):
        """ Test that the list identifier is set during init """
        expected = "ul.characters li.characters__item"
        actual = charactercrawler.list_identifier

        assert expected == actual

    # def test_get_name_returns_correct_value(self):
    #     """ Test that the _get_name() function returns the right value """

    # def test_get_description_returns_correct_value(self):
    #     """ Test that the _get_description() function returns the right value """

    # def test_get_image_headshot_returns_correct_value(self):
    #     """ Test that the _get_image_headshot() function returns the right value """

    # def test_get_image_action_returns_correct_value(self):
    #     """ Test that the _get_image_action() function returns the right value """

    # def test_get_page_data_returns_correct_value(self):
    #     """ Test that the _get_page_data() function returns the right value """

    # def test_get_data_returns_correct_value(self):
    #     """ Test that the get_data() function returns the right value """