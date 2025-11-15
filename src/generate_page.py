import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(f"{from_path}", "r") as f:
        markdown = f.read()
    with open(f"{template_path}", "r") as f:
        template = f.read()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    dest_dir = "/".join(dest_path.split("/")[:-1])
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)
    with open(f"{dest_path}", "w") as f:
        f.write(full_html)
    
    
