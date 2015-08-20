import unittest

from constantcontact import Account_Info, Contact, Event

class Test_Event(unittest.TestCase):
    def test_event_init_from_dict(self):
        event = Event({'id': '123456', 'name': 'Name Goes Here'})

        self.assertEqual(event.get_name(), 'Name Goes Here')

    def test_event_contact(self):
        event = Event()

        contact = Contact()

        contact.set_prefix_name('Prof.')
        contact.set_last_name('Oak')

        event.set_contact(contact)

        self.assertEqual(event.get_contact()['name'], 'Prof. Oak')

        account_info = Account_Info()

        account_info.set_first_name('Gary')
        account_info.set_last_name('Oak')

        event.set_contact(account_info)

        self.assertEqual(event.get_contact()['name'], 'Gary Oak')

        event.delete_contact()

        self.assertEqual(event.get_contact(), None)

if __name__ == '__main__':
    unittest.main()
