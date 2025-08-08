import unittest

from src.textnode import TextNode, TextType
from src.util.textnodeconverter import text_node_to_html_node


class TestTextNode(unittest.TestCase):
  def test_plain_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.to_html(), "This is a text node")

  def test_bold_text(self):
    node = TextNode("This is a bold node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

  def test_italic_text(self):
    node = TextNode("This is a italic node", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

  def test_code_text(self):
    node = TextNode("This is a code node", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

  def test_link_text(self):
    node = TextNode("This is a link node", TextType.LINK,"https://www.google.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.to_html(), "<a href=\"https://www.google.com\">This is a link node</a>")

  def test_image_text(self):
    node = TextNode("This is a image node", TextType.IMAGE, "https://www.google.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.to_html(), "<img src=\"https://www.google.com\" alt=\"This is a image node\"></img>")

if __name__ == "__main__":
    unittest.main()