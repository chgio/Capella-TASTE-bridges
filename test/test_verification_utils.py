# include needed for the Capella modeller API
include("workspace://Python4Capella/simplified_api/capella.py")
if False:
    from simplified_api.capella import *

# include needed for utilities
include("workspace://Python4Capella/utilities/CapellaPlatform.py")
if False:
    from utilities.CapellaPlatform import *

include("workspace://Capella-TASTE-bridges/test/common.py")
if False:
    from test.common import *

include("workspace://Capella-TASTE-bridges/verification/utils.py")
if False:
    from verification.utils import *

import os


class TestFSMAsAsString(Py4CBaseTestOnIFE):
    
    def test_fsm_states_as_string_simple(self):
        exp_path = os.path.join(self.test_expectations_path, "fsm_states_as_string_simple.txt")
        with open(exp_path) as exp_file:
            fsm_states_as_string_verbose_expected = exp_file.read()
        sa = self.se.get_system_analysis()
        sa_fsm = sa.get_all_contents_by_type(StateMachine)[0]
        fsm_states_as_string_verbose_actual = sa_fsm.states_as_string(verbose=False).strip()
        self.assertEqual(
            fsm_states_as_string_verbose_actual,
            fsm_states_as_string_verbose_expected,
            f"Simple string representation of States in StateMachine {sa_fsm.get_name()} does not match expectation."
        )

    def test_fsm_states_as_string_verbose(self):
        exp_path = os.path.join(self.test_expectations_path, "fsm_states_as_string_verbose.txt")
        with open(exp_path) as exp_file:
            fsm_states_as_string_verbose_expected = exp_file.read()
        sa = self.se.get_system_analysis()
        sa_fsm = sa.get_all_contents_by_type(StateMachine)[0]
        fsm_states_as_string_verbose_actual = sa_fsm.states_as_string(verbose=True).strip()
        self.assertEqual(
            fsm_states_as_string_verbose_actual,
            fsm_states_as_string_verbose_expected,
            f"Verbose string representation of States in StateMachine {sa_fsm.get_name()} does not match expectation."
        )

    def test_fsm_transitions_as_string_simple(self):
        exp_path = os.path.join(self.test_expectations_path, "fsm_transitions_as_string_simple.txt")
        with open(exp_path) as exp_file:
            fsm_transitions_as_string_verbose_expected = exp_file.read()
        sa = self.se.get_system_analysis()
        sa_fsm = sa.get_all_contents_by_type(StateMachine)[0]
        fsm_transitions_as_string_verbose_actual = sa_fsm.transitions_as_string(verbose=False).strip()
        self.assertEqual(
            fsm_transitions_as_string_verbose_actual,
            fsm_transitions_as_string_verbose_expected,
            f"Simple string representation of Transitions in StateMachine {sa_fsm.get_name()} does not match expectation."
        )

    def test_fsm_transitions_as_string_verbose(self):
        exp_path = os.path.join(self.test_expectations_path, "fsm_transitions_as_string_verbose.txt")
        with open(exp_path) as exp_file:
            fsm_transitions_as_string_verbose_expected = exp_file.read()
        sa = self.se.get_system_analysis()
        sa_fsm = sa.get_all_contents_by_type(StateMachine)[0]
        fsm_transitions_as_string_verbose_actual = sa_fsm.transitions_as_string(verbose=True).strip()
        self.assertEqual(
            fsm_transitions_as_string_verbose_actual,
            fsm_transitions_as_string_verbose_expected,
            f"Verbose string representation of Transitions in StateMachine {sa_fsm.get_name()} does not match expectation."
        )


if __name__ == "__main__":
    unittest.main()
