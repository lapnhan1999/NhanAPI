'''
#TASK 3
#Target: The Post API contains data in JSON format which is the information in item 2
import requests

#Get url
url = "https://afg.softworldvietnam.com/api/v1/Store/Areas"

#Get data from url
data = requests.get(url).json()

#Data reduction
list_data = data['result']['storeArea']

#Create list of Names and brandCodes
name = []
code = []
for i in range(len(list_data)):
    name.append(list_data[i]['name'])
    code.append(list_data[i]['brandCode'])


#Create a dictionary of the data you have obtained
x = []
y = []
for i in range(len(list_data)):
    x.append(list_data[i].get('name'))
    y.append(list_data[i].get('brandCode'))

arr = []
for i,j in zip(x,y):
    dict1 = {"Name" : i, "brandCode" : j}
    arr.append(dict1)

#Returns data as dictionary
from django.http import JsonResponse
def index(request):
    return JsonResponse({"": arr})
'''

#Task 4
#Target: The Post API contains JSON data in the apiModel.png pattern
import requests
url = "https://afg.softworldvietnam.com/api/v1/Store/Areas"
data = requests.get(url).json()
list_data = data['result']['storeArea']
name = []
code = []
for i in range(len(list_data)):
    name.append(list_data[i]['name'])
    code.append(list_data[i]['brandCode'])


url = "http://127.0.0.1:8000/"
myName = "Nhan"
data = {
    "set_attributes": {
        "Name": name,
        "BrandCode": code
    },
    "message": [
        {"text" : myName},
        {"attachment": {
            "type": "image",
            "payload":{
                "url" : url
            }
        }}
    ]
}



from django.http import JsonResponse
def index(request):
    return JsonResponse(data)




