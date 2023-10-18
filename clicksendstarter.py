from __future__ import print_function
import time
import clicksend_client
from clicksend_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = clicksend_client.Configuration()
configuration.username = 'CLICK SEND USERNAME HERE'
configuration.password = 'CLICK SEND API KEY HERE'

# create an instance of the API class
api_instance = clicksend_client.AccountApi(clicksend_client.ApiClient(configuration))

try:
    # Get account information
    api_response = api_instance.account_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get: %s\n" % e)
