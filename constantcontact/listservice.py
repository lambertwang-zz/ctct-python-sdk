from .baseservice import BaseService

from .components import Contact, Contact_List, Result_Set

class ListService(BaseService):
    # Contact List services endpoints
    # returns a list rather than a Result_Set
    def get_lists(self, modified_since = None):
        queries = {}
        if modified_since:
            queries['modified_since'] = modified_since

        response = self.request('get', 'lists', params = queries)
        # Convert dict to components
        if type(response) is list:
            for i in range(len(response)):
                response[i] = Contact_List(response[i])
        return response

    def post_lists(self, contact_list, status = 'ACTIVE'):
        if type(contact_list) is str:
            contact_list = Contact_List({'name': contact_list, 'status': status})
        contact_list = self.validate_contact_list(contact_list)
        return Contact_List(self.request('post', 'lists', body = contact_list))

    # Methods which accept a list_id will also accept a list component
    def get_list(self, list_id):
        list_id = self.list_to_id(list_id)
        return Contact_List(self.request('get', 'lists/'+list_id))

    def update_list(self, contact_list):
        contact_list = self.validate_contact_list(contact_list)
        return Contact_List(self.request('put', 'lists/'+contact_list.get_id(), body = contact_list))

    def delete_list(self, list_id):
        list_id = self.list_to_id(list_id)
        return self.request('delete', 'list/'+list_id)

    # TODO: This method does not currently return a Result_Set of Contact components
    def get_list_contacts(self, list_id, limit = 50, modified_since = None):
        queries = {}
        queries['limit'] = limit
        if modified_since is not None:
            queries['modified_since'] = modified_since

        list_id = self.list_to_id(list_id)
        response = self.request('get', 'list/'+list_id+'/contacts', params = queries)

        try:
            response['results']
        except:
            return response
        for i in range(len(response['results'])):
            response['results'][i] = Contact(response['results'][i])
        return Result_Set(response)

    def validate_contact_list(self, contact_list):
        if type(contact_list) is dict:
            contact_list = Contact_List(contact_list)
        if type(contact_list) is not Contact_List:
            TypeError('invalid type for contact_list: '+type(contact_list).__name__)
            
        return contact_list

    def list_to_id(self, contact_list):
        if type(contact_list) is Contact_List:
            contact_list = contact_list.get_id()
        return contact_list
