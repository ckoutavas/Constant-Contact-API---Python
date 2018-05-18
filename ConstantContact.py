import requests



class ConstantContact(object):
    """
    ConstantContact uses the requests package with the constant contact api
    to prefrom various GET and POST requests
    """
    def __init__(self, api_key, token, originating_ip):
        self.api_key = api_key
        self.token = token
        self.originating_ip = originating_ip
        self.file_name = None
        self.list_id = None
        self.types = None

    def add_contacts(self, file_name, list_id, types=None):
        """
        add_contacts uses the requests module to post a file

        it uses the constant contact addcontacts api and passes your headers, which contains
        your access token, X-Originating-Ip and the content-type

        the dict POSTed must contain file_name, data and lists

        returns the http response and the response text

        """
        self.file_name = file_name
        self.list_id = list_id
        self.types = types
        uri = 'https://api.constantcontact.com/v2/activities/addcontacts?api_key='+self.api_key
        headers = {'Authorization': 'Bearer '+self.token, 'X-Originating-Ip': self.originating_ip,
                   'content-type': 'multipart/form-data'}

        for i in self.list_id:
            files = {'file_name': self.file_name,
                     'data': (self.file_name, open(self.file_name, 'rb'),
                              'application/vnd.ms-excel',
                              {'Expires': '0'}),
                     'lists': i}
        response = requests.post(uri, headers=headers, files=files)
        if self.types is None:
            return(response, response.json())
        if self.types == 'text':
            return(response, response.text)

    def get_mailing_lists(self, types=None):
        """
        get_mailing_list uses a GET request to gather mailing list information

        it uses the constant contact lists api and passes your headers, which contains
        your access token, X-Originating-Ip and the content-type

        returns a json response by default but using the argument types=text8 you can
        return response.text

        """
        self.types = types
        uri = 'https://api.constantcontact.com/v2/lists?api_key='+self.api_key
        headers = {'Authorization': 'Bearer '+self.token, 'X-Originating-Ip': self.originating_ip}
        response = requests.get(uri, headers=headers)
        if self.types == 'json':
            return response.json()
        if self.types == 'text':
            return response.text
        if self.types is None:
            return response.json()

    def bulk(self, types=None):
        """
        bluk uses a GET request to gather the bulk activites api response

        it uses the constant contact Activities api and passes your headers, which contains
        your access token, X-Originating-Ip and the content-type

        returns a json response for all bulk activiteies for the day the default is
        json but using the argument types=text you can return response.text

        """
        self.types = types
        uri = 'https://api.constantcontact.com/v2/activities?api_key='+self.api_key
        headers = {'Authorization': 'Bearer '+self.token, 'X-Originating-Ip': self.originating_ip}
        response = requests.get(uri, headers=headers)
        if self.types == 'json':
            return response.json()
        if self.types == 'text':
            return response.text
        if self.types is None:
            return response.json()
        