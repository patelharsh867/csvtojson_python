from __future__ import absolute_import
import csv
import json
import io


with open('nid_name.csv', 'r') as csvfile:

    csvfields = 'nid', 's1', 'd1', 'y1', 's2', 'd2', 'y2', 's3', 'd3', 'y3', 's4', 'd4', 'y4','s5','d5','y5'
    reader = csv.DictReader(csvfile, fieldnames=csvfields)
    database = {}
    education = database['education'] = []  # initialize item to be parsed
    for row in reader:
        education.append(
            {
                'nid' : row['nid'],

            'education':[{
                'orgName' : row['s1'],
                'degree' : row['d1'],
                'graduationDate' : row['y1']
            },
            {
                'orgName' : row['s2'],
                'degree' : row['d2'],
                'graduationDate' : row['y2']
            },
            {
                'orgName' : row['s3'],
                'degree' : row['d3'],
                'graduationDate' : row['y3']
            },
            {
                'orgName' : row['s4'],
                'degree' : row['d4'],
                'graduationDate' : row['y4']
            },{
                'orgName' : row['s5'],
                'degree' : row['d5'],
                'graduationDate' : row['y5']
            }]
            }
        )

f = open("file.json", "w")
f.write(str(education))


    