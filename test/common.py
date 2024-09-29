# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for utilities
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *

import unittest, os

class Py4CBaseTestOnIFE(unittest.TestCase):
    
    def setUp(self):
        # set up path with expected result files
        self.test_expectations_path = os.environ["TEST_EXPECTATIONS_PATH"]
        # allow long string diffs to be printed
        self.maxDiff = None
        # initialise IFE sample model
        aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
        self.model = CapellaModel()
        self.model.open(aird_path)
        self.se = self.model.get_system_engineering()
        # start transaction so writes don't violate invariants
        self.model.start_transaction()

    def tearDown(self):
        # roll back transaction so writes don't violate invariants
        self.model.rollback_transaction()
