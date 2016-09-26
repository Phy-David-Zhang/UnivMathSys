/* Initialization of Universal Mathematics System */

#ifndef Initialization_h
#define Initialization_h

#include <cstring>
#include <string>

using namespace std;

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
	Predicate(){Symbol = "\mu";
		 TruthValue = false;}
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
	// condition
	virtual bool Condition(IndepVar &Input)
		{return false;}
	virtual void CondChn(IndepVar &Input)
		{TruthValue = Condition(Input);}
};

class Class
{
	// information
	string Concept = "Class";
	string Symbol;
	// property
	IndepVar Objt;
	Predicate Prop;
	// method
public:
	// initialization
	Class(){Symbol = "C";}
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get property
	IndepVar GetObject(){return Objt;}
	Predicate GetProperty(){return Prop;}
	// let info
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	// let property
	void LetObject(IndepVar NewObjt)
		{Objt = NewObjt;}
	void LetProperty(Predicate NewProp)
		{Prop = NewProp;}
	// formulation
	Predicate ClassForm()
	{
		Predicate class_c;
		class_c.LetSymbol("\{" + 
			Objt.GetSymbol() + "\mid " + 
			Prop.GetSymbol() + "\}");
		class_c.LetTruthValue(true);
		return class_c;
	}
};

class Object
{
	// information
	string Concept = "Object";
	string Symbol;
	// property
	Class Class_C;
	// method
public:
	// initialization
	Object(){Symbol = "x";}
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get property
	Class GetClass(){return Class_C;}
	// let info
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	// let property
	void LetClass(Class NewClass)
		{Class_C = NewClass;
		 Symbol = Class_C.GetObject().GetSymbol();}
	// formulation
	Predicate ObjectForm()
	{
		Predicate object_x;
		object_x.LetSymbol
			(Class_C.GetObject().GetSymbol());
		object_x.LetTruthValue(true);
	}
};

class BelongTo
{
	// information
	string Concept = "belong to";
	string Symbol = "\in";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// formulation
	Predicate OpBelongTo(Object &Objt, 
		Class Class_C)
	{
		Predicate obj_in_c;
		obj_in_c.LetSymbol
			(Objt.GetSymbol() + " " + 
				Symbol + " " + 
				Class_C.GetSymbol());
		obj_in_c.LetTruthValue
			((Objt.GetClass().GetSymbol() ==
				Class_C.GetSymbol()));
	}
};

#endif

/* end of file */