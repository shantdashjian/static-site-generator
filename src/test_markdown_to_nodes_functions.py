import unittest
from markdown_to_nodes_functions import extract_markdown_links, split_nodes_delimiter, extract_markdown_images
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_node_with_code_to_3(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))

    def test_text_node_with_code_to_3(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

class TextExtractMarkdownImages(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        image_parts = extract_markdown_images(text)
        self.assertEqual(image_parts[0][0], "rick roll")
        self.assertEqual(image_parts[0][1], "https://i.imgur.com/aKaOqIh.gif")
        self.assertEqual(image_parts[1][0], "obi wan")
        self.assertEqual(image_parts[1][1], "https://i.imgur.com/fJRm4Vk.jpeg")

class TextExtractMarkdownLinks(unittest.TestCase):
    def test_extract_link(self):
        text = "Visit [Pro Coding Mentor](https://procodingmentor.com)"
        image_parts = extract_markdown_links(text)
        self.assertEqual(image_parts[0][0], "Pro Coding Mentor")
        self.assertEqual(image_parts[0][1], "https://procodingmentor.com")
