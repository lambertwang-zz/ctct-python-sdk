from .domain_lambda import *

# Event Registrant component
class Registrant(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        # All attributes are read-only
        # Array and object attriutes for the Registrant component 
        # will not have a specialized component for them
        attributes = [
            'attendance_status',
            'email',
            'fees',
            'guest_info',
            'guest_secton',
            'guests',
            'first_name',
            'guest_count',
            'id',
            'items',
            'last_name',
            'order',
            'payment_status',
            'payment_summary',
            'promo_code_info',
            'registration_date',
            'registration_status',
            'sections',
            'ticket_id',
            'updated_date'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')

