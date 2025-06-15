from html.parser import HTMLParser

class MyHTMLLinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    print(f"Znaleziono link: {value}")

html_doc = """
<html>
<body>
    <p>Odwiedź <a href="https://www.python.org">Python.org</a> lub
    <a href="https://www.google.com">Google</a>.</p>
</body>
</html>
"""

if __name__ == "__main__":
    parser = MyHTMLLinkParser()
    parser.feed(html_doc)