from .domain_lambda import *

# Billing_Plan is a simple component with no additional logic
class Billing_Plan(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        # Current tiers is returned as a dict
        attributes = [
            'billing_day_of_month',
            'current_tiers',
            'plan_level',
            'plan_type',
            'status'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')