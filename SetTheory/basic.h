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
		void temp(){cout<<"tick"<<endl;}
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
	Predicate* psiC;
public:
	Set()
	{
		// information
		MathDef::Definition = "Set";
		MathDef::Symbol = "X";
		LetClass(*this);
		PropOfSet();
		// eligibility
		if (ChkEligibility()==false)
			{cout<<"Ill defined!"<<endl;}
	}
	// check eligibility
	bool ChkEligibility()
		{return Subclass::Formulation()
			.GetTruthValue();}
	// default property
	virtual void PropOfSet(){}
};


#endif

/* end of file */