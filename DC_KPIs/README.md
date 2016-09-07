# Python Demonstration

### In the beginning, there was nothing...

Prior to 27 August 2016, I had no knowledge of how to code in Python.

Over the course of two weekends, I studied what resources I could find in order
to start building an understanding. The resulting project was the DC_KPIs tool.

Studying a new (spoken) language becomes easier when one has previously studied
another language. One gains an awareness of the general structures and
underlying principles of language. The same can be true with code;
'tis but language of another kind. The words may change, but the ideas are the
same. In my case, the prior languages were VBA for Excel and R.

The intent of this project is to demonstrate initial competency in Python,
with the understanding that there is always more one can learn. After all,
each of us will ideally continue to learn throughout our lives.


### DC_KPIs tool

##### Objective:
1.  Compile data on key performance indicators (KPIs) reported by the
District of Columbia for different fiscal years.
2.  Extract the KPIs pertaining to a specified budget program.
3.  Save out the results in a CSV file for additional processing by the user.

#### Setup:
1.  Download KPI data for the available fiscal years from the following address:
    <http://opendata.dc.gov/datasets?keyword=Performance>
2.  Keep the default file name:
    'DC_Agency_Performance_Data_KPIs__'and the fiscal year.
3.  Ensure the KPI data and Python script are saved in the same directory.

#### Running the script:
You will see a series of prompts after executing the code.

1.  Confirm that the KPI data files are properly located and ready to begin.
    * 'N' exits the program
    * 'Y' proceeds through the program
2.  Enter the fiscal years for which you want to compile the data,
    separating each year by a space.
3.  Enter the name of the budget program for which you would like data.
    * Some examples include 'Urban Forestry Administration' or
    'Homeless Services Program'.
    * More programs can be found by viewing the Program/Activity detail at
    <http://cfoinfo.dc.gov/cognos/finance.htm> or enter <http://bit.ly/1Cyx2ME>
    to go directly to the tool.
4.  Once done, a message will indicating the name of the output file.

### Feedback is welcome
This is merely a first effort. I invite any feedback, whether on this project
in particular or with writing Python code in general.

Thank you!
