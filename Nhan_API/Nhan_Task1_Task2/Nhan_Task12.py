#TASK 1:
#Target : Print out the names of the regions
'''
import requests
import json

#get url
url = "https://afg.softworldvietnam.com/api/v1/Store/Areas"

#get data from url
data = requests.get(url).json()

#get attributes of "storeArea"
list_data = data['result']['storeArea']

#print out all the name of the attributes of "storeArea"
for i in range(len(list_data)):
    print(i+1,"-",list_data[i]['name'])
'''

#Run task 2 have to comment task 1 and vice versa
#TASK 2
#Target : Print out the region names and the corresponding brandCode
import requests
from tabulate import tabulate
url = "https://afg.softworldvietnam.com/api/v1/Store/Areas"
data = requests.get(url).json()
list_data = data['result']['storeArea']

#Create list of Names and brandCodes
name = ['Name']
code = ['brandCode']
for i in range(len(list_data)):
    name.append(list_data[i]['name'])
    code.append(list_data[i]['brandCode'])

#Use tabulate to print out as the table type
print(tabulate([name, code], tablefmt="grid"))







