/* Basic Definitions of Set Theory */

#ifndef Basic_h
#define Basic_h

#include <cstring>
#include <string>
#include <iostream>

using std::string;
using std::cout;

// Definition: Set
class Set: virtual public MathDef, private Subclass
{
	// set property
	Predicate* SetProp = new Predicate;
public:
	// initialization
	Set()
	{
		MathDef::Definition = "Set";
		MathDef::Symbol = "X";
		Class::LetSymbol("X");
		PropOfSet();
		ChkEligibility();
	}
	// destruction
	virtual ~Set()
		{delete SetProp; SetProp = nullptr;}
	// let whether set is empty
	void isEmpty(bool SetEmpty = false)
		{if (false == SetEmpty) {DefineClass();}
			else {EmptyClass();}}
	// get base concept
	string GetBase(){return GetConcept();}
	// get symbol
	string GetDefSymbol(){return MathDef::Symbol;}
	string GetSetSymbol(){return Class::GetSymbol();}
	// get element variable
	IndepVar GetElement(){return GetObject();}
	// get set property
	Predicate* GetSetProp(){return SetProp;}
	// let symbol
	void LetDefSymbol(string NewSymbol)
		{MathDef::LetSymbol(NewSymbol);}
	void LetSetSymbol(string NewSymbol)
		{Class::LetSymbol(NewSymbol);}
	// let element
	void LetElement(IndepVar NewElement)
		{LetObject(NewElement);}
	// let set property
	void LetSetProp(Predicate *NewProp)
		{delete SetProp; SetProp = NewProp;
			UpdateAndChk();}
	// update property info and check
	void UpdateAndChk()
		{ClassInterface *Temp = new ClassInterface;
			Temp->LetObject(GetObject());
			Temp->LetProperty(SetProp);
			LetClass(*Temp); ChkEligibility();
			Temp->Reset();
			delete Temp; Temp = nullptr;}
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

// Operation belong to
class SetBelongTo: virtual public MathOp,
	private BelongTo
{
public:
	// initialization
	SetBelongTo()
	{
		MathOp::Operation = GetConcept();
		MathOp::Symbol = BelongTo::GetSymbol();
	}
	// get symbol
	string GetDefSymbol(){return MathOp::Symbol;}
	// operation
	Predicate OpBelongTo(IndepVar Elmnt,
		Set *SetX)
	{
		Predicate ele_in_x;
		ele_in_x.LetSymbol
			(Elmnt.GetSymbol() + " " + 
				MathOp::Symbol + " " + 
				SetX->GetSetSymbol());
		ele_in_x.LetTruthValue
			(SetX->GetSetProp()
				->Condition(Elmnt));
		return ele_in_x;
	}
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
	Predicate OpForm(Set *Left, Set *Rght)
	{
		Predicate contained_in;
		Inference RghtArr;
		SetBelongTo in;
		// let symbol
		contained_in.LetSymbol(Left
			  ->MathDef::GetSymbol()
			+ MathOp::Symbol + " " 
			+ Rght->MathDef::GetSymbol());
		// define arguments
		Predicate LeftArg = 
			in.OpBelongTo(Left->GetElement(), Left);
		Predicate RghtArg = 
			in.OpBelongTo(Left->GetElement(), Rght);
		// let operation truth value
		contained_in.LetTruthValue(RghtArr
			.OpInference(LeftArg, RghtArg)
			.GetTruthValue()); 
		// return
		return contained_in;
	}
};

// Definition: Subset
class Subset: virtual public MathDef, public Set
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
	}
	// destruction
	~Subset(){delete SetX; SetX = nullptr;}
	// get property
	Set* GetSet(){return SetX;}
	// let property
	void LetSet(Set *NewSet)
		{delete SetX; SetX = NewSet;}
	// formulation
	Predicate Formulation()
	{
		Predicate form;
		Inference RghtArr;
		// operation
		SetBelongTo in;
		SetContainedIn contained_in;
		// let form symbol
		form.LetSymbol(this->GetElement()
			.GetSymbol() + in.GetDefSymbol() + " " 
			+ MathDef::Symbol
			+ RghtArr.GetSymbol() + " "
			+ SetX->GetElement().GetSymbol()
			+ in.GetDefSymbol() + " "
			+ SetX->GetSetSymbol());
		// let fomr truth value
		form.LetTruthValue(contained_in.OpForm(
			this, SetX).GetTruthValue());
		// return
		return form;
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
		isEmpty(true);
		this->LetSetProp(Empty);
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