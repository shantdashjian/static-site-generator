import os
import shutil


def copy_content(source, destination):
    destination_path = os.path.join(os.getcwd(), destination)
    if os.path.isdir(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)
    copy_content_r(source, destination)

def copy_content_r(source, destination):
    source_path = os.path.join(os.getcwd(), source)
    destination_path = os.path.join(os.getcwd(), destination)
    entries = os.listdir(source_path)
    for entry in entries:
        entry_path = os.path.join(source_path, entry)
        if os.path.isfile(entry_path):
            shutil.copy(entry_path, destination_path)
        else:
            new_destination_path = os.path.join(destination_path, entry)
            os.mkdir(new_destination_path)
            copy_content_r(entry_path, new_destination_path)