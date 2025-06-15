from html.parser import HTMLParser
from collections import Counter

class MyHTMLTagCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_counts = Counter()

    def handle_starttag(self, tag, attrs):
        self.tag_counts[tag] += 1

html_doc = """
<div>
    <p>Pierwszy paragraf.</p>
    <span>To jest span.</span>
    <p>Drugi paragraf.</p>
    <div>Kolejny div.</div>
</div>
"""

parser = MyHTMLTagCounter()
parser.feed(html_doc)
print("Liczba wystąpień tagów:", parser.tag_counts)