from clicksend_client import SmsMessage

# Create an instance of SmsMessage
sms_message = SmsMessage(
    source="python",
    body="Hello, this is a test SMS.",
    to="+61 MOBILE NUMBER HERE"
)
