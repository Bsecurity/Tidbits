import clicksend_client                                # Importing necessary modules from the clicksend package to send SMS.
from clicksend_client import SmsMessage, SmsMessageCollection
from config import CLICKSEND_USERNAME, CLICKSEND_PASSWORD, RECIPIENT_PHONE_NUMBER
from my_clicksend_client import SmsMessage             # Importing custom implementation of the clicksend client.
from clicksend_client.rest import ApiException         # To handle exceptions from the Clicksend API.
import time                                            # Importing time module for potential pauses or delays in the script.
import random                                          # Importing random moudle for adding randomness.

# Read facts from facts.txt
with open("facts.txt", "r") as file:
    facts = [line.strip() for line in file.readlines()]

# Define the send_sms function
def send_sms(message):
    configuration = clicksend_client.Configuration()     # Create a configuration object for the Clicksend API.
    configuration.username = CLICKSEND_USERNAME          # Set the username for the API from the config file.
    configuration.password = CLICKSEND_PASSWORD          # Set the password for the API from the config file.

    # Create an API instance using the configuration.
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
    # Define the sender name for the SMS.
    business_name = "TIDBITS"

    sms_message = SmsMessage(       # Create an SMS message object with necessary details.
        source="python",            # The source is set as "python".
        body=message,               # The body of the SMS is the message passed to the function.
        to=RECIPIENT_PHONE_NUMBER,  # The recipient is defined in the config.
        _from=business_name         # The sender's name is set to the business name.
    )
    # Convert the SMS message object into a collection. This is required by the API.
    sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])
    # Try to send the SMS using the API.
    try:
        api_response = api_instance.sms_send_post(sms_messages)         # If successful, print the API response.
        print(api_response)
    # If there's an exception (an error) while trying to send the SMS, catch it.
    except ApiException as e:
        print("Exception when calling SMSApi->sms_send_post: %s\n" % e) # Print the exception message.


def send_random_fact():
    """Select a random fact, assign a random number, and send it as SMS."""
    # Select a random fact
    fact = random.choice(facts)
    # Generate a random number between 2500 and 50000
    fact_number = random.randint(2500, 50000)
    # Combine the number and fact for the message
    message = f"Fact {fact_number}: {fact}"
    
    # Log the sent fact to the sent_facts.txt file
    with open("sent_facts.txt", "a") as file:
        file.write(message + "\n")

    # Ensure the fact is not sent twice by removing it from the list
    facts.remove(fact)
    
    # Send the fact as SMS
    send_sms(message)  

# Run the function to send a random fact
send_random_fact()

