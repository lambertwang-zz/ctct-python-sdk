from .domain_lambda import *

# Mylibrary File component
class Mylibrary_File(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        # Thumbnail is returned as a dict with
        # 3 properties: width, url, height
        attributes = [
            'created_date',
            'description',
            'file_type',
            'folder',
            'folder_id',
            'height',
            'id',
            'is_image',
            'modified_date',
            'name',
            'size',
            'source',
            'status',
            'thumbnail',
            'url',
            'width'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
            