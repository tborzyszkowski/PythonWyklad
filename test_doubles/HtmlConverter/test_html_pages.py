import unittest
import io
from src.test_doubles.HtmlConverter.html_pages import HtmlPagesConverter


class HtmlConverterTests(unittest.TestCase):
    def test_convert_quotes(self):
        fake_file = io.StringIO("quote: ' ")
        converter = HtmlPagesConverter(open_file=fake_file)
        converted_text = converter.get_html_page(0)
        self.assertEqual(converted_text, "quote: &#x27;<br />")

    def test_access_second_page(self):
        fake_file = io.StringIO("""\
page one
PAGE_BREAK
page two
PAGE_BREAK
page three
""")
        converter = HtmlPagesConverter(open_file=fake_file)
        converted_text = converter.get_html_page(1)
        self.assertEqual(converted_text, "page two<br />")
