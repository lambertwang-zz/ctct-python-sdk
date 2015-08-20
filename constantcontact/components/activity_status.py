from .domain_lambda import *

# Activity_Status is a simple component with no additional logic
# Its fields are all readonly
class Activity_Status(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'contact_count',
            'created_date',
            'error_count',
            'errors',
            'file_name',
            'finish_date',
            'id',
            'start_date',
            'status',
            'type',
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            