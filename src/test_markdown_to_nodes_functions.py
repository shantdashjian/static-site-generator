import unittest
from markdown_to_nodes_functions import split_nodes_delimiter
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
