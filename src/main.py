import sys
from copy_content import copy_content
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_content("static", "public")
    generate_pages_recursive(basepath, "content", "template.html", "public")

if __name__ == "__main__":
    main()