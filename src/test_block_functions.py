import unittest

from block_functions import block_to_block_type, markdown_to_blocks
from blocknode import BlockType


class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_header(self):
        md = """
# This is a header
    """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_header_2(self):
        md = """
## This is a header
    """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_code(self):
        md = """
```
print("Hello")
```
    """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, block_type)

    def test_quote(self):
        md = """
> To Be or Not to Be
> To Be or Not to Be
> To Be or Not to Be
    """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_unordered_list(self):
        md = """
- To Be or Not to Be
- To Be or Not to Be
- To Be or Not to Be
    """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_ordered_list(self):
        md = """
1. To Be or Not to Be
2. To Be or Not to Be
3. To Be or Not to Be
    """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_paragraph(self):
        md = """
To Be or Not to Be
To Be or Not to Be
To Be or Not to Be
    """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)
