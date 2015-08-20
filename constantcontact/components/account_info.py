from .domain_lambda import *
from .address import Address

# Account_Info is a mostly simple component
class Account_Info(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'company_logo',
            'country_code',
            'email',
            'first_name',
            'last_name',
            'organization_name',
            'phone',
            'state_code',
            'time_zone',
            'website'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')

    # API currently only supports 1 organization address
    def get_organization_address(self):
        try: 
            self['organization_addresses'][0]
        except:
            return None
        if type(self['organization_addresses'][0]) is not Address:
            self['organization_addresses'][0] = Address(self['organization_addresses'][0])
        return self['organization_addresses'][0]
    # addresses for organization are different from addresses for contacts;
    # however, the model is the same so it is up to the user to adjust fields accordingly
    def set_organization_address(self, address):
        if type(address) is dict:
            address = Address(address)
        if type(address) is not Address:
            raise TypeError('invalid type for address: '+type(address).__name__)
        self['organization_addresses'] = [address]
    def clear_organization_address(self):
        try:
            self.pop('organization_addresses', None)
        except:
            pass
