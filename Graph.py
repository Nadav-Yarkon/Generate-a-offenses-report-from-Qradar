
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


def fillArr(arrVal,dict):
        for key, val in dict.items():
            domain = Connection.Connect_To_API_DomainID(str(key))
            name=domain['name']
            if  not name:
                name = "Cloude"
            arrVal[name]=len(val)
        return  arrVal


def graph(dict):
    arrVal={}
    arrVal=fillArr(arrVal,dict)
    n_groups = len(arrVal)
    means_men = (arrVal.values())
    arr=[]
    arr=[0.3]*dict.__len__()
    std_men=(arr)
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = ax.bar(index, means_men, bar_width,
                    alpha=opacity, color='b',
                    yerr=std_men, error_kw=error_config,
                    label='By week')
    ax.set_xlabel("Domain")
    ax.set_ylabel('Count')
    ax.set_title('Weekly offense count')
    ax.set_xticks(index + bar_width / 2)

    ax.set_xticklabels(arrVal.keys())
    ax.legend()
    fig.tight_layout()
    plt.show()
    
