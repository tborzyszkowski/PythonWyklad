"""Extract list of URLs in a web page

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

from _07_HTMLParser.code_python2.sgmllib_old import SGMLParser

class URLLister(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []

	def start_a(self, attrs):
		href = [v for k, v in attrs if k == 'href']
		if href:
			self.urls.extend(href)


if __name__ == "__main__":
	import urllib

	# link = "http://www.wp.pl/"
	link = "https://mfi.ug.edu.pl//"
	# link = "https://www.python.org/"
	parser = URLLister()
	with urllib.request.urlopen(link) as url:
		parser.feed(url.read())
		parser.close()

	for url in parser.urls:
		if url:
			print(url)
	print(len(parser.urls))
