import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p", "Some text")
        node2 = HTMLNode("p", "Some text")
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HTMLNode("p", "Some text")
        node2 = HTMLNode("span", "Some text")
        self.assertNotEqual(node1, node2)
    
    def test_props_to_html(self):
        node = HTMLNode("a", "Pro Coding Mentor", None, {"href": "https://procodingmentor.com", "class": "red"})
        props_to_html = node.props_to_html()
        self.assertEqual(props_to_html, ' href="https://procodingmentor.com" class="red"')