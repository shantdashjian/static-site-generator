from textnode import TextType
from leafnode import LeafNode


class Converter:
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, value=text_node.text)
            case TextType.BOLD:
                return LeafNode("b", text_node.text, None)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text, None)
            case TextType.CODE:
                return LeafNode("code", text_node.text, None)
            case TextType.LINK:
                href = text_node.url
                return LeafNode("a", text_node.text, {"href": href})
            case TextType.IMAGE:
                src = text_node.url
                alt = text_node.text
                return LeafNode("img", None, {"src": src, "alt": alt})
            case _:
                raise Exception()
