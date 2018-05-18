
This is a Constant Contact api wrapper that uses the Constant Contact API to GET various information out of Constant Contact and POST contact files to lists. For any of types atribute you can call a text response or a json response: types='text' or types='json' the default if type is None is a json response.


Calling the ConstantContact module:
```
from ConstantContact import ConstantContact
CC = ConstantContact(api_key='your_api_key', token='your_access_token', Originating_Ip='your_X-Originating-Ip')
```

How to get all your mailing list information and list ids:
```
CC.get_mailing_lists(types='json')
```

How to POST a csv file of contacts to a mailing list:

Note that your file headers need to be formated correctly. Visit http://developer.constantcontact.com/docs/bulk_activities_api/bulk-activities-import-contacts.html and look at Structure to see appropiate file headers

```
CC.add_contacts(file_name='your_file.csv', list_id=('your_list_id','your other list id'), types='json')
```

How to return the bulk activities response for all bulk actvites for the day:
```
CC.bulk(types='json')
```
