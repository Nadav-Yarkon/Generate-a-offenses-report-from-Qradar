
########### Generate a offenses report from Qradar ########
########### Author: Nadav Yarkon #############
    ### For Educational Purposes Only ###

#Date: 01.12.18
#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon


import numpy as np
import matplotlib.pyplot as plt
import Connection
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


def fillZero(arrOC):
    newarr=[]
    for arr in arrOC:
        arr=list(arr)
        for index in range (len(arr)):
            if arr[index]  == 0:
                arr[index] = 0.01
        arr=tuple(arr)
        newarr.append(arr)
    return newarr


def fillArr(dict):
        arrVal={}
        for key, val in dict.items():
            domain = Connection.Connect_To_API_DomainID(str(key))
            name=domain['name']
            if  not name:
                name = "Cloude"
            arrVal[name]=len(val)
        return  arrVal


def graphOpenClose(arr,dict):
    arr=fillZero(arr)
    keys = fillArr(dict)
    n_groups = len(arr[1])

    means_men = arr[0]
    std_men = [0]*len(arr[1])

    means_women = arr[1]
    std_women = [0]*len(arr[1])

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, means_men, bar_width,
                    alpha=opacity, color='b',
                    yerr=std_men, error_kw=error_config,
                    label='Open')

    rects2 = ax.bar(index + bar_width, means_women, bar_width,
                    alpha=opacity, color='r',
                    yerr=std_women, error_kw=error_config,
                    label='Close')

    ax.set_xlabel('Domain')
    ax.set_ylabel('Count')
    ax.set_title('Open/Close offense group Domain')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(keys)
    ax.legend()

    fig.tight_layout()
    plt.show()



