This project provides Genshi templates for outputting Atom feed documents and service documents.

Sample Usage:

from genshi.template import TemplateLoader
import feedparser

def main():
> loader = TemplateLoader(['..'])
> tmpl = loader.load('atom-feed.xml')

> d = feedparser.parse('test-complete.xml')

> stream = tmpl.generate(feed=d.feed, entries=d.entries)
> print stream.render('xml')

if name == 'main':
> main()

