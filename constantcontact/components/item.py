from .domain_lambda import *

from .attribute import Attribute
from .result_set import Result_Set

# Item component
class Item(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'default_quantity_available',
            'default_quantity_total',
            'description',
            'id',
            'name',
            'per_registrant_limit',
            'price',
            'show_quantity_available'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')

    def get_attributes(self):
        try:
            self['attributes']
        except:
            return None
        for i in range(len(self['attributes'])):
            self['attributes'][i] = Attribute(self['attributes'][i])
        return self['attributes']

    def set_attributes(self, attributes):
        if type(attributes) is Result_Set:
            self['attributes'] = attributes.get_set()
        elif type(attributes) is list:
            self['attributes'] = attributes
        else:
            raise TypeError('invalid type for attributes: '+type(attributes).__name__)

    # Deletes an attribute by id
    def delete_attribute_by_id(self, attribute_id):
        try:
            self['attributes']
        except:
            return None
        for i in range(len(self['attributes'])):
            try:
                if self['attributes'][i]['id'] == attribute_id:
                    self['attributes'].pop(i)
                    break
            except:
                pass

    # Deletes an attribute_id by index
    def delete_attribute(self, index):
        try:
            self['attributes']
        except:
            return None
        self['attributes'].pop(index)

    # Clears all attributes
    def clear_attributes(self):
        try:
            self.pop('attributes', None)
        except:
            pass

