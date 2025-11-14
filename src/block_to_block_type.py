from blocktype import BlockType
import re


def block_to_block_type(block):
    if re.match(r"^#{1,6} .*$", block):
        return BlockType.HEADING
    elif re.match(r"^```.*```$", block, re.DOTALL):
        return BlockType.CODE
    elif re.match(r"^>", block, re.MULTILINE):
        return BlockType.QUOTE
    elif re.match(r"^- ", block, re.MULTILINE):
        return BlockType.UNORDERED_LIST
    
    lines = block.split("\n")
    is_ordered_list = True
    for i in range(len(lines)):
        line = lines[i]
        if not line.startswith(f"{i + 1}. "):
            is_ordered_list = False
            break
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    