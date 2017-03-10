# Formula Library of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Formula Library of UnivMaths System'''


from Foundation.basic import Variable
from Foundation.set import Set
from Foundation.setop import SetAST


# generate name for identifiers
GenID = lambda id: r'(?P<' + id + r'>' + \
    r'[a-zA-Z\_][0-9a-zA-Z\_]*)'

BasicFormulas = \
{
    Variable._Identify: "Identifier",
    Set._Identify : "Set"
}

GeneralFormulas = \
{
    SetAST() : "Set"
}


# End of Formula Library of UnivMathSys
