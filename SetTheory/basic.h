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
		PfClass(Class *NewClass)
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
class Subclass: public MathDef, public Class
{
	// information
	Class ClassC;
	// method
public:
	// initialization
	Subclass()
	{Definition = "Subclass";
	 MathDef::Symbol = "S";
	 Property = ClassC.GetConcept()
	 	+ " " + ClassC.GetSymbol();}
	// get info
	Class GetClass(){return ClassC;}
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
		// define class
		PfClass psifC(&ClassC); 
		this->LetProperty(&psifS); 
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
			in.OpBelongTo(ClassC.GetObject(), 
				ClassC);
		form.LetTruthValue(RghtArr.OpInference(
			LeftArg, RghtArg).GetTruthValue()); 
		return form;
	}
};




#endif

/* end of file */