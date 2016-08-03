# Nose Blame Plugin

Nose plugin to allow for assigning owners to entire test suites and/or individual test cases.

Outputs json blame report to stdout or specified file.

## Installation

```
pip install nose-blame
```

- Pip doesn't play nice with artifactory and basic auth so for the time being do this instead:
```
pip install git+git://github.com/pubnub/nose-blame.git#egg=nose-blame
```
- We can throw this on PyPI when/if it beccomes necessary

## Usage

```
--with-blame                      | enable blame plugin
--blame-file <path/to/file.json>  | path to json file for blame report, prints to stdout if not set
```
`NOSE_WITH_BLAME` and `NOSE_BLAME_FILE` environment variables may be used in lieu of cli flags

In nose test:
```python
from nose_blame.decorators import *

// Single suite owner
@suite_owner('Owner Name', 'owner@email.com')

// Multiple suite owners
@suite_owners([('Owner Name 1', 'owner1@email.com'), ('Owner Name 2', 'owner2@email.com')])

class MyTestSuite(unittest.TestCase):
  ...

  // Single case owner
  @case_owner('Owner Name', 'owner@email.com')

  // Multiple case owners
  @case_owners([('Owner Name 1', 'owner1@email.com'), ('Owner Name 2', 'owner2@email.com')])

  def test_my_test_case(self):
    ...

```

## Blocks Specific

Wrapper around nose_blame.decorators is located [here](https://github.com/pubnub/blocks/blob/master/itest/blocks_utils/owners.py) in order to avoid repeatedly writing out Name/Email.

Use this module instead like so:

```python
from blocks_utils.owners import *

@case_owner('key')
```

and add yourself to the ```_owner_list``` dict in owners.py
