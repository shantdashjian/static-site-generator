import unittest

from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_simple_paragraphs(self):
        md = """
This is a paragraph

This is another paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph</p><p>This is another paragraph</p></div>",
        )

    def test_simple_paragraph_with_code(self):
        md = """
This is a paragraph with `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with <code>code</code></p></div>",
        )


    def test_paragraph_on_multiple_lines(self):
        md = """
This is a paragraph
on multiple
lines
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph on multiple lines</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings_1(self):
        md = """
# This is an _H1_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is an <i>H1</i></h1></div>",
        )

    def test_headings_6(self):
        md = """
###### This is an **H6**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is an <b>H6</b></h6></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote></div>",
        )

    def test_multi_line_quote(self):
        md = """
> This is a quote
> that is multi-line
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that is multi-line</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- This is a list item
- So it this one
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list item</li><li>So it this one</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. This is a list item
2. So it this one
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is a list item</li><li>So it this one</li></ol></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        actual_html = node.to_html()
        expected_html = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        self.assertEqual(
            actual_html,
            expected_html,
        )