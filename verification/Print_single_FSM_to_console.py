# name                 : Print single FSM
# script-type          : Python
# description          : Prints to console the selected FSM
# popup                : enableFor(org.polarsys.capella.core.data.capellacommon.StateMachine)
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
    # if called from UI, start from the selected StateMachine element in the open project
    specific_cls = EObject.get_class(CapellaPlatform.getFirstSelectedElement())
    fsm = specific_cls(CapellaPlatform.getFirstSelectedElement())
except:
    # if called from CLI:
    if len(argv) != 2:
        # load the IFE model
        aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
        fsm_level_arg = 'System'
        fsm_name_arg = 'IFE Operating Modes'
    else:
        # load the Capella model from the first argument of the script
        aird_path = argv[0]
        (fsm_level_arg, fsm_name_arg) = argv[1].strip().split('/')
        
    model = CapellaModel()
    model.open(aird_path)
    se = model.get_system_engineering()
    fsm_level_getters_dict = {
        'Operational': se.get_operational_analysis,
        'System': se.get_system_analysis,
        'Logical': se.get_logical_architecture,
        'Physical': se.get_physical_architecture    
    }
    fsm_level = fsm_level_getters_dict[fsm_level_arg]()
    level_fsms = fsm_level.get_all_contents_by_type(StateMachine)
    fsm = [ fsm for fsm in level_fsms if fsm.get_name() == fsm_name_arg ][0]

print(fsm.get_name())
print_fsm(fsm, leading_tabs=1, verbose=True)
