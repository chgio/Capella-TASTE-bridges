# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for utilities
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *

from io import StringIO


def fsm_states_as_string(self, leading_tabs=0, verbose=False) -> str:
    states_string = StringIO() # string to print to
    fsm_states = self.get_all_contents_by_type(State)
    print(leading_tabs * '\t' + ('states (verbose):' if verbose else 'states:'), file=states_string)
    for state in fsm_states:
        print((leading_tabs+1) * '\t' + state.get_name(), file=states_string)
        if verbose:
            state_outgoing_transitions = state.get_outgoing()
            for transition in state_outgoing_transitions:
                transition_name = transition.get_name() if transition.get_name() is not None else '*unnamed transition*'
                print((leading_tabs+2) * '\t' + transition_name, file=states_string)
                transition_triggers = transition.get_triggers()
                for trigger in transition_triggers:
                    print((leading_tabs+3) * '\t' + ' -- ' + trigger.get_name() + ' -> ' + transition.get_target().get_name(), file=states_string)
                if len(transition_triggers) == 0:
                    print((leading_tabs+3) * '\t' + ' ---> ' + transition.get_target().get_name(), file=states_string)
    return states_string.getvalue()


def fsm_transitions_as_string(self, leading_tabs=0, verbose=False) -> str:
    transitions_string = StringIO() # string to print to
    fsm_transitions = self.get_all_contents_by_type(StateTransition)
    print(leading_tabs * '\t' + ('transitions (verbose):' if verbose else 'transitions:'), file=transitions_string)
    for transition in fsm_transitions:
        transition_name = transition.get_name() if transition.get_name() is not None else '*unnamed transition*'
        print((leading_tabs+1) * '\t' + transition_name, file=transitions_string)
        if verbose:
            transition_triggers = transition.get_triggers()
            for trigger in transition_triggers:
                print((leading_tabs+2) * '\t' + transition.get_source().get_name() + ' -- ' + trigger.get_name() + ' -> ' + transition.get_target().get_name(), file=transitions_string)
            if len(transition_triggers) == 0:
                print((leading_tabs+2) * '\t' + transition.get_source().get_name() + ' ---> ' + transition.get_target().get_name(), file=transitions_string)
    return transitions_string.getvalue()


def fsm_as_string(self, leading_tabs=0, verbose=False) -> str:
    name_string = self.get_name()
    states_string = fsm_states_as_string(self, leading_tabs+1, verbose)
    transitions_string = fsm_transitions_as_string(self, leading_tabs+1, verbose)
    return leading_tabs * '\t' + name_string + '\n' + states_string + '\n' + transitions_string


if __name__ == '__main__':
    StateMachine.states_as_string = fsm_states_as_string
    StateMachine.transitions_as_string = fsm_transitions_as_string
    StateMachine.as_string = fsm_as_string
