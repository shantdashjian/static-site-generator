import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("Pro Coding Mentor", TextType.LINK, "https://procodingmentor.com")
        node2 = TextNode("Pro Coding Mentor", TextType.LINK, "https://procodingmentor.com")
        self.assertEqual(node1, node2)

    def test__not_eq_text(self):
        node1 = TextNode("This is a text", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test__not_eq_type(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_url(self):
        node1 = TextNode("Pro Coding Mentor", TextType.LINK, "https://procodingmentor.com")
        node2 = TextNode("Pro Coding Mentor", TextType.LINK, "https://procodingmentors.com")
        self.assertNotEqual(node1, node2)
    

if __name__ == "__main__":
    unittest.main()