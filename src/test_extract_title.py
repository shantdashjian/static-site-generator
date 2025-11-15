import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_no_title(self):
        markdown = "Hello"
        with self.assertRaises(ValueError):
            extract_title(markdown)