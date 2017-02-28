# Formula Library of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Formula Library of UnivMaths System'''

Formulas = \
{
    r'([a-zA-Z\_][0-9a-zA-Z\_]*)' + r'\\in' + \
    r'([a-zA-Z\_][0-9a-zA-Z\_]*)' : "RawPredicate",

    r'(Contain\(.+\))|(SetEq\(.+\))' : "GenPredicate",

    r'(Neg\(.+\))|(Conjunc\(.+\))|(Disjunc\(.+\))' + \
    r'|(Imply\(.+\))' : "Logic",

    r'(?:{|\\{)\s*' + r'(.+?)(?:\\in\s+(.+))?\s*' + \
    r'(?:\||\\mid\s)\s*' + r'(.+?)' + r'(?:}|\\})' : "Set",

    r'(Union\(.+\))|(Intsct\(.+\))|(Complt\(.+\))' + \
    r'|(CartProct\(.+\))' : "SetOp"
}


# End of Formula Library of UnivMathSys
