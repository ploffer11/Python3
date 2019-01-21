class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name = "", email="", **kwargs):
        super().__init__(**kwargs)
        self.name, self.email = name, email
        Contact.all_contacts.append(self)

class AddressHolder:
    def __init__(
        self, street = "", city = "", state = "", code = "", **kwargs):
        super().__init__(**kwargs)
        self.street, self.city, self.state, self.code = (
            street, city, state, code 
            )

class Friend(Contact, AddressHolder):
    """ 
    Args :
        phone (str) : phone number

    Kwargs :
        name (str) : name
        email (str) : email address
        street (str), city (str), state (str) : address
        code (str) : etc.

    """
    def __init__(self, phone = "", **kwargs):
        kwargs.update( { "phone" : phone })
        super().__init__(**kwargs)
        self.phone = phone

class Supplier(Contact):
    def order(self, order):
        print(
            "If this were a real system we would "
            f"'{order}' order to '{self.name}'"
        )


class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)

class EmailableContact(Contact, MailSender):
    pass



"""
c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email, s.name, s.email)
print(c.all_contacts)
#c.order("I need pliers")
s.order("I need pliers")
"""

c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jenna@example.net")
 
print( [c.name for c in Contact.all_contacts.search("John")] )

e = EmailableContact("John Smith", "jsmith@example.net")
e.send_mail("Hello, test e-mail here")

f = Friend()