# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split the email addresses using regular expression pattern
        addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', self.email_addresses)
        # Remove duplicates and sort alphabetically
        unique_addresses = sorted(set(addresses))
        return unique_addresses
