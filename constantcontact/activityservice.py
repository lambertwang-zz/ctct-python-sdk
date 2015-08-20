from .baseservice import BaseService

from .components import Activity_Status, Contact, Email_Address, Multipart_Activity

class ActivityService(BaseService):
    # Activity services endpoints
    def import_contacts(self, import_data, lists, columns):
        if 'EMAIL' in columns:
            for contact in import_data:
                if type(contact) is Contact:
                    for i in range(len(contact['email_addresses'])):
                        if type(contact['email_addresses'][i]) is dict or type(contact['email_addresses'][i]) is Email_Address:
                            contact['email_addresses'][i] = contact['email_addresses'][i]['email_address']
                    
        body = {'import_data': import_data, 'lists': lists, 'column_names': columns}
        return Activity_Status(self.request('post', 'activities/addcontacts', body = body))

    def remove_contacts(self, import_data, lists):
        for contact in import_data:
            if type(contact) is Contact:
                for i in range(len(contact['email_addresses'])):
                    if type(contact['email_addresses'][i]) is dict or type(contact['email_addresses'][i]) is Email_Address:
                        contact['email_addresses'][i] = contact['email_addresses'][i]['email_address']

        body = {'import_data': import_data, 'lists': lists}
        return Activity_Status(self.request('post', 'activities/removefromlists', body = body))

    def clear_contact_lists(self, lists):
        return Activity_Status(self.request('post', 'activities/clearlists', body = {'lists': lists}))

    def export_contacts(self, columns, lists, sort_by = 'EMAIL_ADDRESS', file_type = 'CSV', export_added_by = False, export_date_added = False):
        # The body is constructed from individual components passed in by the developer
        body = {'lists': lists, 'column_names': columns, 'file_type': file_type, 'sort_by': sort_by, 'export_added_by': export_added_by, 'export_date_added': export_date_added}
        return Activity_Status(self.request('post', 'activities/exportcontacts', body = body))

    # Retrieves the .csv data
    def get_export_file(self, file_name):
        file_name = file_name.split('v2/')[1].split('?')[0]
        return self.request('get', file_name)

    def multipart_import_contacts(self, multipart_activity):
        attributes = [
            'data',
            'file_name',
            'lists'
        ]
        form_file, form_data = self.prepare_multipart_body(multipart_activity, attributes)

        return self.request('post', 'activities/addcontacts', form_file = form_file, form_data = form_data)

    def multipart_remove_contacts(self, multipart_activity):
        attributes = [
            'data',
            'file_name',
            'lists'
        ]
        form_file, form_data = self.prepare_multipart_body(multipart_activity, attributes)

        return self.request('post', 'activities/removefromlists', form_file = form_file, form_data = form_data)

    def activities_status_report(self, type_query = None, status = 'ALL'):
        params = {'status': status}
        if type_query:
            params['type'] = type_query
        
        response = self.request('get', 'activities', params = params)
        
        if type(response) is list:
            for i in range(len(response)):
                response[i] = Activity_Status(response[i])
        return response

    def individual_activity_status(self, activity_id):
        activity_id = self.activity_to_id(activity_id)
        return Activity_Status(self.request('get', 'activities/'+activity_id))

    def activity_to_id(self, activity_id):
        if type(activity_id) is Activity_Status:
            activity_id = activity_id.get_id()
        return activity_id
