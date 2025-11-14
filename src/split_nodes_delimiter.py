from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) == 1:
                new_nodes.append(node)
                continue
            if len(parts) % 2 == 0:
                raise Exception("invalid markdown")
            this_it_text = True
            i = 0
            while i < len(parts):
                if parts[i] == "" and i == len(parts) - 1:
                    break
                if parts[i] == "":
                    new_node = TextNode(parts[i + 1], text_type)
                    new_nodes.append(new_node)
                    i += 1
                    this_it_text = True
                elif this_it_text:
                    new_node = TextNode(parts[i], TextType.TEXT)
                    new_nodes.append(new_node)
                    this_it_text = False
                else:
                    new_node = TextNode(parts[i], text_type)
                    new_nodes.append(new_node)
                    this_it_text = True
                i += 1
    return new_nodes