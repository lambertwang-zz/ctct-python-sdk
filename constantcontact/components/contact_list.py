from .domain_lambda import *

class Contact_List(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'contact_count',
            'created_date',
            'id',
            'modified_date',
            'name',
            'status'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
        self.set_name = make_setter(self, 'name')
        self.set_status = make_setter(self, 'status')
