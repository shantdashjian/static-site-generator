import unittest
from markdown_to_nodes_functions import extract_markdown_links, split_nodes_delimiter, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextnodes(unittest.TestCase):

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_to_textnodes(text),
        )

    def test_text_to_textnodes(self):
        text = "This is **text**"

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD)
            ],
            text_to_textnodes(text),
        )

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_node_with_code_to_3(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))

    def test_text_node_with_code_to_3(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_text_node_with_bold(self):
        node = TextNode("This is text with a **code block**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.BOLD),
            ],
            new_nodes,
        )

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_not_last(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) here!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" here!", TextType.TEXT),
            ],
            new_nodes,
        )

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with two links: [Pro Coding Mentor](https://procodingmentor.com) and [Pro Coding Mentors](https://procodingmentors.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with two links: ", TextType.TEXT),
                TextNode(
                    "Pro Coding Mentor",
                    TextType.LINK,
                    "https://procodingmentor.com",
                ),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "Pro Coding Mentors",
                    TextType.LINK,
                    "https://procodingmentors.com",
                ),
            ],
            new_nodes,
        )

    def test_split_links_not_last(self):
        node = TextNode(
            "This is text with two links: [Pro Coding Mentor](https://procodingmentor.com) and [Pro Coding Mentors](https://procodingmentors.com)!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with two links: ", TextType.TEXT),
                TextNode(
                    "Pro Coding Mentor",
                    TextType.LINK,
                    "https://procodingmentor.com",
                ),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "Pro Coding Mentors",
                    TextType.LINK,
                    "https://procodingmentors.com",
                ),
                TextNode("!", TextType.TEXT),
            ],
            new_nodes,
        )

class TextExtractMarkdownImages(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        image_parts = extract_markdown_images(text)
        self.assertEqual(image_parts[0][0], "rick roll")
        self.assertEqual(image_parts[0][1], "https://i.imgur.com/aKaOqIh.gif")
        self.assertEqual(image_parts[1][0], "obi wan")
        self.assertEqual(image_parts[1][1], "https://i.imgur.com/fJRm4Vk.jpeg")

class TextExtractMarkdownLinks(unittest.TestCase):
    def test_extract_link(self):
        text = "Visit [Pro Coding Mentor](https://procodingmentor.com)"
        image_parts = extract_markdown_links(text)
        self.assertEqual(image_parts[0][0], "Pro Coding Mentor")
        self.assertEqual(image_parts[0][1], "https://procodingmentor.com")
