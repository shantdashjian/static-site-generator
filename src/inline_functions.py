import re
from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    return (
        split_nodes_link(
            split_nodes_image(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter(nodes
                            , "**", TextType.BOLD)
                        , "_", TextType.ITALIC)
                    , "`", TextType.CODE
                )
            )
        )
    )

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
                nodes.append(TextNode(parts[i], node.text_type))
            else:
                nodes.append(TextNode(parts[i], text_type))
    return nodes    

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if node.text_type != TextType.TEXT or not images:
            nodes.append(node)
            continue
        text_start = 0
        text_end = 0
        for image in images:
            image_start = node.text.index(image[0]) - 2
            image_end = node.text.index(image[1]) + len(image[1])
            text_end = image_start
            if text_start < text_end:
                nodes.append(TextNode(node.text[text_start:text_end], TextType.TEXT))
            nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text_start = image_end + 1
            text_end = image_end + 1
        if text_start < len(node.text):
            nodes.append(TextNode(node.text[text_start:], TextType.TEXT))
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if node.text_type != TextType.TEXT or not links:
            nodes.append(node)
            continue
        text_start = 0
        text_end = 0
        for link in links:
            link_start = node.text.index(link[0]) - 1
            link_end = node.text.index(link[1]) + len(link[1])
            text_end = link_start
            if text_start < text_end:
                nodes.append(TextNode(node.text[text_start:text_end], TextType.TEXT))
            nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text_start = link_end + 1
            text_end = link_end + 1
        if text_start < len(node.text):
            nodes.append(TextNode(node.text[text_start:], TextType.TEXT))
    return nodes

def extract_markdown_images(text):
    parts = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return parts

def extract_markdown_links(text):
    parts = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return parts
