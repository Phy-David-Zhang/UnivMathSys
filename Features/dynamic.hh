/* Dynamic concept for pragmatic usage */

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#ifndef Features_Dynamic_h
#define Features_Dynamic_h

#include <cstring>
#include <string>

using std::string;

// construct dynamic predicate
class DynamicPredicate: public Predicate
{
    // dyanmic condition
    bool (*Dynamic)(IndepVar *Input);
    // method
public:
    // initialization
    DynamicPredicate()
        {Dynamic = &Default;}
    // default condition
    static bool Default(IndepVar* Input)
        {return false;}
    // let dynamic condition
    void LetDynamic(bool (*NewDyn)(IndepVar *Input))
        {Dynamic = NewDyn;}
    // interface
    bool Condition(IndepVar *Input)
        {return Dynamic(Input);}
};

#endif
