from extract_markdown_images import extract_markdown_images
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(images) == 0:
                new_nodes.append(node)
                continue
            text_left = node.text
            for alt_text, url in images:
                image_string = f"![{alt_text}]({url})"
                if text_left.startswith(image_string):
                    new_node = TextNode(alt_text, TextType.IMAGE, url)
                    new_nodes.append(new_node)
                    text_left = text_left[len(image_string):]
                else:
                    pre_image_text = text_left[0:text_left.index(image_string)]
                    new_node = TextNode(pre_image_text, TextType.TEXT)
                    new_nodes.append(new_node)
                    new_node = TextNode(alt_text, TextType.IMAGE, url)
                    new_nodes.append(new_node)
                    text_left = text_left[len(pre_image_text) + len(image_string):]
            if text_left:
                new_node = TextNode(text_left, TextType.TEXT)
                new_nodes.append(new_node)
    return new_nodes