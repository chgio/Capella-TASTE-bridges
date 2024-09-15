# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for utilities
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *

include('workspace://Capella-TASTE-bridges/verification/utils.py')
if False:
    from verification.utils import *

# path relative to workspace
aird_path = '/cloudview-obc-model/obc-model.aird'

model = CapellaModel()
model.open(aird_path)
se = model.get_system_engineering()

print('System Analysis level')
sa = se.get_system_analysis()
sa_fsms = sa.get_all_contents_by_type(StateMachine)
for fsm in sa_fsms:
    print('\t' + fsm.get_name())
    print_fsm(fsm, leading_tabs=2, verbose=True)
    print()

print('Logical Architecture level')
la = se.get_logical_architecture()
la_fsms = la.get_all_contents_by_type(StateMachine)
for fsm in la_fsms:
    print('\t' + fsm.get_name())
    print_fsm(fsm, leading_tabs=2, verbose=False)
    print()

print('Physical Architecture level')
pa = se.get_physical_architecture()
pa_fsms = pa.get_all_contents_by_type(StateMachine)
for fsm in pa_fsms:
    print('\t' + fsm.get_name())
    print_fsm(fsm, leading_tabs=2, verbose=False)
    print()
