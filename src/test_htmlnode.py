import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_a_href(self):
        props = {}
        props["href"] = "https://procodingmentor.com"
        node = HTMLNode("a", "Home", None, props)
        self.assertEqual(node.props_to_html(), 'href="https://procodingmentor.com"')

    def test_props_to_html_img_src_alt(self):
        props = {}
        props["src"] = "https://procodingmentor.com/profile.jpg"
        props["alt"] = "profile"
        node = HTMLNode("img", None, None, props)
        self.assertEqual(node.props_to_html(), 'src="https://procodingmentor.com/profile.jpg" alt="profile"')
    
    def test_repr(self):
        props = {}
        props["src"] = "https://procodingmentor.com/profile.jpg"
        props["alt"] = "profile"
        node = HTMLNode("img", None, None, props)
        self.assertEqual(node.__repr__(), 'HTMLNode(img, None, None, src="https://procodingmentor.com/profile.jpg" alt="profile")')
