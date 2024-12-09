import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Value", None)
        self.assertEqual(node.to_html(), "<p>Value</p>")