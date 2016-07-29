import json
from copy import copy

from nose_blame.owner import Owner

REASON_FAILURE = 'FAILURE'
REASON_ERROR = 'ERROR'

class Blame(object):

    def __init__(self, reason, case, error, case_owners=[], suite_owners=[]):
        self.case = case
        self.error = {'reason': reason, 'type': error[0].__name__, 'message': str(error[1])}
        self.case_owners = case_owners
        self.suite_owners = suite_owners

    def json_friendly(self):
        res = copy(self.__dict__)
        res['case_owners'] = [x.json_friendly() for x in res['case_owners']]
        res['suite_owners'] = [x.json_friendly() for x in res['suite_owners']]
        return res


class BlameList(object):

    def __init__(self):
        self.data = []

    def add_failure(self, *args, **kwargs):
        self.data.append(Blame(REASON_FAILURE, *args, **kwargs))

    def add_error(self, *args, **kwargs):
        self.data.append(Blame(REASON_ERROR, *args, **kwargs))

    def write_json(self, *args, **kwargs):
        return json.dumps([x.json_friendly() for x in self.data], *args, **kwargs)
