import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_one_child(self):
        children = [LeafNode("b", "Bold text")]
        node = ParentNode("div", children, None)
        self.assertEqual(node.to_html(), "<div><b>Bold text</b></div>")

    def test_to_html_many_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("div", children, None)
        self.assertEqual(
            node.to_html(),
            "<div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>",
        )

    def test_to_html_no_children(self):
        children = None
        node = ParentNode("div", children, None)
        self.assertRaises(ValueError)
