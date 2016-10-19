/* Extension - Smart Set */

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
	// internal transfer of property
protected:
	Predicate* GetSmartProperty()
		{return SmartProp.get();}
	// method
public:
	// initialization
	SmartSet(){}
	// copy constructor
	SmartSet(SmartSet &NewSet)
		{LetDefSymbol(NewSet.GetDefSymbol());
			LetSetSymbol(NewSet.GetSetSymbol());
			LetElement(NewSet.GetElement());
			LetSmartProp(NewSet.GetSmartProp());}
	// assignment operator
	SmartSet& operator=(SmartSet &NewSet)
		{if (&NewSet != this) {
			LetDefSymbol(NewSet.GetDefSymbol());
			LetSetSymbol(NewSet.GetSetSymbol());
			LetElement(NewSet.GetElement());
			LetSmartProp(NewSet.GetSmartProp());} 
		return *this;}
	// let smart set property
	void LetSmartProp(shared_ptr<Predicate> NewProp)
		{SmartProp = NewProp;
			UpdateAndChk(GetSmartProperty());}
	// get smart set property
	shared_ptr<Predicate> GetSmartProp()
		{return SmartProp;}
	// formulation
	Predicate Formulation()
	{
		Predicate form;
		form.LetSymbol("\\{" + 
			GetElement().GetSymbol() + "\\mid " + 
			GetSmartProp()->GetSymbol() + "\\}");
		form.LetTruthValue(GetStatus()
			->WetherWellDef());
		return form;
	}
};

#endif

/* end of file */