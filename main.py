# -*- coding: utf-8 -*-
import re

def new_point(filename, name, lat, lon):
    filename.write(f'\n<Placemark><name>{name}</name>\n<Point><coordinates>{lon},{lat},0</coordinates></Point>\n</Placemark>')

def convert(coord_string):
    '''
    converting coordinates from Grad Min Sec to Grad.
    '''
    g, m, s = re.split(r'\D', re.sub(r'[a-zA-Z"]', '', coord_string), maxsplit=2)
    #print(f'{g}, {m}, {s}')
    return round(int(g) + int(m)/60 + float(s)/3600, 7)

filename_kml = 'kml_list.kml'
filename_csv = 'csv.csv'

len_of_file = 0
csv_file = open(filename_csv, "r")
csv_file.readline()
kml_file = open(filename_kml, 'w')
kml_file.write('<?xml version="1.0" encoding="UTF-8"?>')
kml_file.write('<kml xmlns="http://earth.google.com/kml/2.2">')
kml_file.write('<Document>')

for line in csv_file:
    line = line.replace("\r", "").replace("\n", "")
    # print(line)
    # print(re.search(r'[\s|a-zA-Z"\']',line))
    # print(line[line.find(','):])
    if re.search(r'[\s|a-zA-Z"\']', line[line.find(','):]) == None:
        name, lat, lon = line.split(',')
    else:
        name, lat, lon = line.split(',')
        #print(f'{name}, {lat}, {lon}')
        lat = convert(lat)
        lon = convert(lon)
    new_point(kml_file, name, lat, lon)
    len_of_file += 1

csv_file.close()
kml_file.write('\n</Document></kml>')
kml_file.close()

print(f'Ready! \nTotal {len_of_file} points.')
