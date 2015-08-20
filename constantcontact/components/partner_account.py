from .domain_lambda import *

# Partner_Account is a simple component with no additional logic
class Partner_Account(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'billing_locale',
            'country_code',
            'email',
            'first_name',
            'id',
            'idp_provider',
            'idp_provider_id',
            'last_name',
            'oauth2_token',
            'last_login_date',
            'organization_name',
            'password',
            'phone',
            'state_code',
            'status',
            'username'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')