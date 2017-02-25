# Language Compiler of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Interface Language Compiler of UnivMathSys'''


import re
from .exeinit import ExeInit


# Form: let ... be ...
LetBeForm = r'let\s+(.*)\s+be\s+(\w*)\s*'
# Form: let ... be ... of ...
LetBeOfForm = \
    r'let\s+(.*)\s+be\s+(\w*)\s+of\s+(\w*)\s*'
# Form: let ... of ... be ...
LetOfBeForm = \
    r'let\s+(\w*)\s+of\s+(.*)\s+be\s+([.*\s*]*.+)'

# compile syntax
LetBeSyntax = re.compile(LetBeForm)
LetBeOfSyntax = re.compile(LetBeOfForm)
LetOfBeSyntax = re.compile(LetOfBeForm)


# compile given sentences
def Compile(sntces):

    # if match 'let ... of ... be ...' form
    if re.match(LetOfBeForm, sntces):
        Info = LetOfBeSyntax.match(sntces).groups()
        # extract names
        Info = [re.split(r'[\s\,]+', Info[1])]\
            + [Info[0]] + [info for info in Info[2:]]
        # generate commands
        Command = ""
        for Name in Info[0]:
            Command += Name + "." + Info[1] + "=" \
                + Info[2] + "\n"
        return Command

    # if match 'let ... be ...' form
    elif re.match(LetBeForm, sntces):
        Info = LetBeSyntax.match(sntces).groups()
        # extract names
        Info = [re.split(r'[\s\,]+', Info[0])]\
            + [info for info in Info[1:]]
        # generate commands
        Command = ""
        for Name in Info[0]:
            # create instance
            Command += Name + "=" + Info[1] + "()\n"
            # set symbol of instance
            Command += Name + ".Symbol='" \
                + Name + "'\n"
            # other initialization
            Temp = ExeInit(Name, Info[1])
            if Temp:
                Command += Temp
        return Command

    elif re.match(LetBeOfForm, sntces):
        Info = LetBeOfSyntax.match(sntces).groups()
        # extract names
        Info = [re.split(r'[\s\,]+', Info[0])]\
            + [info for info in Info[1:]]
        # generate commands
        Command = ""
        for Name in Info[0]:
            # create instance
            Command += Name + "=" + Info[1] \
                + "(" + Info[2] + ")\n"
            # set symbol of instance
            Command += Name + ".Symbol='" \
                + Name + "'\n"
            # other initialization
            Temp = ExeInit(Name, Info[1])
            if Temp:
                Command += Temp
        return Command

    # return None if match fails
    else:
        return None


# End of Compiler of UnivMathSys
