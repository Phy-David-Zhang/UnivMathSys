/* Pre-definition of mathematical symbols */

#ifndef Symbol_h
#define Symbol_h

#include <cstring>
#include <string>

using namespace std;

// Concept Symbol
class Symbol
{
	// information
	string Concept = "Symbol";
	string SymbolSet = "\latex2e";
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
	// method
public:
	// initialization
	IndepVar(){Symbol = "\mu";
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