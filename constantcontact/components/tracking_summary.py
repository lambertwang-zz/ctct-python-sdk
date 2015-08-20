from .domain_lambda import *

# Tracking_Summary is a simple component with no additional logic
class Tracking_Summary(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        attributes = [
            'bounces',
            'clicks',
            'forwards',
            'opens',
            'sends',
            'spam_count',
            'unsubscribes'
        ]
        
        for name in attributes:
            exec('self.get_'+name+' = make_getter(self, \''+name+'\')')
            exec('self.set_'+name+' = make_setter(self, \''+name+'\')')
            exec('self.delete_'+name+' = make_deleter(self, \''+name+'\')')
            