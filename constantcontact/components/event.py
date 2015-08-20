from .domain_lambda import *

from .contact import Contact
from .account_info import Account_Info

class Event(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'active_date',
            'are_registrants_public',
            'cancelled_date',
            'created_date',
            'currency_type',
            'deleted_date',
            'description',
            'end_date',
            'google_analytics_key',
            'google_merchant_id',
            'id',
            'is_calendar_displayed',
            'is_checkin_available',
            'is_home_page_displayed',
            'is_listed_in_external_directory',
            'is_map_displayed',
            'is_virtual_event',
            'location',
            'meta_data_tags',
            'name',
            'payable_to',
            'paypal_account_email',
            'registration_url',
            'start_date',
            'status',
            'theme_name',
            'time_zone_id',
            'title',
            'total_registered_count',
            'type',
            'twitter_hash_tag',
            'updated_date'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')

    def get_contact(self):
        try:
            return self['contact']
        except:
            return None

    def set_contact(self, contact):
        if type(contact) is dict:
            self['contact'] = contact
        # Prune all other fields for a event contact
        elif type(contact) is Contact:
            event_contact = {}
            try:
                event_contact['email_address'] = contact.get_email_address().get_email_address()
            except:
                pass
            # Automatically generate name
            name = ''
            name = name +(contact.get_prefix_name() if contact.get_prefix_name() else '')
            name = name +((' '+ contact.get_first_name()) if contact.get_first_name() else '')
            name = name +((' '+ contact.get_last_name()) if contact.get_last_name() else '')
            event_contact['name'] = name
            event_contact['organization_name'] = contact.get_company_name()
            event_contact['phone_number'] = contact.get_work_phone()
            self['contact'] = event_contact
        elif type(contact) is Account_Info:
            event_contact = {}
            event_contact['email_address'] = contact.get_email()
            # Automatically generate name
            name = ''
            name = name +(contact.get_first_name() if contact.get_first_name() else '')
            name = name +((' '+ contact.get_last_name()) if contact.get_last_name() else '')
            event_contact['name'] = name
            event_contact['organization_name'] = contact.get_organization_name()
            event_contact['phone_number'] = contact.get_phone()
            self['contact'] = event_contact

    def delete_contact(self):
        try:
            self.pop('contact', None)
        except:
            pass
