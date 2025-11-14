from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(links) == 0:
                new_nodes.append(node)
                continue
            text_left = node.text
            for text, href in links:
                link_string = f"[{text}]({href})"
                if text_left.startswith(link_string):
                    new_node = TextNode(text, TextType.LINK, href)
                    new_nodes.append(new_node)
                    text_left = text_left[len(link_string):]
                else:
                    pre_link_text = text_left[0:text_left.index(link_string)]
                    new_node = TextNode(pre_link_text, TextType.TEXT)
                    new_nodes.append(new_node)
                    new_node = TextNode(text, TextType.LINK, href)
                    new_nodes.append(new_node)
                    text_left = text_left[len(pre_link_text) + len(link_string):]
            if text_left:
                new_node = TextNode(text_left, TextType.TEXT)
                new_nodes.append(new_node)
    return new_nodes