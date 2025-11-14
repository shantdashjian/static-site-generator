import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "Google", None, props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_p_repr(self):
        node = HTMLNode("p", "Google", None, None)
        self.assertEqual(node.__repr__(), "HTMLNode(p, Google, None, None)")

    def test_repr_with_props(self):
        node = HTMLNode("p", "Google", None, {"class": "main"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, Google, None, {'class': 'main'})")