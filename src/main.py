from textnode import TextNode, TextType


def main():
    pro_coding_mentor = TextNode(
        "Pro Coding Mentor", 
        TextType.LINK, 
        "https://procodingmentor.com"
    )
    print(pro_coding_mentor)

main()