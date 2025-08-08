from .htmlnode import HTMLNode


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("Parent Node tag cannot be None")

    if self.children is None:
      raise ValueError("Parent Node cannot have no children nodes")

    result = [f"<{self.tag}{self.props_to_html()}>"]
    for child in self.children:
      result.append(child.to_html())
    result.append(f"</{self.tag}>")
    return "".join(result)