import unittest

from extract_markdown_images import extract_markdown_images

class TextExtractMarkdownImages(unittest.TestCase):
    def test_one_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        actual_result = extract_markdown_images(text)
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(actual_result, expected_result)

    def test_two_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual_result = extract_markdown_images(text)
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual_result, expected_result)