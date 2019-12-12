
########### Generate a offenses report from Qradar ########
########### Author: Nadav Yarkon #############
    ### For Educational Purposes Only ###

#Date: 01.12.18
#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon


import WordAPI
import  Connection

doc = WordAPI.DocxAPI()
dict={}
sum=0


def partOne(dict,arrOpenClose):
        doc.header('Weekly Count Ofenses:')
        i=1
        sum=0
        for key, val  in dict.items()  :
            domain = Connection.Connect_To_API_DomainID(str(key))
            name=domain['name']
            if  not name:
                name = "Cloude"
            doc.writeText(str(i)+') '+ (name)  + ": " + str(len(val))+ "  (Open: " + str(arrOpenClose[0][i-1])+"     " + "Close: "+  str(arrOpenClose[1][i-1])+")"+'\n', None, 12,True)
            sum=sum+len(val)
            i=i+1

        doc.writeText('\n', None, 7)
        doc.writeText('\n', None, 7)
        doc.writeText("Total: "+str(sum) +'\n', None, 13)
        doc.writeText('\n', None, 7)
        doc.writeText('\n', None, 7)


def crateWordFile(dict,arrOpenClose):
    partOne(dict,arrOpenClose)
    doc.header('Here is the Details:')
    doc.writeText('\n',None,10)
    i=1
    sum=0
    for key, val in dict.items():
        domain = Connection.Connect_To_API_DomainID(str(key))
        sum=sum+len(val)
        doc.writeText('\n', None, 7)
        doc.writeText(str(i)+') '+ domain['name'] + "  dec: "+ domain['description']+'  sum: '+str(len(val))+'\n',None,12,True)
        doc.writeText("\n", None, 5)
        for index in val:
            if str(index.getID())== "6470":
                print("")
            doc.writeText("ID: " + str(index.getID()) + "  Status: " + index.getStatus()+"\n", None, 10)
            doc.writeText("desc: "+ index.getDesc()+'\n',None,10,True)
            doc.writeText("notes:"+"\n", None, 10)
            for note in index.getNote():
                n=(note.split("\n"))
                if len(n)>0:
                    for s in n:
                        doc.writeText("    * " + s + "\n", None, 10)
            doc.writeText('\n', None, 10)

        i=i+1

    doc.writeText('\n', None, 10)
    doc.writeText('\n', None, 10)
    doc.writeText('Total Offenses: ' + str(sum), None, 14)
    doc.saveFile("Offense_Weekly.docx")




