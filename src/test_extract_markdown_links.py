import unittest

from extract_markdown_links import extract_markdown_links

class TextExtractMarkdownLinks(unittest.TestCase):
    def test_one_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        actual_result = extract_markdown_links(text)
        expected_result = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(actual_result, expected_result)

    def test_two_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual_result = extract_markdown_links(text)
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(actual_result, expected_result)