from ..leafnode import LeafNode
from ..textnode import TextNode, TextType


def text_node_to_html_node(text_node: TextNode):
  match text_node.text_type:
    case TextType.TEXT:
      return LeafNode(None, text_node.text)
    case TextType.BOLD:
      return LeafNode("b", text_node.text)
    case TextType.ITALIC:
      return LeafNode("i", text_node.text)
    case TextType.CODE:
      return LeafNode("code", text_node.text)
    case TextType.LINK:
      prop = {"href":text_node.url}
      return LeafNode("a", text_node.text,prop)
    case TextType.IMAGE:
      prop = {"src":text_node.url ,
              "alt":text_node.text}
      return LeafNode("img", "", prop)
    case _:
      raise Exception("Text type does not exist")