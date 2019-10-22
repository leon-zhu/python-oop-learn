class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class LongNameDict(dict):
    def longest_key(self):
        longest = None
        # dict本身只支持key的迭代
        for key in self:
            print(key)
            if not longest or len(key) > len(longest):
                longest = key
        return longest


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("Send {0} order to {1}".format(order, self.name))


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)


class EmailableContact(Contact, MailSender):
    pass
