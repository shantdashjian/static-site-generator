import unittest

from converter import Converter
from textnode import TextNode, TextType

class TestConverter(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Good", TextType.TEXT)
        self.assertEqual(Converter.text_node_to_html_node(text_node).__repr__(), "HTMLNode(None, Good, None, None)")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Good", TextType.BOLD)
        self.assertEqual(Converter.text_node_to_html_node(text_node).__repr__(), "HTMLNode(b, Good, None, None)")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Good", TextType.ITALIC)
        self.assertEqual(Converter.text_node_to_html_node(text_node).__repr__(), "HTMLNode(i, Good, None, None)")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Good", TextType.LINK, "https://procodingmentor.com")
        self.assertEqual(Converter.text_node_to_html_node(text_node).__repr__(), 'HTMLNode(a, Good, None, href="https://procodingmentor.com")')

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("Good", TextType.IMAGE, "https://procodingmentor.com/profile.jpg")
        self.assertEqual(Converter.text_node_to_html_node(text_node).__repr__(), 'HTMLNode(img, None, None, src="https://procodingmentor.com/profile.jpg" alt="Good")')

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Good", TextType.CODE)
        self.assertEqual(Converter.text_node_to_html_node(text_node).__repr__(), 'HTMLNode(code, Good, None, None)')
    
    def test_text_node_to_html_node_other(self):
        text_node = TextNode("Good", "Other")
        self.assertRaises(Exception, Converter.text_node_to_html_node, text_node)