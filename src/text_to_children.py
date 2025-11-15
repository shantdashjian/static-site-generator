from text_node_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node)) 
    return html_nodes