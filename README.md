# Constant-Contact-API---Python

This uses the Constant Contact API to get email list IDs and add contacts to mailing list from a file. To POST files, 
it utilizes the Bulk Activites API.

```

import requests

class cc(object):
    def __init__(self, api_key, token, Originating_Ip):
        self.api_key = api_key
        self.token = token
        self.Originating_Ip = Originating_Ip

    def add_contacts(self, file_name, list_id):
        self.file_name = file_name
        self.list_id = list_id
        uri = 'https://api.constantcontact.com/v2/activities/addcontacts?api_key='+self.api_key
        headers = {'Authorization': 'Bearer '+self.token,'X-Originating-Ip': self.Originating_Ip, 'content-type': 'multipart/form-data'}
        files = {'file_name': self.file_name, 
         'data': (self.file_name, open(self.file_name, 'rb'), 'application/vnd.ms-excel', {'Expires': '0'}),
         'lists':(self.list_id)}
        response = requests.post(uri, headers=headers, files=files)
        return(response, response.text)
    
    def get_mailing_lists(self):
        uri = 'https://api.constantcontact.com/v2/lists?api_key='+self.api_key
        headers = {'Authorization': 'Bearer '+self.token,'X-Originating-Ip': self.Originating_Ip}
        response = requests.get(uri, headers=headers)
        return response.json()
       
```      
        
        

# how to return your mailing lists and mailing list IDs:
```
CC = cc(api_key = 'your_api_key', token = 'your_access_token', Originating_Ip = 'your_X-Originating-Ip')
CC.get_mailing_lists()
```

# how to POST a csv file of contacts to a mailing list:

note your file headers need to be formated correctly. 
Visit http://developer.constantcontact.com/docs/bulk_activities_api/bulk-activities-import-contacts.html
and look at Structure to see appropiate file headers

```
CC = cc(api_key = 'your_api_key', token = 'your_access_token', Originating_Ip = 'your_X-Originating-Ip')
CC.add_contacts(file_name = 'your_file.csv', list_id = 'your_list_id')
```
