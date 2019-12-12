########### Generate a offenses report from Qradar ########
########### Author: Nadav Yarkon #############
    ### For Educational Purposes Only ###

#Date: 01.12.18
#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon


import Qradar
import WriteDocx
import Graph
import CnvertDicOpenClose
import GraphOpenClose


def Start(milisecounds):
    print("Now a word file is created in the current directory.")
    print()
    dict = Qradar.date_to_millisecond(int(milisecounds))
    ocdict=CnvertDicOpenClose.CnvertDicOpenClose(dict)
    WriteDocx.crateWordFile(dict,ocdict)
    print("Offense_Weekly.docx created in the current directory.")
    print()
    print("Now a Graph created.")
    print()
    Graph.graph(dict)
    print ("Now a second Graph created.")
    GraphOpenClose.graphOpenClose(ocdict,dict)


import argparse

parser = argparse.ArgumentParser(description='The program provides information from Qradar.\n '
                                             'She introducing the data in In various forms(such as offense  report and graphs)')
parser.add_argument("-d", "-day" , metavar='' , required=True , help= "Enter a few days back you would like to view" , type=int)
parser.parse_args()
args = parser.parse_args()
Start(args.d)