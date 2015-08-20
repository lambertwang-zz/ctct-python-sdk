from .baseservice import BaseService

from .components import Activity_Report, Contact, Contact_List, Email_Address, Result_Set, Tracking_Summary

import sys
if sys.version_info[0] == 2:
    from string import join

class ContactService(BaseService):
    # Contacts services endpoints    
    def get_contacts(self, email = None, limit = 50, modified_since = None, status = 'ALL'):
        queries = {}
        if email is not None:
            if type(email) is Email_Address:
                email = email.get_email_address()
            queries['email'] = email
        
        queries['limit'] = limit
        queries['status'] = status

        if modified_since is not None:
            queries['modified_since'] = modified_since
        
        response = self.request('get', 'contacts', params = queries)
        try:
            response['results']
        except:
            return response
        # Convert dict to Components
        for i in range(len(response['results'])):
            response['results'][i] = Contact(response['results'][i])
        return Result_Set(response)

    def post_contacts(self, contact, action_by = 'ACTION_BY_OWNER'):
        contact = self.validate_contact(contact)
        return Contact(self.request('post', 'contacts', params = {'action_by': action_by}, body = contact))

    def get_contact(self, contact_id):
        contact_id = self.contact_to_id(contact_id)
        return Contact(self.request('get', 'contacts/'+contact_id))

    def update_contact(self, contact, action_by = 'ACTION_BY_OWNER'):
        contact = self.validate_contact(contact)
        if not contact.get_id():
            raise AttributeError('missing Contact.id')
        return Contact(self.request('put', 'contacts/'+contact.get_id(), params = {'action_by': action_by}, body = contact))

    def delete_contact(self, contact_id):
        contact_id = self.contact_to_id(contact_id)
        return self.request('delete', 'contacts/'+contact_id) 

    # Contacts tracking endpoints
    def get_contact_tracking(self, contact_id, created_since = None, limit = 500):
        queries = self.tracking_queries(created_since, limit)
        contact_id = self.contact_to_id(contact_id)

        response = self.request('get', 'contacts/'+contact_id+'/tracking', params = queries)

        return self.tracking_result_set(response)

    def get_contact_tracking_summary(self, contact_id):
        contact_id = self.contact_to_id(contact_id)

        return Tracking_Summary(self.request('get', 'contacts/'+contact_id+'/tracking/reports/summary'))

    def get_contact_bounces(self, contact_id, created_since = None, limit = 500):
        queries = self.tracking_queries(created_since, limit)
        contact_id = self.contact_to_id(contact_id)

        response = self.request('get', 'contacts/'+contact_id+'/tracking/bounces', params = queries)

        return self.tracking_result_set(response)

    def get_contact_clicks(self, contact_id, created_since = None, limit = 500):
        queries = self.tracking_queries(created_since, limit)
        contact_id = self.contact_to_id(contact_id)

        response = self.request('get', 'contacts/'+contact_id+'/tracking/clicks', params = queries)

        return self.tracking_result_set(response)

    def get_contact_forwards(self, contact_id, created_since = None, limit = 500):
        queries = self.tracking_queries(created_since, limit)
        contact_id = self.contact_to_id(contact_id)

        response = self.request('get', 'contacts/'+contact_id+'/tracking/forwards', params = queries)

        return self.tracking_result_set(response)

    def get_contact_opens(self, contact_id, created_since = None, limit = 500):
        queries = self.tracking_queries(created_since, limit)
        contact_id = self.contact_to_id(contact_id)

        response = self.request('get', 'contacts/'+contact_id+'/tracking/opens', params = queries)

        return self.tracking_result_set(response)


    def get_contact_sends(self, contact_id, created_since = None, limit = 500):
        queries = self.tracking_queries(created_since, limit)
        contact_id = self.contact_to_id(contact_id)

        response = self.request('get', 'contacts/'+contact_id+'/tracking/sends', params = queries)

        return self.tracking_result_set(response)

    def get_contact_unsubscribes(self, contact_id, created_since = None, limit = 500):
        queries = self.tracking_queries(created_since, limit)
        contact_id = self.contact_to_id(contact_id)

        response = self.request('get', 'contacts/'+contact_id+'/tracking/unsubscribes', params = queries)

        return self.tracking_result_set(response)

    def get_contact_report_by_campaign(self, contact_id):
        contact_id = self.contact_to_id(contact_id)

        response = {'results': self.request('get', 'contacts/'+contact_id+'/tracking/reports/summaryByCampaign')}
        return self.tracking_result_set(response)

    def validate_contact(self, contact):
        if type(contact) is dict:
            contact = Contact(contact)
        if type(contact) is not Contact:
            raise TypeError('invalid type for contact: '+type(contact).__name__)

        return contact

    def contact_to_id(self, contact_id):
        if type(contact_id) is Contact:
            contact_id = contact_id.get_id()
        return contact_id

    def tracking_queries(self, created_since, limit):
        queries = {}

        if created_since is not None:
            queries['created_since'] = created_since
        
        queries['limit'] = limit

        return queries

    def tracking_result_set(self, tracking_response):
        try:
            tracking_response['results']
        except:
            return tracking_response
        for i in range(len(tracking_response['results'])):
            tracking_response['results'][i] = Activity_Report(tracking_response['results'][i])
        return Result_Set(tracking_response)
