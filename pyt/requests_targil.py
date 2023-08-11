import requests


url_list = open("/home/alex/pyt/site_list.txt", "r")

def get_url_status(list):
    try:
        for url in list:
            status = requests.get(url)
            if status.status_code == 200:
                print('\x1b[6;30;42m' + 'Success!!' + '\x1b[0m' '  The URL :' ,  url, 'and the status is:'+ '\x1b[6;30;42m' + str(status.status_code) + '\x1b[0m')

            elif status.status_code == 404:
                print('\x1b[6;30;43m' + 'Failure!!' + '\x1b[0m' '  The URL :',  url, 'is unreachable the status code is:' + '\x1b[6;30;41m' +  str(status.status_code) +  '\x1b[0m')    
    
    except:
        print('\x1b[6;30;41m' + 'Failure!!' + '\x1b[0m' '  The URL :',  url, 'Has an Unknown Error, the Status Code is:' + '\x1b[6;30;41m' +  str(status.status_code) +  '\x1b[0m')    


get_url_status(url_list.read().split("\n"))       

