from nose.tools import make_decorator

from nose_blame.owner import Owner

def suite_owners(arr):
    def decorate(cls):
        cls.suite_owners = [Owner(*owner_args) for owner_args in arr]
        return cls
    return decorate

def suite_owner(name, email):
    return suite_owners([(name, email)])

def case_owners(arr):
    def decorate(fn):
        def wrapper(self, *args, **kwargs):
            self.case_owners = [Owner(*owner_args) for owner_args in arr]
            fn(self, *args, **kwargs)
        return make_decorator(fn)(wrapper)
    return decorate

def case_owner(name, email):
    return case_owners([(name, email)])
