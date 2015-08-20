from .domain_lambda import *

# Multipart File component
class Multipart_File(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'data',
            'description',
            'file_name',
            'file_type',
            'folder_id',
            'source'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
            