# WhatsappMessageSender

**WhatsappMessageSender** is a Python toolkit for managing contacts and sending WhatsApp messages on WhatsApp Desktop App.

Contacts are saved in `contact.json` file in the following format:

```json
[
    {
        "name": "Name 1",
        "phone": "101010101"
    },
    {
        "name": "Name 2",
        "phone": "1111111111"
    }
]
```

## Usage

### GUI

`gui.py` file is provided for you to enter and delete contacts from `contact.json` file.
```cmd
python ./gui.py
```

### Contacts

`contacts.py` module provides `find_phone_number(name, file_path)` function which takes name and file path for `contact.json` file. This function returns only the number if it exists in the `contact.json`. 

To import `find_phone_number`, use the following code:

```python
from contacts import find_phone_number
```

### Sending messages

`whatsapp.py` module provides `send(name, message, waiting_time)` function which takes name, message, and waiting time in seconds before sending the message. 

To import `send`, use the following code:

```python
from whatsapp import send
```

## Example

To send a WhatsApp message, use the following code:

```python
from whatsapp import send

name = "Name 1"
message = "Hello, World!"
waiting_time = 2  # seconds

send(name, message, waiting_time)
```

This will send a WhatsApp message from your device's WhatsApp Desktop App.

## Use Cases
- If you don't want to create a WhatsApp API key, this toolkit provides a simple and easy way to send messages using your WhatsApp Desktop app.
- It is a great tool for automation as you can send messages to multiple contacts with just a few lines of code.
- Since you can only send messages to people specified in the contact.json file, this toolkit provides an added layer of security and helps prevent the risk of sending messages to the wrong person by mistake.

### Note - This works if you have Whatsapp Desktop Installed.
