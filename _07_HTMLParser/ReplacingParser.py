#!/usr/bin/env python3
"""
replace_words_regex.py

Usage:
    python replace_words_regex.py <url> [output.html]

Example:
    python replace_words_regex.py https://www.python.org python_mod.html
"""
import sys
import re
import os
import urllib.request
import webbrowser
from html.parser import HTMLParser
from html import escape

from ChefDialectReplacement import ChefDialectReplacement
from _07_HTMLParser import FuddDialectReplacement, OldeDialectReplacement


class ReplacingParser(HTMLParser):
    """HTMLParser that applies regex‑based replacements to text nodes."""

    def __init__(self, replacements):
        # keep raw &nbsp; etc. by disabling automatic char‑ref conversion
        super().__init__(convert_charrefs=False)
        # compile patterns once for speed
        self.replacements = [(re.compile(pat), repl) for pat, repl in replacements]
        self.out_parts: list[str] = []

    # ---------- tag echo helpers ----------
    @staticmethod
    def _echo_attrs(attrs):
        return "".join(
            f' {name}' if value is None
            else f' {name}="{escape(value, quote=True)}"'
            for name, value in attrs
        )

    # ---------- standard handlers ----------
    def handle_starttag(self, tag, attrs):
        self.out_parts.append(f"<{tag}{self._echo_attrs(attrs)}>")

    def handle_endtag(self, tag):
        self.out_parts.append(f"</{tag}>")

    def handle_startendtag(self, tag, attrs):
        self.out_parts.append(f"<{tag}{self._echo_attrs(attrs)}/>")

    def handle_data(self, data):
        for pattern, repl in self.replacements:
            data = pattern.sub(repl, data)
        self.out_parts.append(data)

    def handle_comment(self, data):
        self.out_parts.append(f"<!--{data}-->")

    def handle_entityref(self, name):
        self.out_parts.append(f"&{name};")

    def handle_charref(self, name):
        self.out_parts.append(f"&#{name};")

    # ---------- final HTML ----------
    def get_html(self):
        return "".join(self.out_parts)


def fetch_html(url: str) -> str:
    """Download raw HTML and decode with charset from headers (fallback UTF‑8)."""
    with urllib.request.urlopen(url) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python replace_words_regex.py <url> [output.html]")
        sys.exit(1)

    url = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else "modified.html"

    # --- fetch, parse, rewrite ---
    html = fetch_html(url)
    parser = ReplacingParser(ChefDialectReplacement.replacements)
    # parser = ReplacingParser(FuddDialectReplacement.replacements)
    # parser = ReplacingParser(OldeDialectReplacement.replacements)
    parser.feed(html)
    modified_html = parser.get_html()

    # --- save to disk ---
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(modified_html)

    abs_path = os.path.abspath(out_file)
    print(f"Saved modified page to {abs_path}")

    # --- open in default browser ---
    webbrowser.open(f"file://{abs_path}")
    print("Opened in your default web browser.")


if __name__ == "__main__":
    main()
