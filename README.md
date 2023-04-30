# WhatsappMessageSender

**WhatsappMessageSender** is a Python toolkit for managing contacts and sending WhatsApp messages on WhatsApp Desktop App.

## Usage

### GUI

You can use `gui.py` to add or remove contacts from your `contact.json` file by running the following command in your terminal:
```cmd
python gui.py
```

### Contacts

To find a contact's phone number, use the `find_phone_number(name, file_path)` function from `contacts.py`. This function takes a name and a file path for the `contact.json` file and returns the contact's phone number.

Here's an example of how to import `find_phone_number`:

```python
from contacts import find_phone_number
```

### Sending messages

To send a WhatsApp message, use the `send(name, message, waiting_time)` function from `whatsapp.py`. This function takes the name of the contact you want to send the message to, the message itself, and a waiting time in seconds before sending the message.

Here's an example of how to import `send`:

```python
from whatsapp import send
```

To send a message, use the following code:

```python
name = "Name 1"
message = "Hello, World!"
waiting_time = 2  # seconds

send(name, message, waiting_time)
```

This will send a WhatsApp message from your device's WhatsApp Desktop App.

## Contact Format

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

## Use Cases
- If you don't want to create a WhatsApp API key, this toolkit provides a simple and easy way to send messages using your WhatsApp Desktop app.
- It is a great tool for automation as you can send messages to multiple contacts with just a few lines of code.
- Since you can only send messages to people specified in the contact.json file, this toolkit provides an added layer of security and helps prevent the risk of sending messages to the wrong person by mistake.

### Note - This works if you have Whatsapp Desktop Installed.
