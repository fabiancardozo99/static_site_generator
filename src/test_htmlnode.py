import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        html_node = HTMLNode("a", "Google", None, {"href": "https://www.google.com"})
        self.assertEqual(
            'HTMLNode(a, Google, None,  href="https://www.google.com")', repr(html_node)
        )

    def test_props(self):
        html_node = HTMLNode(
            "a",
            "Google",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        result = html_node.props_to_html()
        self.assertEqual(' href="https://www.google.com" target="_blank"', result)

    def test_props_empty(self):
        html_node = HTMLNode("a", "Google", None, None)
        result = html_node.props_to_html()
        self.assertEqual("", result)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
