# -*- coding: utf-8 -*-
import kml_fun
import re

filename_kml = 'kml_list.kml'
filename_csv = 'csv.csv'

len_of_file = 0
try:
    with open(filename_csv, "r") as csv_f, open(filename_kml, 'w') as kml_f:
        csv_f.readline()
        kml_f.write(kml_fun.start)

        for n, line in enumerate(csv_f, 2):
            line = line.replace("\r", "").replace("\n", "")
            if re.search(r'[\s|a-zA-Z"\']', line[line.find(','):]) == None:
                name, lat, lon = line.split(',')
            else:
                name, lat, lon = line.split(',')
                #print(f'{name}, {lat}, {lon}')
                lat = kml_fun.convert(lat)
                lon = kml_fun.convert(lon)
            kml_fun.new_point(kml_f, name, lat, lon)
            len_of_file += 1
        kml_f.write(kml_fun.end)
except ValueError:
    print(f'Error in file {filename_csv}:\nline №{n}: {line}')
else:
    print(f'Ready! \nTotal {len_of_file} points.')