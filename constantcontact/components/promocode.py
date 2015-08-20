from .domain_lambda import *

from .fee import Fee
from .result_set import Result_Set

# Promocode component
class Promocode(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'code_name',
            'code_type',
            'discount_amount',
            'discount_percent',
            'discount_scope',
            'discount_type',
            'id',
            'is_paused',
            'quantity_available',
            'quantity_total',
            'quantity_used'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')

    # Returns a list of strings
    def get_fee_ids(self):
        try:
            return self['fee_ids']
        except:
            return None

    # Sets the promocode fees to a list of strings or Result_Set of Fees
    def set_fee_ids(self, fee_ids):
        if type(fee_ids) is Result_Set:
            self['fee_ids'] = fee_ids.get_set()
        elif type(fee_ids) is list:
            self['fee_ids'] = fee_ids
        else:
            raise TypeError('invalid type for fee_ids: '+type(fee_ids).__name__)
        for i in range(len(self['fee_ids'])):
            if type(self['fee_ids'][i]) is Fee:
                self['fee_ids'][i] = self['fee_ids'][i].get_id()

    # Deletes a fee_id by value
    def delete_fee_by_id(self, fee_id):
        try:
            self['fee_ids']
        except:
            return None
        for i in range(len(self['fee_ids'])):
            if self['fee_ids'][i] == fee_id:
                self['fee_ids'].pop(i)
                break

    # Deletes a fee_id by index
    def delete_fee(self, index):
        try:
            self['fee_ids']
        except:
            return None
        self['fee_ids'].pop(index)

    # Clears all fees
    def clear_fee_ids(self):
        try:
            self.pop('fee_ids', None)
        except:
            pass

