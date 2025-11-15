import re
def extract_title(markdown):
    matching_part = re.match(r"^# (.*)$", markdown, re.MULTILINE)
    if not matching_part:
        raise ValueError("no h1")
    heading_text = matching_part.group(1)
    return heading_text