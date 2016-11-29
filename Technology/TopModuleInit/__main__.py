# Entry File of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Entry File of UnivMathSys'''

import os, sys
import Technology.main
import Technology.test
import Technology.link

if __name__ == "__main__":

    if sys.argv[1] == "test":
        Technology.test.TestRun()
    elif sys.argv[1] == "link":
        pass
    else:
        Technology.main.Success()

# End of Entry File of UnivMathSys
