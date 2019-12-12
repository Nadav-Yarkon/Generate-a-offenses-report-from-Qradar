
########### Generate a offenses report from Qradar ########
########### Author: Nadav Yarkon #############
    ### For Educational Purposes Only ###

#Date: 01.12.18
#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon


import requests
import urllib3

def Connect_To_API(milisecounds):
    urllib3.disable_warnings()
    BASE_URL = 'https://#####<Enter Qradar IP>#######/api/siem/offenses?filter=start_time%3E%3D%22'+str(milisecounds)+'%22'
    headers = {
        'SEC': '#####<Enter Qradar key of API>#######'
    }
    url = BASE_URL
    json_data = requests.get(url, headers=headers, verify=False).json()
    return json_data


def Connect_To_API_Note(IdOffense):
    urllib3.disable_warnings()
    BASE_URL = 'https://#####<Enter Qradar IP>#######/api/siem/offenses/'+str(IdOffense)+'/notes'
    headers = {
        'SEC': '#####<Enter Qradar key of API>#######'
    }
    url = BASE_URL
    json_data = requests.get(url, headers=headers, verify=False).json()
    return json_data


def Connect_To_API_DomainID(domainID):
    urllib3.disable_warnings()
    BASE_URL = 'https://#####<Enter Qradar IP>#######/api/config/domain_management/domains/'+domainID
    headers = {
        'SEC': '#####<Enter Qradar key of API>#######'
    }
    url = BASE_URL
    json_data = requests.get(url, headers=headers, verify=False).json()
    return json_data
