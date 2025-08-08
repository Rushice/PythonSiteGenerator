import unittest

from src.util.markdowntohtml import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
  def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

  def test_unordered_list(self):
    md = """
- First item with **bold** text
- Second item with _italic_ text
- Third item with `code`
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>First item with <b>bold</b> text</li><li>Second item with <i>italic</i> text</li><li>Third item with <code>code</code></li></ul></div>",
    )

  def test_ordered_list(self):
    md = """
1. First numbered item
2. Second numbered item with **emphasis**
3. Third numbered item
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>First numbered item</li><li>Second numbered item with <b>emphasis</b></li><li>Third numbered item</li></ol></div>",
    )

  def test_mixed_lists(self):
    md = """
- Unordered item 1
- Unordered item 2

1. Ordered item 1
2. Ordered item 2
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>Unordered item 1</li><li>Unordered item 2</li></ul><ol><li>Ordered item 1</li><li>Ordered item 2</li></ol></div>",
    )

  def test_quote_block(self):
    md = """
> This is a quote with **bold** text
> and _italic_ text spanning
> multiple lines
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>This is a quote with <b>bold</b> text and <i>italic</i> text spanning multiple lines</blockquote></div>",
    )

  def test_quote_with_multiple_paragraphs(self):
    md = """
> First paragraph of quote
> with `inline code`

> Second quote block
> on multiple lines
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>First paragraph of quote with <code>inline code</code></blockquote><blockquote>Second quote block on multiple lines</blockquote></div>",
    )

  def test_heading_blocks(self):
    md = """
# This is an H1 with **bold**

## This is an H2 with _italic_

### This is an H3

#### This is an H4

##### This is an H5

###### This is an H6 with `code`
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>This is an H1 with <b>bold</b></h1><h2>This is an H2 with <i>italic</i></h2><h3>This is an H3</h3><h4>This is an H4</h4><h5>This is an H5</h5><h6>This is an H6 with <code>code</code></h6></div>",
    )

if __name__ == "__main__":
  unittest.main()