/* Basic Definitions of Set Theory */

#ifndef Basic_h
#define Basic_h

#include <cstring>
#include <string>
#include <iostream>

using std::string;
using std::cout;

// Definition: Set
class Set: virtual public MathDef, public Subclass
{
public:
	// initialization
	Set()
	{
		// information
		MathDef::Definition = "Set";
		MathDef::Symbol = "X";
		Class::LetSymbol("X");
		PropOfSet();
		ChkEligibility();
	}
	// check eligibility
	bool ChkEligibility()
		{bool result = TestSelfContain();
		 if (result==false)
			{cout<<"Ill defined!"<<endl;}
		 return result;}
	// test self containing
	bool TestSelfContain()
		{return Subclass::Formulation()
			.GetTruthValue();}
	// default property
	virtual void PropOfSet(){LetClass(*this);}
	// formulation
	Predicate Formulation()
	{
		Predicate form;
		form.LetSymbol("\\{" + 
			GetObject().GetSymbol() + "\\mid " + 
			GetProperty()->GetSymbol() + "\\}");
		form.LetTruthValue(ChkEligibility());
		return form;
	}
};

// Definition: Element
class Element: virtual public MathDef
{
	// property
	Set *SetX = new Set;
	// method
public:
	// initialization
	Element(){
		MathDef::Definition = "Element";
		MathDef::Symbol = "x";}
	// destruction
	~Element(){delete SetX; SetX = nullptr;}
	// get property
	Set* GetSet(){return SetX;}
	// let property
	void LetSet(Set *NewSet)
		{delete SetX; SetX = NewSet;}
	// formulation
	Predicate Formulation()
	{
		Predicate element_x;
		element_x.LetSymbol(Symbol);
		element_x.LetTruthValue(true);
		return element_x;
	}
};

// Definition: Subset
class Subset: virtual public MathDef, public Subclass
{
	// property
	Set *SetX = new Set;
	// method
public:
	// initialization
	Subset()
	{
		MathDef::Definition = "Subset";
		MathDef::Symbol = "S";
		LetClass(*SetX);
	}
	// destruction
	~Subset(){delete SetX; SetX = nullptr;}
	// get property
	Set* GetSet(){return SetX;}
	// let property
	void LetSet(Set *NewSet)
		{delete SetX; SetX = NewSet;
		 LetClass(*SetX);}
	// formulation
	Predicate Formulation()
		{return Subclass::Formulation();}
};

// Operation: contain in
class SetContainedIn: virtual public MathOp
{
public:
	// initialization
	SetContainedIn()
	{
		MathOp::Operation = "contained in";
		MathOp::Symbol = "\\subset";
	}
	// operation form
	Predicate OpForm(Set *Left, Set *Right)
	{
		Predicate contained_in;
		// let symbol
		contained_in.LetSymbol(Left
			  ->MathDef::GetSymbol()
			+ MathOp::Symbol + " " 
			+ Right->MathDef::GetSymbol());
		// define subclass
		Subclass *TempSet; TempSet = Left;
		TempSet->LetClass(*Right);
		// let truth value
		contained_in.LetTruthValue(TempSet
			->Formulation().GetTruthValue());
		// return
		return contained_in;
	}
};

// Operation: equal
class SetEqual: virtual public MathOp, 
	public SetContainedIn
{
public:
	// initialization
	SetEqual()
	{
		MathOp::Operation = "equal to";
		MathOp::Symbol = "=";
	}
	// operation form
	Predicate OpForm(Set *Left, Set *Right)
	{
		Predicate set_equal;
		// let symbol
		set_equal.LetSymbol(Left
			  ->MathDef::GetSymbol()
			+ MathOp::Symbol 
			+ Right->MathDef::GetSymbol());
		// define operator
		Conjunction wedge;
		SetContainedIn contained_in;
		// define arguments
		Predicate PredL = 
			contained_in.OpForm(Left, Right);
		Predicate PredR = 
			contained_in.OpForm(Right, Left);
		// let truth value
		set_equal.LetTruthValue(wedge.OpConjunction(
			PredL, PredR).GetTruthValue());
		// return
		return set_equal;
	}
};

// Definition: Empty Set
class EmptySet: virtual public MathDef, public Set
{
	// property
	Predicate *Empty = new Predicate;
	// method
public:
	// initialization
	EmptySet()
	{
		MathDef::Definition = "Empty Set";
		MathDef::Symbol = "\\varnothing";
		this->LetProperty(Empty);
		LetClass(*this);
		ChkEligibility();
	}
	// formulation
	Predicate Formulation()
	{
		Predicate empty_set;
		empty_set.LetSymbol(MathDef::Symbol);
		empty_set.LetTruthValue(ChkEligibility());
		return empty_set;
	}
};

#endif

/* end of file */