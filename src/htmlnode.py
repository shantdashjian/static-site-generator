class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        build = lambda item: f"{item[0]}=\"{item[1]}\""
        return (" ").join(list(map(build, self.props.items())))
    
    def __repr__(self):
        props = None
        if self.props != None:
            props = self.props_to_html()
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {props})"
