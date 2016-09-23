/* Pre-definition of mathematical symbols */

#include <cstring>
#include <string>

using namespace std;

// Concept Symbol
class Symbol
{
	string Concept = "Symbol";
	string SymbolSet = "\latex2e";
public:
	string GetConcept(){return Concept;}
	string GetSymbolSet(){return SymbolSet;}
};

// Concept Independent Variable
class IndepVar
{
	string Concept = "Independent Variable";
	string Symbol;
public:
	IndepVar(){Symbol = "\mu";}
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	void LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
};
