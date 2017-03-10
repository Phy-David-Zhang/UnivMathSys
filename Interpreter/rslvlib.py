# Resolver Library of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Resolver Library of UnivMaths System'''


class Formulation(object):

    '''Formula Information for Resolver'''

    __slots__ = ('Formula', 'Truth', 'Tendency')

    instances = list()

    def __new__(cls, Formula, Truth, Tendency):
        for instncs in Formulation.instances:
            if instncs.Formula == Formula:
                return instncs
        return object.__new__(cls)

    def __init__(self, Formula, Truth, Tendency):
        self.Formula = Formula
        self.Truth = Truth
        self.Tendency = Tendency
        if not self in Formulation.instances:
            Formulation.instances.append(self)

    def __repr__(self):
        Tendency = lambda: "Positive" \
            if self.Tendency is True else "Negative"
        return "Formula: " + self.Formula + \
            " Truth: " + str(self.Truth) + \
            " Tendency: " + Tendency()

    def __str__(self):
        return self.__repr__()

    @classmethod
    def Reset(cls):
        cls.instances = list()


BelongTo_True = r'(' + r'?P<TRUEFORMULA>' + \
    r'[a-zA-Z\_][0-9a-zA-Z\_]*\s*' + r'\\in\s+' + \
    r'[a-zA-Z\_][0-9a-zA-Z\_]*' + r')'

BelongTo_False = r'(' + r'?P<FALSEFORMULA>' + \
    r'[a-zA-Z\_][0-9a-zA-Z\_]*\s*' + r'\\notin\s+' + \
    r'[a-zA-Z\_][0-9a-zA-Z\_]*' + r')'

BelongTo_Op = r'([a-zA-Z\_][0-9a-zA-Z\_]*\s*)' + \
    r'(?:\\in|\\notin)\s*' + \
    r'([a-zA-Z\_][0-9a-zA-Z\_]*)'

BasicFormulation = \
[
    BelongTo_True, BelongTo_False
]

BasicOperation = \
[
    BelongTo_Op
]


# End of Resolver Library of UnivMathSys
