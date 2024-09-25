# name                 : Print all FSMs
# script-type          : Python
# description          : Prints to console all FSMs of the selected SystemEngineering element
# popup                : enableFor(org.polarsys.capella.core.data.capellamodeller.SystemEngineering)
#

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

try:
    # if called from UI, start from the selected SystemEngineering element in the open project
    specific_cls = EObject.get_class(CapellaPlatform.getFirstSelectedElement())
    se = specific_cls(CapellaPlatform.getFirstSelectedElement())
except:
    # if called from CLI:
    if len(argv) != 1:
        # load the IFE model
        aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
    else:
        # load the Capella model from the first argument of the script
        aird_path = argv[0]
    model = CapellaModel()
    model.open(aird_path)
    se = model.get_system_engineering()

print('System Analysis level')
sa = se.get_system_analysis()
sa_fsms = sa.get_all_contents_by_type(StateMachine)
for fsm in sa_fsms:
    print(fsm.as_string(leading_tabs=1, verbose=True))
    print()

print('Logical Architecture level')
la = se.get_logical_architecture()
la_fsms = la.get_all_contents_by_type(StateMachine)
for fsm in la_fsms:
    print(fsm.as_string(leading_tabs=1, verbose=False))
    print()

print('Physical Architecture level')
pa = se.get_physical_architecture()
pa_fsms = pa.get_all_contents_by_type(StateMachine)
for fsm in pa_fsms:
    print(fsm.as_string(leading_tabs=1, verbose=False))
    print()
