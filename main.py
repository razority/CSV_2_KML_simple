# -*- coding: utf-8 -*-
def new_point(filename, name, lat, lon):
    filename.write(f'\n<Placemark><name>{name}</name><Point><coordinates>{lon},{lat},0</coordinates></Point></Placemark>')

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
    name, lat, lon = line.split(',')
    new_point(kml_file,name, lat, lon)
    len_of_file += 1
csv_file.close()
kml_file.write('\n</Document></kml>')
kml_file.close()

print(f'Ready! \nTotal {len_of_file} points.')
