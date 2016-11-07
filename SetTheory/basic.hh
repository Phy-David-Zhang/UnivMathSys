/* Basic Definitions of Set Theory */

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#ifndef SetTheory_Basic_h
#define SetTheory_Basic_h

#include <cstring>
#include <string>
#include <iostream>

using std::string;
using std::cout;

// Definition: Set
class Set: virtual public MathDef, private Class
{
	// set property
	Predicate *SetProp = new Predicate;
	// define status
	WellDefined *Defined = new WellDefined;
	// verify define validity
protected:
	// define internal belong to predicate
	void DefineClass()
		{PredicateForClass *DefaultProp
						= new PredicateForClass;
			DefaultProp->LetClass(this);}
	// check eligibility
	bool ChkEligibility()
		{Defined->LetWellDef(TestSelfContain());
			if (Defined->WetherWellDef()==false)
				{cout<<"Ill defined!"<<endl;}
			return Defined->WetherWellDef();}
	// test self containing
	bool TestSelfContain()
		{IndepVar TempVar; TempVar.LetSymbol(
			GetSmartElement()->GetSymbol());
			ClassIntface *Temp = new ClassIntface;
			Temp->LetProperty(GetSmartProperty());
			Predicate RghtArg = BelongTo::
				OpBelongTo(&TempVar, Temp);
			Predicate LeftArg = BelongTo::
				OpBelongTo(&TempVar, this);
			Temp->Reset();
			delete Temp; Temp = nullptr;
			return Inference::OpInference(RghtArg,
				LeftArg).GetTruthValue();}
	// method
public:
	// initialization
	Set()
	{
		MathDef::Definition = "Set";
		MathDef::Symbol = "";
		Class::LetSymbol("X");
		DefineClass();
		ChkEligibility();
	}
	// destruction
	virtual ~Set()
		{delete SetProp; SetProp = nullptr;
			delete Defined; Defined = nullptr;}
	// get base concept
	string GetBase(){return GetConcept();}
	// get symbol
	string GetDefSymbol(){return MathDef::Symbol;}
	string GetSetSymbol(){return Class::GetSymbol();}
	// get element variable
	IndepVar* GetElement(){return GetObject();}
	// get set property
	Predicate* GetSetProp(){return SetProp;}
	// get define status
	WellDefined* GetStatus(){return Defined;}
	// let symbol
	void LetDefSymbol(string NewSymbol)
		{MathDef::LetSymbol(NewSymbol);}
	void LetSetSymbol(string NewSymbol)
		{Class::LetSymbol(NewSymbol);}
	// let element
	void LetElement(IndepVar *NewElement)
		{LetObject(NewElement);}
	// let set property
	void LetSetProp(Predicate *NewProp)
		{delete SetProp; SetProp = NewProp;
			ChkEligibility();}
	// smart set interface
	virtual Predicate* GetSmartProperty()
		{return GetSetProp();}
	virtual IndepVar* GetSmartElement()
		{return GetElement();}
	// default property
	virtual void PropOfSet(){}
	// formulation
	Predicate Formulation()
	{
		Predicate form;
		form.LetSymbol("\\{" + 
			GetElement()->GetSymbol() + "\\mid " + 
			GetSmartProperty()->GetSymbol() + "\\}");
		form.LetTruthValue(Defined
			->WetherWellDef());
		return form;
	}
};

	// define set property
	class PredicateForSet: public Predicate
	{
		// father set
		Set *SetX;
	public:
		// initialization
		PredicateForSet()
			{SetX = nullptr;}
		// define father set
		void LetSet(Set *NewSet)
			{SetX = NewSet;}
		// define condition
		bool Condition(IndepVar *Input)
			{return (Input->GetRpsnt() == SetX
				->GetSmartElement()->GetRpsnt());}
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
	static string GetDefSymbol()
		{return SymSetBelongTo;}
	// operation
	static Predicate OpBelongTo(IndepVar *Elmnt,
		Set *SetX)
	{
		Predicate ele_in_x;
		ele_in_x.LetSymbol
			(Elmnt->GetSymbol() + " " + 
				SymSetBelongTo + " " + 
				SetX->GetSetSymbol());
		ele_in_x.LetTruthValue
			(SetX->GetSmartProperty()
				->Condition(Elmnt));
		return ele_in_x;
	}
};

// Operation: contain in
class SetContain: virtual public MathOp
{
public:
	// initialization
	SetContain()
	{
		MathOp::Operation = "contained in";
		MathOp::Symbol = "\\subset";
	}
	// get symbol
	static string GetDefSymbol()
		{return SymContain;}
	// operation form
	static Predicate OpForm(Set *Left, Set *Rght)
	{
		Predicate contained_in;
		// let symbol
		contained_in.LetSymbol(Left
			  ->GetSetSymbol()
			+ SymContain + " " 
			+ Rght->GetSetSymbol());
		// define arguments
		Predicate LeftArg = SetBelongTo::
			OpBelongTo(Left->GetElement(), Left);
		Predicate RghtArg = SetBelongTo::
			OpBelongTo(Left->GetElement(), Rght);
		// let operation truth value
		contained_in.LetTruthValue(Inference::
			OpInference(LeftArg, RghtArg)
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
		// let form symbol
		form.LetSymbol(this->GetElement()
			->GetSymbol() + SetBelongTo::
			GetDefSymbol() + " " + GetSetSymbol()
			+ Inference::GetDefSymbol() + " "
			+ SetX->GetElement()->GetSymbol()
			+ SetBelongTo::GetDefSymbol() + " "
			+ SetX->GetSetSymbol());
		// let fomr truth value
		form.LetTruthValue(SetContain::OpForm(
			this, SetX).GetTruthValue());
		// return
		return form;
	}
};

// Operation: equal
class SetEqual: virtual public MathOp, 
	public SetContain
{
public:
	// initialization
	SetEqual()
	{
		MathOp::Operation = "equal to";
		MathOp::Symbol = "=";
	}
	// get symbol
	static string GetDefSymbol()
		{return SymSetEqual;}
	// operation form
	static Predicate OpForm(Set *Left, Set *Right)
	{
		Predicate set_equal;
		// let symbol
		set_equal.LetSymbol(Left
			  ->GetSetSymbol()
			+ SymSetEqual 
			+ Right->GetSetSymbol());
		// define arguments
		Predicate PredL = 
			SetContain::OpForm(Left, Right);
		Predicate PredR = 
			SetContain::OpForm(Right, Left);
		// let truth value
		set_equal.LetTruthValue(Conjunction::
			OpConjunction(PredL, PredR)
				.GetTruthValue());
		// return
		return set_equal;
	}
};

// Definition: Empty Set
class EmptySet: virtual public MathDef, public Set
{
public:
	// initialization
	EmptySet()
	{
		MathDef::Definition = "Empty Set";
		MathDef::Symbol = "\\varnothing";
	}
	// formulation
	Predicate Formulation()
	{
		Predicate empty_set;
		empty_set.LetSymbol(MathDef::Symbol);
		empty_set.LetTruthValue(GetStatus()
			->WetherWellDef());
		return empty_set;
	}
};

#endif

/* end of file */