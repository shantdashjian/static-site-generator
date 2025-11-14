import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_already_code(self):
        node = TextNode("`This is text`", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "", TextType.TEXT)
        self.assertEqual(new_nodes, [node])

    def test_bad_markdown_for_bold(self):
        node = TextNode("This is text with **bold text in it.", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_only_text(self):
        node = TextNode("This is text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_text_bold_text(self):
        node = TextNode("This is text with **BOLD TEXT HERE** in it.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("BOLD TEXT HERE", TextType.BOLD),
            TextNode(" in it.", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_bold_only(self):
        node = TextNode("**BOLD TEXT HERE**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("BOLD TEXT HERE", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_text_bold(self):
        node = TextNode("some text **BOLD TEXT HERE**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("some text ", TextType.TEXT),
            TextNode("BOLD TEXT HERE", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_bold_bold(self):
        node = TextNode("**BOLD TEXT HERE****MORE BOLD TEXT HERE**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("BOLD TEXT HERE", TextType.BOLD),
            TextNode("MORE BOLD TEXT HERE", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_bold_text_bold(self):
        node = TextNode("**BOLD TEXT HERE**text**MORE BOLD TEXT HERE**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("BOLD TEXT HERE", TextType.BOLD),
            TextNode("text", TextType.TEXT),
            TextNode("MORE BOLD TEXT HERE", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes)