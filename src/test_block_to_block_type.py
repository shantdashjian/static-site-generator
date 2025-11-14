import unittest

from block_to_block_type import block_to_block_type
from blocktype import BlockType
from markdown_to_blocks import markdown_to_blocks

class TestBlockToBlocktype(unittest.TestCase):
    def test_heading(self):
        block = "### Welcome"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code(self):
        block_markdown = """
```
print("Hello")
```
        """
        blocks = markdown_to_blocks(block_markdown)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.CODE)

    def test_quote(self):
        block_markdown = """
> Yes
> I did
        """
        blocks = markdown_to_blocks(block_markdown)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.QUOTE)

    def test_unordered_list(self):
        block_markdown = """
- First
- Second
        """
        blocks = markdown_to_blocks(block_markdown)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block_markdown = """
1. First
2. Second
        """
        blocks = markdown_to_blocks(block_markdown)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block_markdown = """
First Second
        """
        blocks = markdown_to_blocks(block_markdown)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.PARAGRAPH)