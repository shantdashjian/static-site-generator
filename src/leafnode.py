from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return self.value
        props = ""
        if self.props != None:
            props = f" {self.props_to_html()}"
        return f'<{self.tag}{props}>{self.value}</{self.tag}>'