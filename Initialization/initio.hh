/* Initialization of Universal Mathematics System */

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#ifndef Initialization_Initio_h
#define Initialization_Initio_h

#include <cstring>
#include <string>

using std::string;

// Operation Symbol
static const string SymBelongTo = "\\in";

// Concept Independent Variable
class IndepVar
{
	// information
	string Concept = "Independent Variable";
	string Symbol;
	// representation
	void *rpsnt;
	// interface
protected:
	// switch format of rpsnt
	virtual void SwitchFormat(){}
	// method
public:
	// initialization
	IndepVar(){Symbol = "\\mu";
		rpsnt = &Symbol;}
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	void* GetRpsnt(){return rpsnt;}
	// let info
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	// let representation
	void LetRpsnt(void *Input)
		{rpsnt = Input;}
};

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
	virtual bool Condition(IndepVar *Input)
		{return false;}
	virtual void CondChn(IndepVar *Input)
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
	IndepVar *Obj = new IndepVar;
	Predicate *Prop 
		= new Predicate;
	// interface
protected:
	// reset initial
	void ResetInit()
		{Prop = new Predicate;
			Obj = new IndepVar;}
	// method
public:
	// initialization
	Class(){Symbol = "C";
		Obj->LetSymbol("x");}
	// destruction
	~Class(){delete Prop; Prop = nullptr;
		delete Obj; Obj = nullptr;}
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get property
	IndepVar* GetObject(){return Obj;}
	Predicate* GetProperty(){return Prop;}
	// let info
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	// let property
	void LetObject(IndepVar *NewObj)
		{delete Obj; Obj = NewObj;}
	void LetProperty(Predicate *NewProp)
		{delete Prop; Prop = NewProp;}
	// formulation
	Predicate ClassForm()
	{
		Predicate class_c;
		class_c.LetSymbol("\\{" + 
			Obj->GetSymbol() + "\\mid " + 
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
	static Predicate OpBelongTo(IndepVar *Obj, 
		Class *ClassC)
	{
		Predicate obj_in_c;
		obj_in_c.LetSymbol
			(Obj->GetSymbol() + " " + 
				SymBelongTo + " " + 
				ClassC->GetSymbol());
		obj_in_c.LetTruthValue
			(ClassC->GetProperty()
				->Condition(Obj));
		return obj_in_c;
	}
};

#endif

/* end of file */