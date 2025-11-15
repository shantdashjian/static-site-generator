import os
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    source_path = os.path.join(os.getcwd(), dir_path_content)
    destination_path = os.path.join(os.getcwd(), dest_dir_path)
    entries = os.listdir(source_path)
    for entry in entries:
        entry_path_source = os.path.join(source_path, entry)
        entry_path_destination = os.path.join(destination_path, entry)
        if os.path.isfile(entry_path_source):
            entry_path_destination_html = entry_path_destination.replace(".md", ".html")
            generate_page(entry_path_source, template_path, entry_path_destination_html)
        else:
            os.mkdir(entry_path_destination)
            generate_pages_recursive(entry_path_source, template_path, entry_path_destination)