# Check the Eligibility of UnivMathSys Concepts

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Elementary.certify of UnivMathSys'''

def Check(Input, Type):
    if Type == 'function':
        if not callable(Input):
            raise TypeError("Expect function, {} provided"\
                            .format(type(Input)))
    elif not isinstance(Input, Type):
        raise TypeError("Expect {}, {} provided"\
                        .format(Type, type(Input)))
    else:
        pass

# End of Module Elementary.certify of UnivMathSys
