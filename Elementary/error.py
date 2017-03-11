# Error Report and Exception Raise of UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Elementary.error of UnivMathSys'''

import logging

StrHndlr = logging.StreamHandler()
StrHndlr.setFormatter(logging.Formatter\
    ('%(message)s'))

Logger = logging.getLogger('Error')
Logger.setLevel('WARNING')
Logger.addHandler(StrHndlr)

class Error(Exception):
    pass

class LogicError(Error):

    def __init__(self, msg):
        msg = "LogicError: " + msg
        Logger.critical(msg)

class IllDefined(Error):
    pass

class AccessError(Error):
    pass

class IntpnError(Error):
    pass

class Insufficiency(Error):

    def __init__(self):
        msg = "Warning: "
        msg += "Deduction Condition Insufficient"
        Logger.warn(msg)

class MatchError(Error):
    pass

class FormulaError(Error):
    pass

# End of Module Elementary.error of UnivMathSys
