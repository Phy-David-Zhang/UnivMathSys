/* Support methods of initialization */

#ifndef SetTheory_Support_h
#define SetTheory_Support_h

#include <cstring>
#include <string>

using std::string;

	// define class property
	class PredicateForClass: public Predicate
	{
		// father class
		Class *ClassC;
	public:
		// initialization
		PredicateForClass()
			{ClassC = NULL;}
		// define father class
		void LetClass(Class *NewClass)
			{ClassC = NewClass;}
		// define condition
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
	Class *ClassC = NULL;
	// method
public:
	// initialization
	Subclass()
	{
		// information
		MathDef::Definition = "Subclass";
		MathDef::Symbol = "S";
		DefineClass();
	}
	// define non-empty class
	void DefineClass()
	{
		PredicateForClass *SubclassSProp
			= new PredicateForClass;
		SubclassSProp->LetClass(this);
		this->LetProperty(SubclassSProp);
	}
	// define empty class
	void EmptyClass()
	{
		Predicate *Empty = new Predicate;
		this->LetProperty(Empty);
	}
	// get info
	Class* GetClass(){return ClassC;}
	// let info
	void LetClass(Class &NewClass)
		{ClassC = &NewClass;}
	// formulation
	Predicate Formulation()
	{
		Predicate form;
		// operation
		BelongTo in;
		Inference RghtArr;
		// let form symbol
		form.LetSymbol(this->GetObject().GetSymbol()
			+ in.GetSymbol() + " " + MathDef::Symbol
			+ RghtArr.GetSymbol() + " "
			+ ClassC->GetObject().GetSymbol()
			+ in.GetSymbol() + " "
			+ ClassC->GetSymbol());
		// let temp class ptr
		Class *Temp; Temp = this;
		// define arguments
		Predicate LeftArg = 
			in.OpBelongTo(this->GetObject(), Temp);
		Predicate RghtArg = 
			in.OpBelongTo(this->GetObject(), 
				ClassC);
		// let form truth value
		form.LetTruthValue(RghtArr.OpInference(
			LeftArg, RghtArg).GetTruthValue());
		// return
		return form;
	}
};

// interface to reset class property
class ClassInterface: public Class
{
public:
	void Reset(){ResetInit();}
};

#endif

/* end of file */