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

    def test_if_get_copyright_is_called_with_correct_types(self, mocker, basecrawler, elem):
        """ Test that the copyright function returns correct types """
        mocked_copyright = mocker.patch.object(data_crawl.basecrawler.BaseCrawler, '_get_copyright', autospec=True)
        basecrawler._get_copyright(elem)
        (func, call_args) = mocked_copyright.call_args[0]
        actual = type(call_args)
        expected = lxml.html.HtmlElement

        assert expected == actual

    def test_if_get_copyright_is_returns_correct_value(self, mocker, basecrawler, elem):
        """ Test that the copyright function returns correct value """
        html_string = '<div class="footer-main__links__legal"><p>Test copyright</p>No copyright</div>'
        actual = basecrawler._get_copyright(elem)
        expect = 'Test copyright'

        assert expected == actual


    def test_base_class_cannot_be_inited_with_params(self, basecrawler):
        """ Test that the base class does not accept parameters """
        expected = r"_get_image_from_elem\(\) missing 2 required positional arguments: \'elem\' and \'selector\'"
        with pytest.raises(TypeError, match=expected):
            basecrawler._get_image_from_elem()

    def test_base_class_no_get_data_implemented(self, basecrawler):
        """ Test that the base class does not have a get_data function """
        expected = r"get_data\(\) is not implemented"
        with pytest.raises(NotImplementedError, match=expected):
            basecrawler.get_data()
