import lxml.html
import os
import pytest
import sys

import data_crawl

class TestBaseCrawler:
    """ Defines the tests for the base class for the BaseCrawler """

    def test_base_url(self, basecrawler):
        """ Test the base URL of the crawler """
        expected = "https://mario.nintendo.com"
        actual = basecrawler.BASE_URL

        assert expected == actual

    def test_base_class_no__get_page_data_implemented(self, basecrawler):
        """ Test that the base class does not have a _get_page_data function """
        expected = r""
        with pytest.raises(NotImplementedError, match=expected):
            basecrawler._get_page_data()

    def test_base_class__get_image_from_elem_returns_correct_value(self, basecrawler):
        """ Test the _get_image_from_elem function """
        html_string = '<div><img class="testclass" src="/some/image.jpg" /></div>'
        elem = lxml.html.fromstring(html_string)

        actual = basecrawler._get_image_from_elem(elem, "img.testclass")
        expected = "https://mario.nintendo.com/some/image.jpg"

        assert expected == actual

    def test_base_class_no_get_data_implemented(self, basecrawler):
        """ Test that the base class does not have a get_data function """
        expected = r"get_data\(\) is not implemented"
        with pytest.raises(NotImplementedError, match=expected):
            basecrawler.get_data()

    def test_if_get_copyright_is_called_with_correct_types(self, mocker, basecrawler, elem):
        """ Test that the copyright function returns correct types """
        mocked_copyright = mocker.patch.object(data_crawl.basecrawler.BaseCrawler, '_get_copyright', autospec=True)
        basecrawler._get_copyright(elem)
        (func, call_args) = mocked_copyright.call_args[0]
        
        actual = type(call_args)
        expected = lxml.html.HtmlElement

        assert expected == actual

    def test_if_get_copyright_is_returns_correct_value(self, basecrawler, elem):
        """ Test that the copyright function returns correct value """
        html_string = '<div class="footer-main__links__legal"><p>Test copyright</p>No copyright</div>'
        elem = lxml.html.fromstring(html_string)

        actual = basecrawler._get_copyright(elem)
        expected = 'Test copyright'

        assert expected == actual

    def test_base_class_cannot_be_inited_with_params(self, basecrawler):
        """ Test that the base class does not accept parameters """
        expected = r"_get_image_from_elem\(\) missing 2 required positional arguments: \'elem\' and \'selector\'"
        with pytest.raises(TypeError, match=expected):
            basecrawler._get_image_from_elem()

    def test_if_get_text_from_elem_returns_correct_value(self, basecrawler, elem):
        """ Test that the copyright function returns correct value """
        html_string = '<div class="correct-identifier">Lorum ipsum</div>'
        elem = lxml.html.fromstring(html_string)

        actual = basecrawler._get_text_from_elem(elem, "div.correct-identifier")
        expected = "Lorum ipsum"

        assert expected == actual

    def test_if_get_text_from_elem_returns_none_for_no_match(self, basecrawler, elem):
        """ Test that the copyright function returns correct value """
        html_string = '<div class="correct-identifier">Lorum ipsum</div>'
        elem = lxml.html.fromstring(html_string)

        actual = basecrawler._get_text_from_elem(elem, "div.incorrect-identifier")
        expected = None

        assert expected is actual

    def test_if__get_selector_returns_empty_list_for_no_match(self, basecrawler, elem):
        """ Test that the get selector function returns an empty list for no match """
        html_string = '<div class="correct-identifier">Lorum ipsum</div>'
        elem = lxml.html.fromstring(html_string)

        actual = basecrawler._get_selector(elem, "div.incorrect-identifier")
        expected = []

        assert expected == actual