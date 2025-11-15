import sys
from copy_content import copy_content
from generate_pages_recursive import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_content("static", "docs")
    generate_pages_recursive(basepath, "content", "template.html", "docs")

if __name__ == "__main__":
    main()