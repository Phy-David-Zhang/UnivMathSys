/* Pre-definition of mathematical symbols */

#ifndef Initialization_Symbol_h
#define Initialization_Symbol_h

#include <cstring>
#include <string>

using std::string;

// Operation Symbol
static const string SymUnivQuan = "\\forall";
static const string SymExistQuan = "\\exists";
static const string SymNegation = "\\neg";
static const string SymDisjunction = "\\vee";
static const string SymConjunction = "\\wedge";
static const string SymImplication = "\\rightarrow";
static const string SymInference = "\\Rightarrow";
static const string SymSetBelongTo = "\\in";
static const string SymContain = "\\subset";
static const string SymSetEqual = "=";

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

#endif

/* end of file */