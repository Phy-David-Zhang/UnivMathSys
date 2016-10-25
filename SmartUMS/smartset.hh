/* Extension - Smart Set */

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#ifndef SmartUMS_SmartSet_h
#define SmartUMS_SmartSet_h

#include <cstring>
#include <string>
#include <memory>

using std::string;
using namespace std;

// Construct Smart Set
class SmartSet: virtual public MathDef, public Set
{
	// smart property for smart set
	shared_ptr<Predicate> SmartProp
		= shared_ptr<Predicate>(new Predicate);
	// smart element for smart set
	shared_ptr<IndepVar> SmartElmnt
		= shared_ptr<IndepVar>(new IndepVar);
	// internal transfer of property
protected:
	Predicate* GetSmartProperty()
		{return SmartProp.get();}
	IndepVar* GetSmartElement()
		{return SmartElmnt.get();}
	// method
public:
	// initialization
	SmartSet(){this->GetElement()
		->LetRpsnt(SmartElmnt->GetRpsnt());}
	// copy constructor
	SmartSet(SmartSet &NewSet)
		{LetDefSymbol(NewSet.GetDefSymbol());
			LetSetSymbol(NewSet.GetSetSymbol());
			LetSmartElmnt(NewSet.GetSmartElmnt());
			LetSmartProp(NewSet.GetSmartProp());}
	// assignment operator
	SmartSet& operator=(SmartSet &NewSet)
		{if (&NewSet != this) {
			LetDefSymbol(NewSet.GetDefSymbol());
			LetSetSymbol(NewSet.GetSetSymbol());
			LetSmartElmnt(NewSet.GetSmartElmnt());
			LetSmartProp(NewSet.GetSmartProp());} 
		return *this;}
	// let smart set element
	void LetSmartElmnt(shared_ptr<IndepVar> NewElmnt)
		{SmartElmnt = NewElmnt;
			this->GetElement()
				->LetRpsnt(SmartElmnt->GetRpsnt());}
	// let smart set property
	void LetSmartProp(shared_ptr<Predicate> NewProp)
		{SmartProp = NewProp; ChkEligibility();}
	// get smart set element
	shared_ptr<IndepVar> GetSmartElmnt()
		{return SmartElmnt;}
	// get smart set property
	shared_ptr<Predicate> GetSmartProp()
		{return SmartProp;}
	// formulation
	Predicate Formulation()
	{
		Predicate form;
		form.LetSymbol("\\{" + 
			GetSmartElmnt()->GetSymbol() + "\\mid " + 
			GetSmartProp()->GetSymbol() + "\\}");
		form.LetTruthValue(GetStatus()
			->WetherWellDef());
		return form;
	}
};

#endif

/* end of file */