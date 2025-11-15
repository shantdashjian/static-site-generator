from block_to_block_type import block_to_block_type
from blocktype import BlockType
from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_node_to_html_node import text_node_to_html_node
from text_to_children import text_to_children
import re

from textnode import TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block_node = paragraph_block_to_html_node(block)
            case BlockType.HEADING:
                block_node = heading_block_to_html_node(block)
            case BlockType.QUOTE:
                block_node = quote_block_to_html_node(block)
            case BlockType.UNORDERED_LIST:
                block_node = unordered_list_block_to_html_node(block)
            case BlockType.ORDERED_LIST:
                block_node = ordered_list_block_to_html_node(block)
            case BlockType.CODE:
                block_node = code_block_to_html_node(block)
        children.append(block_node)

    div_node = ParentNode("div", children)
    return div_node

def heading_block_to_html_node(block):
    matching_parts = re.match(r"^(#{1,6}) (.*)$", block)
    heading_hash = matching_parts.group(1)
    heading_text = matching_parts.group(2)
    heading_hash_length = len(heading_hash)
    block_children = text_to_children(heading_text)
    block_node = ParentNode(f"h{heading_hash_length}", block_children)
    return block_node

def paragraph_block_to_html_node(block):
    block_children = text_to_children(block)
    block_node = ParentNode("p", block_children)
    return block_node

def quote_block_to_html_node(block):
    lines = block.split("\n")
    text = []
    for line in lines:
        matching_parts = re.match(r"^(>)(.*)$", line)
        quote_text = matching_parts.group(2)
        text.append(quote_text)
    block = " ".join(text)
    block_children = text_to_children(block)
    block_node = ParentNode("blockquote", block_children)
    return block_node

def unordered_list_block_to_html_node(block):
    lines = block.split("\n")
    block_children = []
    for line in lines:
        matching_parts = re.match(r"^(-) (.*)$", line)
        quote_text = matching_parts.group(2)
        line_children = text_to_children(quote_text)
        block_children.append(ParentNode("li", line_children))
    block_node = ParentNode("ul", block_children)
    return block_node

def ordered_list_block_to_html_node(block):
    lines = block.split("\n")
    block_children = []
    for line in lines:
        matching_parts = re.match(r"^(\d\.) (.*)$", line)
        quote_text = matching_parts.group(2)
        line_children = text_to_children(quote_text)
        block_children.append(ParentNode("li", line_children))
    block_node = ParentNode("ol", block_children)
    return block_node

def code_block_to_html_node(block):
    text_node = TextNode("\n".join(block.split("\n")[1:-1]) + "\n", TextType.CODE)
    html_node = text_node_to_html_node(text_node)
    pre_node = ParentNode("pre", [html_node])
    return pre_node
                
               