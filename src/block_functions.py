def markdown_to_blocks(markdown):
    return list(
        filter(
            lambda line: line
            , map(lambda block: block.strip(" \n"), markdown.split("\n\n"))
        )
    )
