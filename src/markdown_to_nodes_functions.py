import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        for i in range(len(parts)):
            if not parts[i]:
                continue
            if i % 2 == 0:
                nodes.append(TextNode(node.text, node.text_type, node.url))
            else:
                nodes.append(TextNode(parts[i], text_type, node.url))
    return nodes    

def extract_markdown_images(text):
    parts = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return parts

def extract_markdown_links(text):
    parts = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return parts
