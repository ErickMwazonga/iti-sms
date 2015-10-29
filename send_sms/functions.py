"""Class to send sms programmatically via smsgateway.me is defined here."""

#lib
import json
from django.http import request
import requests

#local
from send_sms.models import device

class SmsGateway(object):

    """Python equivalent class of the php sample given by smsgateway.me."""

    BASE_URL = "https://smsgateway.me"

    def loginDetails(self, email, password):
        """Each instance work with an email registered with the site.
           password for authentication.
        """
        self.email = email
        self.password = password

    def getMessages(self, page=1):
        """Get a list of all messages for this email."""
        return self.makeRequest('/api/v3/messages', 'GET', dict(page=page))

    def sendMessageToNumber(self, to, message, device, options={}):
        """Send message to given number, `to`.
        to: Phone number of the recipient as String.
        message: Message to be sent as String.
        device: Device ID (as String) registered with the site.
                message will be directed to it.
        options: A dict with any extra options, if required.
        """
        options.update({'number': to, 'message': message,
                        'device': device})
        return self.makeRequest('/api/v3/messages/send', 'POST', options)

    def sendMessageToManyNumbers(self, to, message, device, options={}):
        """Send messages to all numbers given. `to` is a list of numbers."""
        options.update({'number': to, 'message': message,
                        'device': device})
        return self.makeRequest('/api/v3/messages/send', 'POST', options)

    def makeRequest(self, url, method, fields):
        """Sends the request to server, parses & returns the response.

        url: Full url of the request api.
        method: "GET" or "POST".
        fields: dict with keys like, 'email', 'password', 'page', 'number',
                                     'message', 'device', etc.

        Returns a dict with keys, 'response' and 'status'.
        'response' value is a json dict as defined in site API docs.
        'status' represents the HTML response codes.
        """
        fields['email'] = self.email
        fields['password'] = self.password
        url = self.BASE_URL + url
        ret_dict = {}
        # Fields need not be encoded as in php sample.
        # requests library will take care of that.
        #
        # 1. CURLOPT_RETURNTRANSFER is not relevant here as result will always
        #    be returned, not printed.
        # 2. CURLOPT_HEADER not relevant as code takes care of returning the
        #    response text only.
        # 3. CURLOPT_SSL_VERIFYPEER is set to false with `verify=False` param.
        if method == "POST":
            resp = requests.post(url, data=fields, verify=False)
        else:
            resp = requests.get(url, params=fields, verify=False)
        # Response is obtained. Now build the return value out of it.
        try:
            ret_dict['response'] = resp.json()
        except ValueError: # If Response could not be parsed as json..
            try:
                ret_dict['response'] = json.loads(resp.text)
            except ValueError: # If Response body is not valid for json..
                ret_dict['response'] = resp.text
        ret_dict['status'] = resp.status_code
        return ret_dict


