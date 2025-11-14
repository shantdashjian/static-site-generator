from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    textnodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    textnodes = split_nodes_delimiter(textnodes, "_", TextType.ITALIC)
    textnodes = split_nodes_delimiter(textnodes, "`", TextType.CODE)
    textnodes = split_nodes_image(textnodes)
    textnodes = split_nodes_link(textnodes)
    return textnodes
