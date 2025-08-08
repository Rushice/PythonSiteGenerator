import unittest

from src.leafnode import LeafNode
from src.parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_multiple_children(self):
    child_node = LeafNode("span", "child")
    other_child_node = LeafNode("span", "other child")
    parent_node = ParentNode("div", [child_node,other_child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>other child</span></div>")

  def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>",
      )


if __name__ == "__main__":
    unittest.main()