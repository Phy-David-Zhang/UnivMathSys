/* Common Mathematical Terms */

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#ifndef UnivMath_Term_h
#define UnivMath_Term_h

#include <cstring>
#include <string>
#include <iostream>

using std::string;
using std::cout;

// Well Defined Predicate
class WellDefined: public Predicate
{
	// record define status
	bool isWellDefined;
	// method
public:
	// initialization
	WellDefined()
		{isWellDefined = false;}
	// get whether is well defined
	bool WetherWellDef()
		{return isWellDefined;}
	// update well define status
	void LetWellDef(bool WellorNot)
		{isWellDefined = WellorNot;
			ChnWellDef();}
	// output status
	void ChnWellDef()
		{if (true == isWellDefined)
			{LetSymbol("Well Defined");}
		else {LetSymbol("Ill Defined");}}
	// show status
	bool ShowWellDef()
		{cout<<GetSymbol()<<endl;
			return WetherWellDef();}
};

#endif

/* end of file */