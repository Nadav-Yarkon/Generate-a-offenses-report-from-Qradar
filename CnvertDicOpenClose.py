
def CnvertDicOpenClose(dict):
    arrOpenClose=[]
    open=0
    close=0
    arrClose=[]
    arrOpen=[]
    for key, val in dict.items():
        open=0
        close=0
        for index in val:
            if  index.getStatus() == 'OPEN':
                open=open+1
            else:
                close=close+1
        arrOpen.append(open)
        arrClose.append(close)


    arrOpenClose.append(arrOpen)
    arrOpenClose.append(arrClose)
    return arrOpenClose










