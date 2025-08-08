import unittest

from src.util.markdowntoblocks import BlockType, block_to_block_type, markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
      def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

      def test_block_to_block_type(self):
        md = """
###### This is a Header

# This is another header

####### This is a paragraph

```This is a code block```

``` This is a code block
with a new line ```

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a unordered list
- with items

>This is a quote block

1. This
2. Is
3. A
4. Ordered
5. List
"""
        blocks = markdown_to_blocks(md)
        block_types = list(map(block_to_block_type,blocks))
        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.PARAGRAPH,
                BlockType.CODE,
                BlockType.CODE,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.UNORDERED_LIST,
                BlockType.QUOTE,
                BlockType.ORDERED_LIST,
            ],
        )

if __name__ == "__main__":
  unittest.main()