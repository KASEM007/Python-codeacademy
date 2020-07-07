class message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


class User:
    def __init__(self, user_name):
        self.user_name = user_name

    def edit_message(self, message, new_text):
        if message.sender == self.user_name:
            message.trxt = new_text


class Admin(User):
    def edit_message(self, message, new_text):
        if message.sender != self.user_name:
            try:
                message.text = new_text
            except User:
                print("Do Something")

