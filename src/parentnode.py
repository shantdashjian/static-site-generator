from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        if self.children == None:
            raise ValueError("No children")
        children_html = []
        for child in self.children:
            children_html.append(child.to_html())
        props = ""
        if self.props != None:
            props = f" {self.props_to_html()}"
        return f"<{self.tag}{props}>{"".join(children_html)}</{self.tag}>"
