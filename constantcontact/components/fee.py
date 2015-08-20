from .domain_lambda import *

# Fee is a simple component with no additional logic
class Fee(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'early_fee',
            'fee',
            'fee_scope',
            'has_restricted_access',
            'id',
            'label',
            'late_fee'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')