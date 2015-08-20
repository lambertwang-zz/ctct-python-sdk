from .domain_lambda import *

# Mylibrary Folder component
class Mylibrary_Folder(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        # Children is stored as an array of strings
        attributes = [
            'children',
            'created_date',
            'id',
            'item_count',
            'level',
            'modified_date',
            'name',
            'parent_id'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
            