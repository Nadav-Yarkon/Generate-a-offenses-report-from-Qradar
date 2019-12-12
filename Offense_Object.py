
########### Generate a offenses report from Qradar ########
########### Author: Nadav Yarkon #############
    ### For Educational Purposes Only ###

#Date: 01.12.18
#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon


class Offense:


    def __init__(self, id, desc , status, domainId, domainName="non",domainDec="non"):
        self.id = id
        self.desc = desc
        self.status=status
        self.domainId=domainId
        self.notes = []
        self.domainName=domainName
        self.domainDec=domainDec

    def addNote(self,note):
        self.notes.append(note)

    def getNote(self):
        return self.notes

    def getID(self):
        return self.id

    def getDesc(self):
        return self.desc

    def getStatus(self):
        return self.status

    def getDomain(self):
        return self.domainId

    def getDomainName(self):
        return self.domainName

    def getdomainDec(self):
        return self.domainDec

