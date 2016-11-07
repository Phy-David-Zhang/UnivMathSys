/* This is to test whether the system identifies
   Russell class, which means providing error 
   message when defining Russell class as a set. */

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#ifndef SetTheory_Russell_h
#define SetTheory_Russell_h

#include <cstring>
#include <string>

using std::string;

	// define property of Russell class
	class PredicateForRussell: public Predicate
	{
		// property
		Set *SetX;
		// method
	public:
		// initialization
		PredicateForRussell()
			{SetX = nullptr;}
		// let set
		void LetSet(Set *NewSet)
			{SetX = NewSet;}
		// define condition
		bool Condition(IndepVar *Input)
		{
			LetSymbol(Input->GetSymbol() + 
				"\\notin " + SetX->GetSetSymbol());
			return !(Input->GetRpsnt() == 
				SetX->GetElement()->GetRpsnt());
		}
	};

// Definition: Russell Class
class Russell: virtual public MathDef, public Set
{
public:
	// initialization
	Russell()
		{MathDef::Definition = "Russell Class";
			PropOfSet();}
	// define property
	void PropOfSet()
	{
		PredicateForRussell *RussellPredicate
			= new PredicateForRussell;
		RussellPredicate->LetSet(this);
		LetSetProp(RussellPredicate);
	}
	// formulation
	Predicate Formulation()
	{
		Predicate Form;
		Form.LetSymbol("\\{" + 
			GetElement()->GetSymbol() + "\\mid " + 
			GetSetProp()->GetSymbol() + "\\}");
		Form.LetTruthValue(GetStatus()
			->WetherWellDef());
		return Form;
	}
};

#endif

/* end of file */