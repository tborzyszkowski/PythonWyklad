
import html as html_converter


class HtmlPagesConverter:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.open_file = open(self.filename)
        self._find_page_breaks()
        return self

    def __exit__(self, *exc):
        return self.open_file.close()

    def _find_page_breaks(self):
        """Read the file and note the positions of the page breaks
        so we can access them quickly"""
        self.breaks = [0]
        while True:
            line = self.open_file.readline()
            if not line:
                break
            if "PAGE_BREAK" in line:
                self.breaks.append(self.open_file.tell())
        self.breaks.append(self.open_file.tell())

    def get_html_page(self, page):
        """Return html page with the given number (zero indexed)"""
        page_start = self.breaks[page]
        page_end = self.breaks[page+1]
        html = ""
        self.open_file.seek(page_start)
        while self.open_file.tell() != page_end:
            line = self.open_file.readline()
            if "PAGE_BREAK" in line:
                continue
            line = line.rstrip()
            html += html_converter.escape(line, quote=True)
            html += "<br />"
        return html
