class Result_Set(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        try:
            self.set_type = type(self['results'][0])
        except:
            self.set_type = None
    def get_set(self):
        return self['results']
    def get_item(self, index):
        return self['results'][index]
    def get_set_type(self):
        return self.set_type
    def add_item(self, item):
        if self.set_type:
            if type(item) is not self.set_type:
                raise TypeError('Item type ('+type(item).__name__+') does not match set_type ('+set_type.__name__+')')
            else:
                self['results'].append(item)
        else:
            self['results'] = [item]
            self.set_type = type(item)
    def remove_item(self, index):
        self['results'].pop(index)
        if not self['results']:
            self.set_type = None
    def clear_result_set(self):
        self.pop('results', None)
        self['results'] = []
        self.set_type = None
    def get_next_page(self):
        try:
            return self['meta']['pagination']['next_link']
        except:
            return None
