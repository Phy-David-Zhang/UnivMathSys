/* Initialization of Universal Mathematics System */

#ifndef Initialization_h
#define Initialization_h

#include <cstring>
#include <string>

using std::string;

// Concept Predicate
class Predicate
{
	// information
	string Concept = "Predicate";
	string Symbol;
	// property
	bool TruthValue;
	// methods
public:
	// initialization
	Predicate(){Symbol = "\\mu";
		 TruthValue = false;}
	// condition
	virtual bool Condition(IndepVar &Input)
		{return false;}
	virtual void CondChn(IndepVar &Input)
		{TruthValue = Condition(Input);}
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get property
	bool GetTruthValue(){return TruthValue;}
	// let info
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	// let property
	void LetTruthValue(bool NewTruthValue)
		{TruthValue = NewTruthValue;}
};

// Concept Class
class Class
{
	// information
	string Concept = "Class";
	string Symbol;
	// property
	IndepVar Obj;
	Predicate *Prop 
		= new Predicate;
	// interface
protected:
	// reset initial
	void ResetInit(){Prop = new Predicate;}
	// method
public:
	// initialization
	Class(){Symbol = "C";
		Obj.LetSymbol("x");}
	// destruction
	~Class(){delete Prop; Prop = nullptr;}
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get property
	IndepVar GetObject(){return Obj;}
	Predicate* GetProperty(){return Prop;}
	// let info
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	// let property
	void LetObject(IndepVar NewObj)
		{Obj = NewObj;}
	void LetProperty(Predicate *NewProp)
		{delete Prop; Prop = NewProp;}
	// formulation
	Predicate ClassForm()
	{
		Predicate class_c;
		class_c.LetSymbol("\\{" + 
			Obj.GetSymbol() + "\\mid " + 
			Prop->GetSymbol() + "\\}");
		class_c.LetTruthValue(true);
		return class_c;
	}
};

// Concept Object
class Object
{
	// information
	string Concept = "Object";
	string Symbol;
	// property
	Class *ClassC = new Class;
	// interface
protected:
	// reset initial
	void ResetInit(){ClassC = new Class;}
	// method
public:
	// initialization
	Object(){Symbol = "x";}
	~Object(){delete ClassC; ClassC = nullptr;}
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get property
	Class* GetClass(){return ClassC;}
	// let info
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	// let property
	void LetClass(Class *NewClass)
		{delete ClassC; ClassC = NewClass;}
	// formulation
	Predicate ObjectForm()
	{
		Predicate object_x;
		object_x.LetSymbol(Symbol);
		object_x.LetTruthValue(true);
		return object_x;
	}
};

// Operation belong to
class BelongTo
{
	// information
	string Concept = "belong to";
	string Symbol = "\\in";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// formulation
	Predicate OpBelongTo(IndepVar Obj, 
		Class *ClassC)
	{
		Predicate obj_in_c;
		obj_in_c.LetSymbol
			(Obj.GetSymbol() + " " + 
				Symbol + " " + 
				ClassC->GetSymbol());
		obj_in_c.LetTruthValue
			(ClassC->GetProperty()
				->Condition(Obj));
		return obj_in_c;
	}
};

#endif

/* end of file */