/* Pre-definition of mathematical symbols */

#ifndef Initialization_Symbol_h
#define Initialization_Symbol_h

#include <cstring>
#include <string>

using std::string;

// Concept Symbol
class Symbol
{
	// information
	string Concept = "Symbol";
	string SymbolSet = "\\latex2e";
	// method
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbolSet(){return SymbolSet;}
};

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

#endif

/* end of file */