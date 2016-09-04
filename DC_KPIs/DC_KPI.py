# This program compiles KPIs (key performance indicators), reported by the
# government of the District of Columbia, for the selected year and budget
# program. The result is saved to a CSV file for additional processing.

import csv
import sys

def data_in(year):
    csv.reader(open('DC_Agency_Performance_Data_KPIs__%s.csv', 'rb')) % year

def set_KPI_data(year):
    csv.reader(open('DC_Agency_Performance_Data_KPIs__%s.csv', 'rb')) % year

# Confirm source files are properly staged.
prep_check = raw_input("""Please ensure source files are in the same directory as this script.
Are you ready to proceed?
'Y' or 'N'""")

# If source files are not staged, the script will close.
# If ready, then the user is prompted to enter list of reporting years.
if prep_check = 'N':
    print ("Please have all relevant files prepared before proceeding.")
    exit
elif
    year_input = raw_input('Enter reporting years to compile, separated by a space.>>>')
    year_list = year_input.split(' ')

# Enter the budget program for which to compile KPIs.
program_input = raw_input('Enter the budget program you wish to compile.>>>')
budget_program = program_input.upper()

# Set first reporting year.
initial_year = year_list[0]

# Save out headers and initialize target list.
KPI_data = set_KPI_data(initial_year)
header = KPI_data.next()
program_compiled = [(header)]

# Loop through reporting years and budget programs.
i = 0

While i <=len(year_list) + 1:
    reporting_year = year_list[i]
    KPI_data = set_KPI_data(reporting_year)

    for row in KPI_data:
        if row[17] == budget_program:
            program_compiled.append(row)
    i =+ 1


# Update of results and saving results to CSV.
print 'Data to be saved out is as follows:\n%s' % program_compiled


with open('%s_KPIs.csv','wb') % budget_program as output_path:
    output_file = csv.writer(output_path)
    output_file.writerows(program_compiled)

print ("""
Success! All your base code are belong to us...
Just kidding.")
