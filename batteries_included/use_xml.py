from xml.parsers.expat import ParserCreate
from urllib import request


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s ' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:end_element: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
# print(''.join(L))

def parseXml(xml_str):
    print(xml_str)
    return {
        'city': '?',
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low': 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low': 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low': 19
            }
        ]
    }


URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
