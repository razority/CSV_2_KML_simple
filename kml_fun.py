import re


def new_point(filename, name, lat, lon):
    '''
    Simple text-writer: add point which contains name and coordinates, framed XML elements
    '''
    filename.write(f'\n<Placemark>\n<name>{name}</name>\n<Point><coordinates>{lon},{lat},0</coordinates></Point>\n</Placemark>')

def convert(coord_string):
    '''
    Converting coordinates from Grad Min Sec to Grad.
    '''
    g, m, s = re.split(r'\D', re.sub(r'[a-zA-Z"]', '', coord_string), maxsplit=2)
    #print(f'{g}, {m}, {s}')
    return round(int(g) + int(m)/60 + float(s)/3600, 7)

start = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.2">
<Document>'''

end = '\n</Document>\n</kml>'