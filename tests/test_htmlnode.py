import unittest

from src.leafnode import LeafNode
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_mixed_types(self):
        props_dict = {
        "id": "main-button",
        "width": 300,
        "class": "btn-primary"
        }

        node = LeafNode(None,"This is a HTML Node",props_dict)

        html_props = node.props_to_html()

        self.assertEqual(html_props, " id=\"main-button\" width=\"300\" class=\"btn-primary\"")

    def test_props_basic(self):
        props_dict = {
          "href": "https://www.google.com",
          "target": "_blank",
        }

        node = LeafNode(None,"This is a HTML Node",props_dict)

        html_props = node.props_to_html()

        self.assertEqual(html_props, " href=\"https://www.google.com\" target=\"_blank\"")


    def test_props_empty(self):
        props_dict = {
        }

        node = LeafNode(None,"This is a HTML Node",props_dict)

        html_props = node.props_to_html()

        self.assertEqual(html_props, "")

if __name__ == "__main__":
    unittest.main()