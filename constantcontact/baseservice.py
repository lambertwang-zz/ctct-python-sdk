import requests
import json

from .components import Activity_Report, Campaign, Contact, Result_Set

__version__ = '0.3.2'

class BaseService():
    def __init__(self, client_id, token, base_url = 'https://api.constantcontact.com/v2'):
        self.client_id = client_id
        self.token = token
        # Add required headers.
        # TODO: Add header for SDK usage tracking
        self.header = {}
        self.header['Authorization'] = 'Bearer '+self.token
        self.header['x-ctct-request-source'] = 'sdk.lwang_python.'+__version__
        self.base_url = base_url

    # Token info only works on production environments. 
    def token_info(self):
        token_info = requests.post('https://oauth2.constantcontact.com/oauth2/tokeninfo.htm'+'?access_token='+self.token)
        token_json = json.loads(token_info.content)
        return token_json

    def request(self, request_type, endpoint, params = {}, body = [], header = {}, form_data = None, form_file = None):
        # Formulate a request URI string for a request
        request_string = self.base_url+'/'+endpoint
        
        params['api_key'] = self.client_id

        response = None

        # set required headers.
        header.update(self.header)

        if request_type == 'get':
            response = requests.get(request_string, headers=header, json=body, params = params)
        elif request_type == 'put':
            response = requests.put(request_string, headers=header, json=body, params = params)
        elif request_type == 'post':
            # For multipart/form-data posts (Mylibrary multipart post)
            if form_data and form_file:
                response = requests.post(request_string, headers=header, params = params, files = form_file, data = form_data)
            else:
                response = requests.post(request_string, headers=header, json=body, params = params)
        elif request_type == 'delete':
            response = requests.delete(request_string, headers=header, json=body, params = params)
        elif request_type == 'patch':
            response = requests.patch(request_string, headers=header, json=body, params = params)


        try:
            response = response if response is None else json.loads(response.content.decode('utf8'))
        except:
            pass
        '''
        except AttributeError:
            return response
        except ValueError:
            return response
        except TypeError:
        '''

        # Check if an error message key pair is returned
        try:
            if response[0]['error_message']:
                response = response[0]
        except:
            pass

        return response

    # The url from the pagination data can be directly passed into this method
    # Pagination is returned from the api in the form /v2/{service}?next={uuid}
    def next_page(self, url):
        service = url.split('/', 2)[2].split('?', 1)[0]
        url = self.base_url + '/' + url.split('/', 2)[2]
        
        # Set the api key for pagination request
        params = {'api_key': self.client_id}

        response = requests.get(url, headers=self.header, params = params)

        try:
            response = response if response is None else json.loads(response.content.decode('utf8'))
        except:
            pass
        # Check if an error message key pair is returned
        try:
            if response[0]['error_message']:
                response = response[0]
        except:
            # Parse response into a resultset
            if service == 'contacts':
                for i in range(len(response['results'])):
                    response['results'][i] = Contact(response['results'][i])
            elif service == 'emailmarketing/campaigns':
                for i in range(len(response['results'])):
                    response['results'][i] = Campaign(response['results'][i])
            elif service.split('/', 1)[0] == 'lists':
                for i in range(len(response['results'])):
                    response['results'][i] = Contact(response['results'][i])
            elif service.split('/')[2] == 'tracking':
                # Contact tracking
                for i in range(len(response['results'])):
                    response['results'][i] = Activity_Report(tracking_response['results'][i])
            elif service.split('/')[3] == 'tracking':
                # Email campaign tracking
                for i in range(len(response['results'])):
                    response['results'][i] = Activity_Report(tracking_response['results'][i])

        return Result_Set(response)
    
    # Prepares a multipart object into form_file and form_data into 
    # multipart/form-data content for a multipart post endpoint.
    # Returns a tuple containing the file and data fields.
    def prepare_multipart_body(self, multipart_object, attributes):
        form_file = {}
        form_data = {}

        for key, value in multipart_object.items():
            if key not in attributes:
                raise AttributeError('Invalid attribute for '+type(multipart_object).__name__+': '+key)
            if key == 'data':
                form_file[key] = value
            else:
                form_data[key] = (None, value)
        for key in attributes:
            try:
                multipart_object[key]
            except:
                raise AttributeError('Missing attribute for '+type(multipart_object).__name__+': '+key)

        return (form_file, form_data)

