/* Standard elements of Mathematics */

#ifndef Standard_h
#define Standard_h

#include <cstring>
#include <string>

using std::string;

// Definition
class MathDef
{
protected:
	// information
	string Definition;
	string Symbol;
	string Property;
	// universal method
public:
	// initialization
	MathDef()
		{Definition = "";
		 Symbol = ""; 
		 Property = "";}
	// get info
	string GetDefinition()
		{return Definition;}
	string GetSymbol()
		{return Symbol;}
	string GetMathProperty()
		{return Property;}
	// let info
	void LetDefinition(string Def)
		{Definition = Def;}
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	void LetMathProperty(string Prop)
		{Property = Prop;}
	// formulation
	virtual Predicate Formulation() = 0;
};

class MathOp
{
protected:
	// information
	string Operation;
	string Symbol;
	string Property;
	// universal method
public:
	// initialization
	MathOp()
		{Operation = "";
		 Symbol = ""; 
		 Property = "";}
	// get info
	string GetOperation()
		{return Operation;}
	string GetSymbol()
		{return Symbol;}
	string GetProperty()
		{return Property;}
	// let info
	void LetOperation(string Op)
		{Operation = Op;}
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	void LetProperty(string Prop)
		{Property = Prop;}
	// formulation
	virtual Predicate OpForm(void *Left,
		void *Right) {};
};

#endif

/* end of file */