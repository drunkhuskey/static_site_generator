
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_string = ""
        for key in self.props:
            prop_string += f" {key}=\"{self.props[key]}\""
        return prop_string
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag assigned")
        if self.children == None:
            raise ValueError("no children assigned")
        text = f"<{self.tag}"
        if self.props != None:
            text += self.props_to_html()
        text += ">"
        for child in self.children:
            text += child.to_html()
        text += f"</{self.tag}>"
        return text
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        text = f"<{self.tag}"
        if self.props != None:
            text += self.props_to_html()
        text += f">{self.value}</{self.tag}>"
        return text