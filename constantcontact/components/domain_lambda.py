# Lambda functions used to dynamically generate getter and setter methods
# These methods are applicable to dictionaries

# self refers to the object implementing these methods
# name refers to the field being modified
def make_getter(self, name):
    return lambda: get_attr(self, name)
def get_attr(self, name):
    try:
        return self[name]
    except:
        return None

def make_setter(self, name):
    # v refers to the value the field is being set to
    return lambda v: set_attr(self, name, v)
def set_attr(self, name, value):
    self[name] = value

def make_deleter(self, name):
    return lambda: delete_attr(self, name)
def delete_attr(self, name):
    try:
        self.pop(name, None)
    except:
        pass
