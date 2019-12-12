
########### Generate a offenses report from Qradar ########
########### Author: Nadav Yarkon #############
    ### For Educational Purposes Only ###

#Date: 01.12.18
#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon



import Connection
from datetime import datetime, timedelta
from Offense_Object import Offense


def ParseOffancesToDict(json_data):
    dictDomain={}
    Offenses=[]
    for element in json_data:

        domainId = element['domain_id']
        id = element['id']
        status = element['status']
        desc = element['description'][:-1]
        obj = Offense(id, desc, status, domainId)
        if domainId in dictDomain.keys():
            dictDomain[domainId].append(obj)
        else:
            dictDomain[domainId] = []
            dictDomain[domainId].append(obj)
    return dictDomain


def AddNote(dictDomain):
    for val in dictDomain.values():
        fillNoteToArray(val)
    return dictDomain

def fillNoteToArray(val):
        notes=[]
        for i in val:
            notes=Connection.Connect_To_API_Note(i.getID())
            for note in notes:
                i.addNote(note['username']+": "+note['note_text'])
            notes.clear()

def date_to_millisecond(day):
    date_N_days_ago = datetime.now() - timedelta(days=day)
    return AddNote(ParseOffancesToDict(Connection.Connect_To_API(datetime_to_float(date_N_days_ago))))


def datetime_to_float(d):
    epoch = datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    return int(round(total_seconds *1000))

