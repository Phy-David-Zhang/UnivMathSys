# Alphabet and other Symbol List for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Interpreter.alphabet of UnivMathSys'''

Greek_Lower = ['alpha', 'beta', 'gamma', 'delta',
         'epsilon', 'varepsilon', 'zeta', 'eta',
         'theta', 'vartheta', 'iota', 'kappa',
         'lamda', 'mu', 'nu', 'xi', 'pi', 'varpi',
         'rho', 'varrho', 'sigma', 'varsigma',
         'tau', 'upsilon', 'phi', 'varphi', 'chi',
         'psi', 'omega']

Greek_Upper = ['Gamma', 'Delta', 'Theta', 'Lambda',
               'Xi', 'Pi', 'Sigma', 'Upsilon', 'Phi',
               'Psi', 'Omega']

var_Greek_Upper = ['var' + Greek for Greek
    in Greek_Upper]

Greek_Upper = Greek_Upper + var_Greek_Upper

Greek_Lower_LaTeX = ['\\' + Greek for Greek
    in Greek_Lower]

Greek_Upper_LaTeX = ['\\' + Greek for Greek
    in Greek_Upper]

Greek = Greek_Upper + Greek_Lower
Greek_LaTeX = Greek_Upper_LaTeX + Greek_Lower_LaTeX
