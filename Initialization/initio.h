/* Initialization of Universal Mathematics System. */

#ifndef Initialization
#define Initialization

#include <cstring>

// Concept Symbol
class Symbol
{
	string Concept = "Symbol";
	string SymbolSet = "\latex2e";
public:
	GetConcept(){return Concept;}
	GetSymbolSet(){return SymbolSet;}
}

class IndepVar
{
	string Concept = "Independent Variable";
	string Symbol;
public:
	IndepVar(){Symbol = "\mu";}
	GetConcept(){return Concept;}
	GetSymbol(){return Symbol;}
	LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
}

class Predicate
{
	string Concept = "Predicate";
	string Symbol;
	bool TruthValue;
public:
	Predicate(){Symbol = "\mu";
		 TruthValue = false;}
	GetConcept(){return Concept;}
	GetSymbol(){return Symbol;}
	LetSymbol(string NewSymbol)
		{Symbol = NewSymbol;}
	GetTruthValue(){return TruthValue;}
	LetTruthValue(bool NewTruthValue)
		{TruthValue = NewTruthValue;}
}

class PredConst
{
	string Concept = "Predicate Constant";
	string Symbol = "\in";
public:
	GetConcept(){return Concept;}
	GetSymbol(){return Symbol;}
}

class Negation
{
	string Concept = "Negation";
	string Symbol = "\neg";
public:
	GetConcept(){return Concept;}
	GetSymbol(){return Symbol;}
	Predicate Negation(Predicate &psi)
	{
		Predicate neg_psi;
		neg_psi.LetSymbol
			(Symbol + " " + psi.GetSymbol());
		neg_psi.LetTruthValue
			(!psi.TruthValue);
		return neg_psi;
	}
}

class Disjunction
{
	string Concept = "Disjunction";
	string Symbol = "\vee";
public:
	GetConcept(){return Concept;}
	GetSymbol(){return Symbol;}
	Predicate Disjunction
		(Predicate &psi, Predicate &varphi)
	{
		Predicate psi_vee_varphi;
		psi_vee_varphi.LetSymbol
			(psi.GetSymbol() + " " + Symbol
				+ " " + varphi.GetSymbol());
		psi_vee_varphi.LetTruthValue
			(psi.GetTruthValue() || 
				varphi.GetTruthValue());
		return psi_vee_varphi;
	}
}

class Conjunction
{
	string Concept = "Conjunction";
	string Symbol = "\wedge";
public:
	GetConcept(){return Concept;}
	GetSymbol(){return Symbol;}
	Predicate Conjunction
		(Predicate &psi, Predicate &varphi)
	{
		Predicate psi_wedge_varphi;
		psi_wedge_varphi.LetSymbol
			(psi.GetSymbol() + " " + Symbol
				+ " " + varphi.GetSymbol);
		psi_wedge_varphi.LetTruthValue
			(psi.GetTruthValue() &&
				varphi.GetTruthValue());
		return psi_wedge_varphi;
	}
}

class Implication
{
	string Concept = "Implication";
	string Symbol = "\rightarrow";
public:
	GetConcept(){return Concept;}
	GetSymbol(){return Symbol;}
	Predicate Implication
		(Predicate &psi, Predicate &varphi)
	{
		Predicate psi_rightarrow_varphi;
		psi_rightarrow_varphi.LetSymbol
			(psi.GetSymbol() + " " + Symbol
				+ " " + varphi.GetSymbol());
		psi_rightarrow_varphi.LetTruthValue
			(!psi.GetTruthValue() || 
				varphi.GetTruthValue());
		return psi_rightarrow_varphi;
	}
}

class Inference
{
	string Concept = "Inference";
	string Symbol = "\Rightarrow";
public:
	GetConcept(){return Concept;}
	GetSymbol(){return Symbol;}
	Predicate Inference
		(Predicate &psi, Predicate &varphi)
	{
		Predicate psi_Rightarrow_varphi;
		psi_Rightarrow_varphi.LetSymbol
			(psi.GetSymbol() + " " + Symbol
				+ " " + varphi.GetSymbol());
		psi_Rightarrow_varphi.LetTruthValue
			(true);
		if (psi.GetTruthValue()==true && 
			varphi.GetTruthValue==false)
			{cout<<"Inference Error!"}
		return psi_rightarrow_varphi;
	}
}

class Definition
{
private:
	string defname;
protected:
	string get_defname()
	{
		return defname;
	}
}

#endif

/* end of file */