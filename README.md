# Generate-a-offenses-report-from-Qradar
Written in python 3 and cross platform, generate a report with information about the offenses from Qradar in the last days (you determine how many days ago). 
When you run the Run.py file (he runs all the python files), You need to determine how many days you want to collect data.

Parameters: 

-d : Enter how many days back you would like to view. 
-h / --help : help.

This program is divided into three parts:
1) Export word file with all the offenses divided into domains, and additional information about these offenses like description, status, all notes, etc.
2) A graph with all offenses that were opened in the date that predetermined.
3) A graph with all offenses that were opened and closed in the date that predetermined.

In the first time, run Install.py file for install all library.
In the file connection.py, you have to change the IP of Qradar and API key.

example for a run:

python run.py --help.
python run.py -d 3. 
