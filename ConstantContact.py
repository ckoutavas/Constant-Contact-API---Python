import requests


class ConstantContact(object):
    """
    ConstantContact uses the requests package with the constant contact api
    to preform various GET and POST requests
    """

    def __init__(self, api_key, token, originating_ip):
        self.api_key = api_key
        self.token = token
        self.originating_ip = originating_ip
        self.file_name = None
        self.list_id = None
        self.res_type = None
        self.campaign_id = None
        self.campaign_uri = 'https://api.constantcontact.com/v2/emailmarketing/campaigns?api_key=' + self.api_key

    def add_contacts(self, file_name, list_id, res_type=None):
        """
        add_contacts uses the requests module to post a file

        it uses the constant contact bulk activities api and passes your headers, which contains
        your access token, X-Originating-Ip and the content-type

        the dict POSTed must contain file_name, data and lists

        :param file_name: the name of the csv file to POST
        :param list_id: the list ID of the mailing list you want to post the file to
        :param res_type: this is the response type. it is defaulted to json but will take 'text' or 'json'
        :return: returns the POST response
        """

        self.file_name = file_name
        self.list_id = list_id
        self.res_type = res_type

        uri = 'https://api.constantcontact.com/v2/activities/addcontacts?api_key=' + self.api_key
        headers = {'Authorization': 'Bearer ' + self.token, 'X-Originating-Ip': self.originating_ip,
                   'content-type': 'multipart/form-data'}

        for i in tuple(self.list_id):
            files = {'file_name': self.file_name,
                     'data': (self.file_name, open(self.file_name, 'rb'),
                              'application/vnd.ms-excel',
                              {'Expires': '0'}),
                     'lists': i}
            response = requests.post(uri, headers=headers, files=files)
            print(response, 'for:', i)

        if self.res_type == 'json':
            return response.json()
        if self.res_type == 'text':
            return response.text
        if self.res_type is None:
            return response.json()

    def get_mailing_lists(self, res_type=None):
        """
        get_mailing_list uses a GET request to gather mailing list information

        it uses the constant contact lists uri and passes your headers, which contains
        your access token, X-Originating-Ip and the content-type

        :param res_type: this is the response type. it is defaulted to json but will take 'text' or 'json'
        :return: returns the GET response
        """

        self.res_type = res_type

        uri = 'https://api.constantcontact.com/v2/lists?api_key=' + self.api_key
        headers = {'Authorization': 'Bearer ' + self.token, 'X-Originating-Ip': self.originating_ip}
        response = requests.get(uri, headers=headers)

        if self.res_type == 'json':
            return response.json()
        if self.res_type == 'text':
            return response.text
        if self.res_type is None:
            return response.json()

    def bulk(self, res_type=None):
        """
        bulk uses a GET request to gather the bulk activities api responses

        it uses the constant contact bulk activities api and passes your headers, which contains
        your access token, X-Originating-Ip and the content-type

        :param res_type: this is the response type. it is defaulted to json but will take 'text' or 'json'
        :return: returns the GET response
        """

        self.res_type = res_type

        uri = 'https://api.constantcontact.com/v2/activities?api_key=' + self.api_key
        headers = {'Authorization': 'Bearer ' + self.token, 'X-Originating-Ip': self.originating_ip}
        response = requests.get(uri, headers=headers)

        if self.res_type == 'json':
            return response.json()
        if self.res_type == 'text':
            return response.text
        if self.res_type is None:
            return response.json()

    def account(self, res_type=None):
        """
        account uses a GET request to gather account information

        :param res_type: this is the response type. it is defaulted to json but will take 'text' or 'json'
        :return: returns al your account information
        """

        self.res_type = res_type

        uri = 'https://api.constantcontact.com/v2/account/info?api_key=' + self.api_key
        headers = {'Authorization': 'Bearer ' + self.token, 'X-Originating-Ip': self.originating_ip}
        response = requests.get(uri, headers=headers)

        if self.res_type == 'json':
            return response.json()
        if self.res_type == 'text':
            return response.text
        if self.res_type is None:
            return response.json()

    def get_campaigns(self):
        """
        get_campaigns uses a GET request to gather all campaign information
        Must be json response

        :return: returns campaign information but the limit is 50 use next_link() to get the next 50
        """

        headers = {'Authorization': 'Bearer ' + self.token, 'X-Originating-Ip': self.originating_ip}
        response = requests.get(self.campaign_uri, headers=headers)

        return response.json()

    def next_link(self):
        """
        next link will allow you to view all your campaigns 50 results at a time

        this will raise a key error if next_link cannot be found in the json response

        :return: returns the new uri for get_campaigns

        sample code:
        cc = ConstantContact(x,y,z)
        cc.campaign_uri = cc.next_link()
        cc.get_campaigns()

        """
        data = self.get_campaigns()
        next_link = data['meta']['pagination']['next_link'].split('next=')[1]
        uri = 'https://api.constantcontact.com/v2/emailmarketing/campaigns?api_key=' + self.api_key + '&next=' + next_link

        return uri

    def unique_campaign(self, campaign_id, res_type=None):
        """
        unique_campaign uses GET a GET request to gather single campaign information

        :param campaign_id: the campaign id for the campaign you want to return
        :param res_type: this is the response type. it is defaulted to json but will take 'text' or 'json'
        :return: returns the GET response
        """

        self.campaign_id = campaign_id
        self.res_type = res_type

        uri = 'https://api.constantcontact.com/v2/emailmarketing/campaigns/'+self.campaign_id+'?api_key='+self.api_key
        headers = {'Authorization': 'Bearer ' + self.token, 'X-Originating-Ip': self.originating_ip}
        response = requests.get(uri, headers=headers)

        if self.res_type == 'json':
            return response.json()
        if self.res_type == 'text':
            return response.text
        if self.res_type is None:
            return response.json()

