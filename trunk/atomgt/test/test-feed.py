import genshi
from genshi import XML, Stream
from genshi.template import MarkupTemplate
from genshi.core import Markup
from genshi.template import TemplateLoader
import feedparser

def main():
  loader = TemplateLoader(['..'])
  tmpl = loader.load('atom-feed.xml')

  d = feedparser.parse('test-complete.xml')

  # we add some extra attributes to feedparser model
  d.feed.author_detail.attrs ={'1myattr':'myval'}
  d.feed.tags[0].attrs ={'2myattr':'myval'}
  d.entries[0].content[0].attrs ={'3myattr':'myval'}
  d.feed.contributors[0].attrs ={'3myattr':'myval'}
  d.entries[0].attrs ={'4myattr':'myval'}
  d.feed.attrs={'5myattr':'myval'}
  d.feed.generator_detail.attrs={'6myattr':'myval'}
  d.feed.links[0].attrs={'7myattr':'myval'}
  d.entries[0].source.attrs={'8myattr':'myval'}

  # we need to set the proper output type for markup
  for entry in d.entries:
    for x in range(len(entry.content)):
      if(
        entry.content[x].type.endswith('+xml') or
        entry.content[x].type.endswith('/xml')):
        entry.content[x].value = Markup(entry.content[x].value)

  # Different ways to generate. Feed, or plain entry
  stream = tmpl.generate(feed=d.feed, entries=d.entries)
  #stream = tmpl.generate(feed=None,entries=d.entries)
  #stream = tmpl.generate(feed=None)

  serviceDoc = stream.render('xml')
  print serviceDoc

if __name__ == '__main__':
  main()


