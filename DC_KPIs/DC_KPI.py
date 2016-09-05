# This program compiles KPIs (key performance indicators), reported by the
# government of the District of Columbia, for the selected year and budget
# program. The result is saved to a CSV file for additional processing.

import csv
import sys

#def source_file(year):
#    return """open('DC_Agency_Performance_Data_KPIs__%s.csv', 'rb')""" % year

def set_KPI_data(year):
    filestring = 'DC_Agency_Performance_Data_KPIs__%s.csv' % year
    source_file = open(filestring, 'rb')
    source_data = csv.reader(source_file)
    return source_data

# Confirm source files are properly staged.
prep_check = raw_input("""Please ensure source files are in the same directory as this script.
Are you ready to proceed?
'Y' or 'N'>>>""")

# If source files are not staged, the script will close.
# If ready, then the user is prompted to enter list of reporting years.
if prep_check == 'Y':
    year_input = raw_input('Enter reporting years to compile, separated by a space.>>>')
    year_list = year_input.split(' ')
else:
    print ("Please have all relevant files prepared before proceeding.")
    exit(0)

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
range_end = len(year_list)

for i in range (0, range_end):
    reporting_year = year_list[i]
    print "Processing %s" % reporting_year
    KPI_data = set_KPI_data(reporting_year)

    for row in KPI_data:
        if row[17] == budget_program:
            program_compiled.append(row)
    i =+ 1


# Results saved to CSV.
output_string = 'DC_Performance_KPIs_%s.csv' % budget_program
output_path = open(output_string,'wb')
output_file = csv.writer(output_path)
output_file.writerows(program_compiled)
print """Results are saved to DC_Performance_KPIs_%s.csv""" % budget_program

print ("""
Success! All your base code are belong to us...
Just kidding.
I've been wanting to use that line for a while.""")
