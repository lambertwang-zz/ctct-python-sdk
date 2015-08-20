from .domain_lambda import *

# Activity_Report is a simple component with no additional logic
class Activity_Report(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'activity_type',
            'bounce_code',
            'bounce_date',
            'bounce_description',
            'bounce_message',
            'bounces',
            'campaign_id',
            'click_date',
            'clicks',
            'contact_id',
            'email_address',
            'forward_date',
            'forwards',
            'link_id',
            'link_uri',
            'open_date',
            'opens',
            'send_date',
            'unsubscribe_date',
            'unsubscribe_reason',
            'unsubscribe_source'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
            