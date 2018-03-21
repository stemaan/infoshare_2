class Contact:
    contacts_no = 0
    last_id = 0

    def __init__(self, name, lastname):
        Contact.last_id += 1
        self.id = Contact.last_id
        self.name = name
        self.lastname = lastname
        Contact.contacts_no += 1

    def full_name(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return f'ID: {self.id} Name: {self.name} Lastname: {self.lastname}'

    def __repr__(self):
        return f'Contact({self.name}, {self.lastname})'

    def __del__(self):
        print('called')
        Contact.contacts_no -= 1


if __name__ == '__main__':
    from pprint import pprint


    c = Contact('Jan', 'Kowalski')
    c2 = Contact('Adam', 'Nowak')
    print(c)
    print(c2)
    contacts = [c, c2]
    pprint(contacts)
    del contacts[1]
    pprint(contacts)
    print(Contact.contacts_no)