from .domain_lambda import *

from .contact_list import Contact_List
from .tracking_summary import Tracking_Summary

class Campaign(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'created_date',
            'email_content',
            'email_content_format',
            'from_email',
            'from_name',
            'greeting_name',
            'greeting_salutations',
            'greeting_string',
            'id',
            'is_permission_reminder_enabled',
            'is_view_as_webpage_enabled',
            'last_run_date',
            'message_footer',
            'modified_date',
            'name',
            'next_run_date',
            'permalink_url',
            'permission_reminder_text',
            'reply_to_email',
            'status',
            'style_sheet',
            'subject',
            'template_type',
            'text_content',
            'view_as_web_page_link_text',
            'view_as_web_page_text'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
    
    def get_click_through_details(self):
        try:
            return self['click_through_details']
        except:
            return None
    def get_click_through_detail(self, index):
        return self['click_through_details'][index]
    def clear_click_through_details(self):
        try:
            self.pop('click_through_details', None)
        except:
            pass
    
    # sent_to_contact_lists will not use the contact_list component, it 
    # will be a simple array of strings. The component will be passable 
    # to these methods, but only the list_id will be extracted and used.
    def get_sent_to_contact_lists(self):
        try:
            return self['sent_to_contact_lists']
        except:
            return None
    def add_sent_to_contact_lists(self, list_id):
        if type(list_id) is Contact_List:
            list_id = list_id.get_id()
        try:
            self['sent_to_contact_lists']
        except:
            self['sent_to_contact_lists'] = []
        self['sent_to_contact_lists'].append({'id': list_id})
    def remove_sent_to_contact_lists_id(self, list_id):
        try:
            self['sent_to_contact_lists']
        except:
            return None
        if type(list_id) is Contact_List:
            list_id = list_id.get_id()
        for i in range(len(self['sent_to_contact_lists'])):
            if self['sent_to_contact_lists'][i]['id'] == list_id:
                self['sent_to_contact_lists'].pop(i)
                break
        if len(self['sent_to_contact_lists']) == 0:
            self.clear_sent_to_contact_lists()
    def remove_sent_to_contact_lists(self, index):
        try:
            self['sent_to_contact_lists']
        except:
            return None
        self['sent_to_contact_lists'].pop(index)
        if len(self['sent_to_contact_lists']) == 0:
            self.clear_sent_to_contact_lists()
    def clear_sent_to_contact_lists(self):
        try:
            self.pop('sent_to_contact_lists', None)
        except:
            pass

    def get_tracking_summary(self):
        try:
            self['tracking_summary']
        except:
            return None
        if type(self['tracking_summary']) is dict:
            self['tracking_summary'] = Tracking_Summary(self['tracking_summary'])
        return self['tracking_summary']
    def delete_tracking_summary(self):
        try:
            self.pop('tracking_summary', None)
        except:
            pass

