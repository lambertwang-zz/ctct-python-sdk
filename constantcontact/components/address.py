from .domain_lambda import *

# Address is a simple component with no additional logic
class Address(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'id',
            'address_type',
            'latitude',
            'line1',
            'line2',
            'line3',
            'longitude',
            'city',
            'state_code',
            'state',
            'country_code',
            'postal_code',
            'sub_postal_code'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
            