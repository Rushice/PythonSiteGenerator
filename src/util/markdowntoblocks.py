from enum import Enum

class BlockType(Enum):
  PARAGRAPH = 'paragraph'
  HEADING = 'heading'
  CODE = 'code'
  QUOTE = 'quote'
  UNORDERED_LIST = 'unordered_list'
  ORDERED_LIST = 'ordered_list'


def markdown_to_blocks(markdown: str):
  blocks = markdown.split("\n\n")
  for i in range(len(blocks)):
    blocks[i] = blocks[i].strip()
    if len(blocks[i]) == 0:
      del blocks[i]

  return blocks

def block_to_block_type(markdown: str):
  # check for header
  for i in range(1,7):
    prefix = '#' * i + ' '
    if markdown.startswith(prefix):
      return BlockType.HEADING

  if markdown.startswith("```") and markdown.endswith("```"):
    return BlockType.CODE

  lines = markdown.splitlines()
  is_quote = True
  is_unordered_list = True
  is_ordered_list = True
  for i in range(len(lines)):
      if lines[i].startswith('>') == False:
        is_quote = False
      if lines[i].startswith('- ') == False:
        is_unordered_list = False
      order_index = f"{i+1}. "
      if lines[i].startswith(order_index) == False:
        is_ordered_list = False

  if is_quote:
    return BlockType.QUOTE
  if is_unordered_list:
    return BlockType.UNORDERED_LIST
  if is_ordered_list:
    return BlockType.ORDERED_LIST

  return BlockType.PARAGRAPH