from blocknode import BlockType


def markdown_to_blocks(markdown):
    return list(
        filter(
            lambda line: line
            , map(lambda block: block.strip(" \n"), markdown.split("\n\n"))
        )
    )

def block_to_block_type(block):
    if is_heading(block):
        return BlockType.HEADING
    if is_code(block):
        return BlockType.CODE
    if is_quote(block):
        return BlockType.QUOTE
    if is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_heading(block):
    return (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    )

def is_code(block):
    return block.startswith("```") and block.endswith("```")

def is_quote(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("> "):
            return False
    return True

def is_unordered_list(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("- "):
            return False
    return True

def is_ordered_list(block):
    lines = block.split("\n")
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            return False
    return True