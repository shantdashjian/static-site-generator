from textnode import TextNode, TextType

def main():
    link_node = TextNode("My personal website", TextType.LINK, "https://shantdashjian.com")
    print(link_node)

if __name__ == "__main__":
    main()