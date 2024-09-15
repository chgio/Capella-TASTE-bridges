# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for utilities
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *


def print_states(fsm, leading_tabs=0, verbose=False):
    fsm_states = fsm.get_all_contents_by_type(State)
    print(leading_tabs * '\t' + ('states (verbose):' if verbose else 'states:'))
    for state in fsm_states:
        print((leading_tabs+1) * '\t' + state.get_name())
        if verbose:
            state_outgoing_transitions = state.get_outgoing()
            for transition in state_outgoing_transitions:
                transition_name = transition.get_name() if transition.get_name() is not None else '*unnamed transition*'
                print((leading_tabs+2) * '\t' + transition_name)
                transition_triggers = transition.get_triggers()
                for trigger in transition_triggers:
                    print((leading_tabs+3) * '\t' + ' -- ' + trigger.get_name() + ' -> ' + transition.get_target().get_name())
                if len(transition_triggers) == 0:
                    print((leading_tabs+3) * '\t' + ' ---> ' + transition.get_target().get_name())


def print_transitions(fsm, leading_tabs=0, verbose=False):
    fsm_transitions = fsm.get_all_contents_by_type(StateTransition)
    print(leading_tabs * '\t' + ('transitions (verbose):' if verbose else 'transitions:'))
    for transition in fsm_transitions:
        transition_name = transition.get_name() if transition.get_name() is not None else '*unnamed transition*'
        print((leading_tabs+1) * '\t' + transition_name)
        if verbose:
            transition_triggers = transition.get_triggers()
            for trigger in transition_triggers:
                print((leading_tabs+2) * '\t' + transition.get_source().get_name() + ' -- ' + trigger.get_name() + ' -> ' + transition.get_target().get_name())
            if len(transition_triggers) == 0:
                print((leading_tabs+2) * '\t' + transition.get_source().get_name() + ' ---> ' + transition.get_target().get_name())


def print_fsm(fsm, leading_tabs=0, verbose=False):
    print_states(fsm, leading_tabs, verbose)
    print_transitions(fsm, leading_tabs, verbose)
