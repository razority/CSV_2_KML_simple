# -*- coding: utf-8 -*-
import kml_fun
import re

filename = kml_fun.json_load('filename.json')

filename_kml = filename['kml']
filename_csv = filename['csv']
# ',' comma separator in csv, use '\t' for tab-separator
separator = filename['separator']

try:
    with open(filename_csv, "r") as csv_f, open(filename_kml, 'w') as kml_f:
        csv_f.readline()
        kml_f.write(kml_fun.start)

        for n_lines, line in enumerate(csv_f, 2):
            '''
            Checking for correct file content and coordinates format
            '''
            line = line.replace("\r", "").replace("\n", "")
            if re.search(r'[ |a-zA-Z"\']', line[line.find(','):]) == None:
                name, lat, lon = line.split(separator)
                # if you using ',' for fraction separator
                lat.replace(',', '.')  #  58,34643 -> 58.34643
                lon.replace(',', '.')
            else:
                name, lat, lon = line.split(separator)
                #print(f'{name}, {lat}, {lon}')
                lat = kml_fun.convert(lat)
                lon = kml_fun.convert(lon)
            kml_fun.new_point(kml_f, name, lat, lon)
        kml_f.write(kml_fun.end)
except ValueError:
    print(f'Error in file {filename_csv}:\nline №{n}: {line}')
else:
    print(f'Ready! \nTotal {n_lines - 1} points.')