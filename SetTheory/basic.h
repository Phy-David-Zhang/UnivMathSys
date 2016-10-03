/* Basic Definitions of Set Theory */

#ifndef Basic_h
#define Basic_h

#include <cstring>
#include <string>

using namespace std;

	// define class property
	class PfClass: public Predicate
	{
		Class *ClassC;
	public:
		PfClass()
			{ClassC = NULL;}
		void LetClass(Class* NewClass)
			{ClassC = NewClass;}
		bool Condition(IndepVar &Input)
		{
			bool result; 
			result = (Input.GetRpsnt() == 
				ClassC->GetObject().GetRpsnt());
			return result;
		}
	};

// Definition Subclass
class Subclass: virtual public MathDef, public Class
{
	// information
	Class ClassC;
	PfClass psifS;
	// method
public:
	// initialization
	Subclass()
	{Definition = "Subclass";
	 MathDef::Symbol = "S";
	 Property = ClassC.GetConcept()
	 	+ " " + ClassC.GetSymbol();
	 // define class
	 psifS.LetClass(this); 
	 this->LetProperty(&psifS);}
	// get info
	Class* GetClass(){return &ClassC;}
	// let info
	void LetClass(Class NewClass)
		{ClassC = NewClass;}
	// formulation
	Predicate Formulation()
	{
		Predicate form;
		// operation
		BelongTo in;
		Inference RghtArr;
		// let form
		form.LetSymbol(this->GetObject().GetSymbol() 
			+ in.GetSymbol() + " " + MathDef::Symbol
			+ RghtArr.GetSymbol() + " "
			+ ClassC.GetObject().GetSymbol()
			+ in.GetSymbol() + " "
			+ ClassC.GetSymbol());
		Predicate LeftArg = 
			in.OpBelongTo(this->GetObject(), *this);
		Predicate RghtArg = 
			in.OpBelongTo(this->GetObject(), 
				ClassC);
		form.LetTruthValue(RghtArr.OpInference(
			LeftArg, RghtArg).GetTruthValue()); 
		return form;
	}
};

class Set: virtual public MathDef, public Subclass
{
public:
	Set()
	{
		// information
		MathDef::Definition = "Set";
		MathDef::Symbol = "X";
		Class::LetSymbol("X");
		LetClass(*this);
	}
	// check eligibility
	bool ChkEligibility()
		{bool result = TestSelfContain();
		 if (result==false)
			{cout<<"Ill defined!"<<endl;}
		 return result;}
	bool TestSelfContain()
		{return Subclass::Formulation()
			.GetTruthValue();}
	// default property
	virtual void PropOfSet(){}
	// formulation
	Predicate Formulation()
	{
		Predicate Form;
		Form.LetSymbol("\\{" + 
			GetObject().GetSymbol() + "\\mid " + 
			GetProperty()->GetSymbol() + "\\}");
		Form.LetTruthValue(ChkEligibility());
		return Form;
	}
};

class Element: virtual public MathDef, public Object
{
	Set SetX;
public:
	Element()
	{
		MathDef::Definition = "Element";
		MathDef::Symbol = "x";
		LetClass(SetX);
	}
	Set GetSet(){return SetX;}
	void LetSet(Set NewSet){SetX = NewSet;}
	Predicate Formulation()
		{return ObjectForm();}
};

class Subset: virtual public MathDef, public Subclass
{
	Set SetX;
public:
	Subset()
	{
		MathDef::Definition = "Subset";
		MathDef::Symbol = "S";
		LetClass(SetX);
	}
	Set GetSet(){return SetX;}
	void LetSet(Set NewSet)
		{SetX = NewSet;
		 LetClass(SetX);}
	Predicate Formulation()
		{return Subclass::Formulation();}
};

class SetContainedIn: virtual public MathOp
{
public:
	SetContainedIn()
	{
		MathOp::Operation = "contained in";
		MathOp::Symbol = "\\subset";
	}
	Predicate OpForm(Set* Left, Set* Right)
	{
		Predicate contained_in;
		contained_in.LetSymbol(Left
			  ->MathDef::GetSymbol()
			+ MathOp::Symbol + " " 
			+ Right->MathDef::GetSymbol());
		Subclass TempSet = *Left;
		TempSet.LetClass(*Right);
		contained_in.LetTruthValue(TempSet
			.Formulation().GetTruthValue());
		return contained_in;
	}
};

class SetEqual: virtual public MathOp, 
	public SetContainedIn
{
public:
	SetEqual()
	{
		MathOp::Operation = "equal to";
		MathOp::Symbol = "=";
	}
	Predicate OpForm(Set* Left, Set* Right)
	{
		Predicate set_equal;
		set_equal.LetSymbol(Left
			  ->MathDef::GetSymbol()
			+ MathOp::Symbol 
			+ Right->MathDef::GetSymbol());
		Conjunction wedge;
		SetContainedIn contained_in;
		Predicate PredL = 
			contained_in.OpForm(Left, Right);
		Predicate PredR = 
			contained_in.OpForm(Right, Left);
		set_equal.LetTruthValue(wedge.OpConjunction(
			PredL, PredR).GetTruthValue());
		return set_equal;
	}
};

class EmptySet: virtual public MathDef, public Set
{
	Predicate Empty;
public:
	EmptySet()
	{
		MathDef::Definition = "Empty Set";
		MathDef::Symbol = "\\varnothing";
		this->LetProperty(&Empty);
		LetClass(*this);
		ChkEligibility();
	}
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