from __future__ import print_function
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException

# Configure HTTP basic authorization: BasicAuth
configuration = clicksend_client.Configuration()
configuration.username = 'CLICK SEND USERNAME HERE'
configuration.password = 'CLICK SEND API KEY HERE'

# create an instance of the API class
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

# Set the business name
business_name = "TIDBITS"

# Create an instance of SmsMessage
sms_message = SmsMessage(
    source="python",
    body="",
    to="+61 MOBILE NUMBER HERE",
    schedule=1436874701,
    _from=business_name  # Set the business name here
)

# Create SmsMessageCollection
sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

try:
    # Send sms message(s)
    api_response = api_instance.sms_send_post(sms_messages)
    print(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
