from .domain_lambda import *

from .address import Address
from .contact_list import Contact_List
from .email_address import Email_Address

# Contact contains additional logic for fields that contain lists, such as email_addresses, custom_fields, notes, and lists
class Contact(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'custom_fields',
            'prefix_name',
            'first_name',
            'middle_name',
            'last_name',
            'job_title',
            'company_name',
            'home_phone',
            'work_phone',
            'cell_phone',
            'fax',
            'confirmed',
            'created_date',
            'modified_date',
            'source',
            'source_details',
            'id',
            'status'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')

    # The api ignores additional email addresses after the first one
    # This SDK reflects that
    # email_addresses has no remove or clear method as one email_address must always be present
    def get_email_address(self):
        try:
            self['email_addresses'][0]
        except:
            return None
        if type(self['email_addresses'][0]) is dict:
            self['email_addresses'][0] = Email_Address(self['email_addresses'][0])
        return self['email_addresses'][0]
    # In addition to dict and Email_Addresses classes, this method will also accept a string
    # and create a new Email_Address component with the string as the email address
    def set_email_address(self, email_address):
        if type(email_address) is dict:
            email_address = Email_Address(email_address)
        if type(email_address) is Email_Address:
            self['email_addresses'] = [email_address]
        elif type(email_address) is str or unicode:
            new_email = Email_Address()
            new_email.set_email_address(email_address)
            self['email_addresses'] = [new_email]
        else:
            raise TypeError('invalid type for email_address: '+type(email_address).__name__)

    def get_addresses(self):
        try:
            self['addresses']
        except:
            return None
        for i in range(len(self['addresses'])):
            if type(self['addresses'][i]) is not Address:
                self['addresses'][i] = Address(self['addresses'][i])
        return self['addresses']
    # The API currently only supports handling 2 addresses at a time, 
    # one personal and one business address.
    def get_address(self, addr_type):
        try:
            self['addresses']
        except:
            pass
        else:
            for i in range(len(self['addresses'])):
                if type(self['addresses'][i]) is dict:
                    self['addresses'][i] = Address(self['addresses'][i])
                if self['addresses'][i].get_address_type() == addr_type:
                    return self['addresses'][i]
        return None
    def set_address(self, address):
        if type(address) is dict:
            address = Address(address)
        if type(address) is Address:
            if address.get_address_type() not in ['PERSONAL', 'BUSINESS']:
                raise AttributeError('address type must be \'PERSONAL\' or \'BUSINESS\'')
            # Remove address of same type if one already exists
            self.remove_address(address.get_address_type())
            # Initialize field if field doesn't exist
            try:
                self['addresses']
            except:
                self['addresses'] = []
            self['addresses'].append(address)
        else:
            raise TypeError('invalid type for address: '+type(address).__name__)
    def remove_address(self, addr_type = None):
        # Quit method early if there are no addresses
        try:
            self['addresses']
        except:
            return None
        if addr_type:
            for i in range(len(self['addresses'])):
                if self['addresses'][i].get_address_type() == addr_type:
                    self['addresses'].pop(i)
            # Cleanup the dictionary if no more addresses are present
            if len(self['addresses']) is 0:
                self.clear_addresses()
        # if no address type is specified, all addresses are removed
        else:
            self.clear_addresses()

    def clear_addresses(self):
        try:
            self.pop('addresses', None)
        except:
            pass

    # Custom field index does not refer to the position in the list 'custom_fields' 
    # it refers to the numbering of the 'label' of a specific custom field.
    # This is done because custom_fields supports up to 15 fields labelled from 1-15
    # and a user will generally assign a specific field to a certain label.
    def get_custom_field(self, index):
        try:
            self['custom_fields']
        except:
            pass
        else:
            if self['custom_fields']:
                for field in self['custom_fields']:
                    # TODO: Be able to regex match all valid names for custom field labels

                    if str(index) == self.__get_field_name_number(field['name']):
                        return field
        return None

    def set_custom_field(self, index, value):
        self.remove_custom_field(index)
        try:
            self['custom_fields']
        except:
            self['custom_fields'] = []
        field = {'name': 'CustomField'+str(index), 'value': value}
        self['custom_fields'].append(field)

    def remove_custom_field(self, index):
        # Quit method early if there are no custom fields
        try:
            self['custom_fields']
        except:
            return None
        for i in range(len(self['custom_fields'])):
            # TODO: Be able to regex match all valid names for custom field labels

            if str(index) == self.__get_field_name_number(self['custom_fields'][i]['name']):
                self['custom_fields'].pop(i)
                break
        # if no more custom fields are present, cleanup the dict
        if len(self['custom_fields']) == 0:
            self.clear_custom_fields()

    def clear_custom_fields(self):
        try:
            self.pop('custom_fields', None)
        except:
            pass

    def __get_field_name_number(self, name):
        # Extract the name_number from the name field
        # ie for name = '{somestring}123512', name_number = '123512'
        name_number = ''.join([str(char) for char in name if char in [str(d) for d in range(10)]])
        return name_number

    # Methods over the lists list are useful if a user wants to copy lists to another contact 
    def get_lists(self):
        try:
            self['lists']
        except:
            return None
        for i in range(len(self['lists'])):
            if type(self['lists'][i]) is not Contact_List:
                self['lists'][i] = Contact_List(self['lists'][i])
        return self['lists']
    # Does not accept a Result_Set for lists
    def set_lists(self, lists):
        if lists:
            self['lists'] = lists
    def get_list(self, index):
        if type(self['lists'][index]) is dict:
            self['lists'][index] = Contact_List(self['lists'][index])
        return self['lists'][index]
    # Accepts a string as list_id
    def add_list_id(self, list_id):
        try:
            self['lists']
        except:
            self['lists'] = []
        new_list = Contact_List({'id': list_id})
        self['lists'].append(new_list)
    # Accepts a string as list_id
    def add_list(self, contact_list):
        try:
            self['lists']
        except:
            self['lists'] = []
        if type(contact_list) is dict:
            contact_list = Contact_List(contact_list)
        if type(contact_list) is Contact_List:
            self['lists'].append(contact_list)
        else:
            raise TypeError('invalid type for contact_list: '+type(contact_list).__name__)
    def remove_list_id(self, list_id):
        try:
            self['lists']
        except:
            return None
        for i in range(len(self['lists'])):
            if type(self['lists'][i]) is dict:
                self['lists'][i] = Contact_List(self['lists'][i])
            if self['lists'][i].get_id() == list_id:
                self['lists'].pop(i)
                break
    def remove_list(self, index):
        try:
            self['lists']
        except:
            return None
        self['lists'].pop(index)
    # A clear method is added for lists to allow users to easily 
    # reset a contact's lists despite lists being a required field. 
    def remove_all_lists(self):
        try:
            self.pop('lists', None)
        except:
            pass

    # The API only allows max one note per contact
    def get_notes(self):
        try:
            return self['notes']
        except:
            return None
    # note accepts either a dict or string. A string will be formatted into a proper note.
    # There is no validation on an input dict.
    def set_note(self, note):
        try: 
            self['notes']
        except:
            self['notes'] = []
        if type(note) is str:
            self['notes'].append({'note': note})
        elif type(note) is dict:
            self['notes'].append(note)
        else:
            raise TypeError('invalid type for note: '+type(note).__name__)
    def clear_notes(self):
        try:
            self.pop('notes', None)
        except:
            pass

