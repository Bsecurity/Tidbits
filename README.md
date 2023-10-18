SMS Fantasy Fact Sender

Send random facts as SMS to your recipients using the ClickSend API!
Features:

    Easy Configuration: Use a simple config file to setup your ClickSend credentials and recipient phone number.
    Random Fact Generator: Automatically selects a random fact from a provided list to send.
    Logging System: Keeps track of sent facts to prevent repetition.
    Error Handling: Built-in handling for potential ClickSend API errors.

Pre-requisites:

    Python3: Ensure you have Python3 installed on your machine. You can download and install it from Python's official site.
    https://www.python.org/downloads/

    Visual Studio Code (Recommended): We recommend using Visual Studio Code (VS Code) as the code editor for this project. It offers a rich development environment with support for Python.
    Download VS Code 
    https://code.visualstudio.com/download
    
    After installation, add the Python extension for VS Code to get enhanced support for Python development.
    https://marketplace.visualstudio.com/items?itemName=ms-python.python

    ClickSend Account: Make sure you have a ClickSend account with relevant API credentials. You can sign up on their official site
    https://www.clicksend.com/

Setup:

    Clone the Repository:
    git clone https://github.com/Bsecurity/Tidbits.git

Install ClickSend Client:

    pip install clicksend_client

Configure:

    Update config.py with your ClickSend username, API key, and the recipient phone number.

Usage:

    Run the Script:
    python3 Tidbits.py

A random fact from facts.txt will be sent to the specified recipient via SMS.

The sent fact will be logged in sent_facts.txt.

Customization:

    Custom Implementation: The project also allows for the integration of a custom ClickSend client (my_clicksend_client). This can be further expanded upon based on your needs.

Error Handling:

The script has built-in error handling for the ClickSend API. If there's an issue while trying to send the SMS, it will be printed to the console.
Contributing:

Feel free to fork the repository and submit pull requests! All contributions are welcome.
