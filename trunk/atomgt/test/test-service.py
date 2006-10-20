import genshi
from genshi import XML, Stream
from genshi.template import MarkupTemplate
from genshi.template import TemplateLoader


class Workspace:
  def __init__(self, title=None, attrs={}, collections=[]):
    self.title = title
    self.attrs = attrs
    self.collections = collections

class Collection:
  def __init__(self,
    title=None, href=None, accept=None, attrs={}, categories=[]):

    self.title = title
    self.href = href
    self.accept = accept
    self.attrs = attrs
    self.categories = categories

class Categories:
  def __init__(self, scheme=None, fixed='no', list=[]):
    self.scheme = scheme
    self.fixed = fixed
    self.list = list

class Category:
  def __init__(self, scheme=None, term=None, label=None, attrs={}):
    self.scheme = scheme
    self.term = term
    self.label = label
    self.attrs = attrs


def main():

  loader = TemplateLoader(['..'])
  tmpl = loader.load('atom-service.xml')
  stream = tmpl.generate(
    service_attrs={'myServiceAttr':'myServiceAttrValue'},
    workspaces=[
      Workspace(
        title="Ben's workspace",
        collections=[
          Collection(title='News', categories="http://example.com/benCat")
        ]
      ),
      Workspace(
        title="Moe's workspace",
        collections=[
          Collection(title='Blog',
            categories=Categories(scheme='hi',list=[Category(term='myterm')]))
        ]
      )
    ]
    )

  serviceDoc = stream.render('xml')
  print serviceDoc
  """
  try:
    instream = XML(serviceDoc)
    substream = Stream(list(instream.select('workspace')))
    for kind, data, pos in substream:
      print kind, data
  except genshi.input.ParseError:
    print 'XML parsing error'
  """


if __name__ == '__main__':
  main()


