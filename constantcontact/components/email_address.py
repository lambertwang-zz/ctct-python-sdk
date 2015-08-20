from .domain_lambda import *

class Email_Address(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'id',
            'status',
            'confirm_status',
            'opt_in_source',
            'opt_out_source',
            'opt_in_date',
            'opt_out_date',
            'email_address',
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
