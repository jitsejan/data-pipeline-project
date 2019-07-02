import lxml.html
import os
import sys
import unittest
import unittest.mock as mock

sys.path.append(os.path.abspath(sys.path[0]) + "/../")
from data_crawl.basecrawler import BaseCrawler
from data_crawl.charactercrawler import CharacterCrawler


class DataCrawlTestClass(unittest.TestCase):
    """ Defines the tests for the base class for the DataCrawl """

    def setUp(self):
        """ Setup the default settings """
        self.object_to_test = BaseCrawler()
        self.elem = lxml.html.fromstring("<fake><element></element></fake>")

    def test_base_url(self):
        expected = "https://mario.nintendo.com"
        actual = self.object_to_test.BASE_URL

        self.assertEqual(expected, actual)

    @mock.patch("data_crawl.basecrawler.BaseCrawler._get_copyright", autospec=True)
    def test_if_get_copyright_is_called_with_correct_types(self, mocked_method):
        self.object_to_test._get_copyright(self.elem)
        (func, call_arg) = mocked_method.call_args[0]

        self.assertEqual(type(call_arg), lxml.html.HtmlElement)

    def test_base_class_cannot_be_inited_with_params(self):
        expected = "_get_image_from_elem() missing 2 required positional arguments: 'elem' and 'selector'"
        with self.assertRaises(TypeError) as context:
            self.object_to_test._get_image_from_elem()
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_base_class_no_get_data_implemented(self):
        expected = "get_data() is not implemented"
        with self.assertRaises(NotImplementedError) as context:
            self.object_to_test.get_data()
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    @mock.patch("data_crawl.charactercrawler.CharacterCrawler.get_data", autospec=True)
    def test_derived_class_get_data_is_called_twice(self, mocked_method):
        """ Test if the derived class get data function is called twice """
        subject = CharacterCrawler()
        subject.get_data()
        subject.get_data()

        self.assertEqual(mocked_method.call_count, 2)


if __name__ == "__main__":
    unittest.main()
