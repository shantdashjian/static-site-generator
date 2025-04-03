from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if not self.children:
            raise ValueError("Missing children")
        children_html = []
        for child in self.children:
            child_html = child.to_html()
            children_html.append(child_html)
        return f"<{self.tag}{self.props_to_html()}>{"".join(children_html)}</{self.tag}>"
