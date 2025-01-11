
# < ====================================
# < Imports
# < ====================================

import mytools
from mytools import moduleA
import mytools.moduleA
from mytools.moduleA import cprint

# < ====================================
# < Execution
# < ====================================

mytools.moduleA.cprint(1)
moduleA.cprint(2)
cprint(3)