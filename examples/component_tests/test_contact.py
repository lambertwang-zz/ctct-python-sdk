import unittest

from constantcontact import Address, Contact, Contact_List, Email_Address

class Test_Contact(unittest.TestCase):
    def test_cont_init_from_dict(self):
        contact = Contact({'first_name': 'Dipper', 'last_name': 'Pines'})

        self.assertEqual(contact.get_first_name(), 'Dipper')

    def test_cont_setter_getter(self):
        contact = Contact()

        contact.set_first_name('Mabel')
        contact.set_last_name('Pines')
        contact.set_company_name('The Mystery hack')

        self.assertEqual(contact.get_job_title(), None)
        self.assertEqual(contact.get_first_name(), 'Mabel')
        self.assertEqual(contact.get_last_name(), 'Pines')

        contact.delete_last_name()

        self.assertEqual(contact.get_last_name(), None)

    def test_cont_email_address(self):
        contact = Contact()
        email_address = Email_Address()

        email_address.set_email_address('bill@example.com')

        self.assertEqual(contact.get_email_address(), None)

        contact.set_email_address(email_address)

        self.assertEqual(contact.get_email_address().get_email_address(), 'bill@example.com')


    def test_cont_address(self):
        contact = Contact()
        address = Address()

        address.set_state('Oregon')
        address.set_city('Gravity Falls')
        address.set_address_type('BUSINESS')

        self.assertEqual(contact.get_addresses(), None)

        contact.set_address(address)

        self.assertEqual(contact.get_address('BUSINESS').get_city(), 'Gravity Falls')
        
        contact.remove_address('PERSONAL')

        self.assertEqual(contact.get_address('BUSINESS').get_city(), 'Gravity Falls')

        contact.clear_addresses()

        self.assertEqual(contact.get_address('BUSINESS'), None)

    def test_cont_custom_field(self):
        contact = Contact()

        contact.set_custom_field(2, 'Really likes sweaters')
        contact.set_custom_field(3, 'Bill was here')
        contact.set_custom_field(14, 'Has a pig named Waddles')

        self.assertEqual(contact.get_custom_field(0), None)
        self.assertEqual(contact.get_custom_field(1), None)
        self.assertEqual(contact.get_custom_field(2)['value'], 'Really likes sweaters')
        self.assertEqual(contact.get_custom_field(14)['value'], 'Has a pig named Waddles')


        contact.remove_custom_field(3)

        self.assertEqual(contact.get_custom_field('2')['value'], 'Really likes sweaters')
        self.assertEqual(contact.get_custom_field(3), None)

        contact.clear_custom_fields()

        self.assertEqual(contact.get_custom_field(2), None)

    def test_cont_lists(self):
        contact = Contact()

        lists = [{'id': '123'}, {'id': '456'}, {'id': '789'}]
        contact_list = Contact_List({'id': '321'})

        contact.set_lists(lists)

        self.assertEqual(len(contact.get_lists()), 3)
        self.assertEqual(contact.get_list(2).get_id(), '789')

        contact.add_list(contact_list)
        contact.add_list_id('654')
        contact.remove_list_id('123')
        contact.remove_list(1)

        self.assertEqual(contact.get_list(0).get_id(), '456')
        self.assertEqual(contact.get_list(2).get_id(), '654')
        self.assertEqual(len(contact.get_lists()), 3)

        contact.remove_all_lists()

        self.assertEqual(contact.get_lists(), None)

    def test_cont_notes(self):
        contact = Contact()

        self.assertEqual(contact.get_notes(), None)

        contact.set_note('Weakness: leafblowers')

        self.assertEqual(contact.get_notes()[0]['note'], 'Weakness: leafblowers')

        contact.clear_notes()

        self.assertEqual(contact.get_notes(), None)


if __name__ == '__main__':
    unittest.main()
