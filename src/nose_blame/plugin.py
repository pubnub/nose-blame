import logging
import os

from nose.plugins import Plugin
from nose.util import resolve_name
from nose.tools import make_decorator

from nose_blame.owner import Owner
from nose_blame.blame import BlameList

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

class BlamePlugin(Plugin):
    enabled = False
    name = 'blame'
    score = 0

    def options(self, parser, env=os.environ):
        super(BlamePlugin, self).options(parser, env=env)

        env_opt = 'NOSE_BLAME_FILE'
        parser.add_option('--blame-file', action='store', type='string',
                          dest='blame_file', default=env.get(env_opt, None),
                          help='Path that blame json file will be written to.')


    def configure(self, options, conf):
        super(BlamePlugin, self).configure(options, conf)
        self.conf = conf

        if not self.enabled or not self.can_configure: return
        self.blame_file = getattr(options, 'blame_file', None)

    def begin(self):
        self.blame_list = BlameList()

    def handleError(self, test, err):
        case_owners = getattr(test.test, 'case_owners', [])
        suite_owners = getattr(test.test, 'suite_owners', [])
        self.blame_list.add_error(test.id(), err, case_owners=case_owners, suite_owners=suite_owners)

    def handleFailure(self, test, err):
        case_owners = getattr(test.test, 'case_owners', [])
        suite_owners = getattr(test.test, 'suite_owners', [])
        self.blame_list.add_failure(test.id(), err, case_owners=case_owners, suite_owners=suite_owners)

    def finalize(self, result):
        if self.blame_file:
            fd = open(self.blame_file, 'w')
            fd.write(self.blame_list.write_json())
            fd.close()
        else:
            print(self.blame_list.write_json(indent=2, sort_keys=True))
        return None
