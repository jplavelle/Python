import csv
import sys

print ('Ensure the relevant files are present in the same directory.')
reporting_year = raw_input('Enter the reporting year you wish to append to the output file.>>>')

input_file = 'DC_Agency_Performance_Data_KPIs__%s.csv' % reporting_year

KPI = csv.reader(open(input_file, 'rb'))

header = KPI.next()

hsp = [(header)]

for row in KPI:
    if row[17] == 'HOMELESS SERVICES PROGRAM':
        hsp.append(row)

print hsp

with open('Human_Services_KPIs.csv','wb') as output_path:
    output_file = csv.writer(output_path)
    output_file.writerows(hsp)
