/* Initialization of Universal Mathematics System. */

#ifndef Initialization
#define Initialization

#include <cstring>
#include <string>
#include <iostream>

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
	// get info
	void LetTruthValue(bool NewTruthValue)
		{TruthValue = NewTruthValue;}
	// condition
	virtual bool Condition(Predicate &Input)
		{return false;}
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
};

class UnivQuan
{
	// information
	string Concept = "for all";
	string Symbol = "\forall";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// operation
	Predicate OpUnivQuan(Predicate &Input,
		Predicate &psi)
	{
		Predicate univ_psi;
		univ_psi.LetSymbol
			(Symbol + " " + Input.GetSymbol()
				+ " \," + psi.GetSymbol());
		univ_psi.LetTruthValue
			(psi.Condition(Input));
		return univ_psi;
	}
};

class UnivQuan
{
	// information
	string Concept = "for all";
	string Symbol = "\forall";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// operation
	Predicate OpUnivQuan(Predicate &Input,
		Predicate &psi)
	{
		Predicate univ_psi;
		univ_psi.LetSymbol
			(Symbol + " " + Input.GetSymbol()
				+ " \," + psi.GetSymbol());
		univ_psi.LetTruthValue
			(psi.Condition(Input));
		return univ_psi;
	}
};

// Operation Nagation
class Negation
{
	// information
	string Concept = "Negation";
	string Symbol = "\neg";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// operation
	Predicate OpNegation(Predicate &psi)
	{
		Predicate neg_psi;
		neg_psi.LetSymbol
			(Symbol + " " + psi.GetSymbol());
		neg_psi.LetTruthValue
			(!psi.GetTruthValue());
		return neg_psi;
	}
};

// Operation Disjunction
class Disjunction
{
	// information
	string Concept = "Disjunction";
	string Symbol = "\vee";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// operation
	Predicate OpDisjunction
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
};

class Conjunction
{
	// information
	string Concept = "Conjunction";
	string Symbol = "\wedge";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// operation
	Predicate OpConjunction
		(Predicate &psi, Predicate &varphi)
	{
		Predicate psi_wedge_varphi;
		psi_wedge_varphi.LetSymbol
			(psi.GetSymbol() + " " + Symbol
				+ " " + varphi.GetSymbol());
		psi_wedge_varphi.LetTruthValue
			(psi.GetTruthValue() &&
				varphi.GetTruthValue());
		return psi_wedge_varphi;
	}
};

class Implication
{
	// information
	string Concept = "Implication";
	string Symbol = "\rightarrow";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// operation
	Predicate OpImplication
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
};

class Inference
{
	// information
	string Concept = "Inference";
	string Symbol = "\Rightarrow";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// operation
	Predicate OpInference
		(Predicate &psi, Predicate &varphi)
	{
		Predicate psi_Rightarrow_varphi;
		psi_Rightarrow_varphi.LetSymbol
			(psi.GetSymbol() + " " + Symbol
				+ " " + varphi.GetSymbol());
		psi_Rightarrow_varphi.LetTruthValue
			(true);
		if (psi.GetTruthValue()==true && 
			varphi.GetTruthValue()==false)
			{cout<<"Inference Error!"<<endl;}
		return psi_Rightarrow_varphi;
	}
};

class Definition
{
private:
	string defname;
protected:
	string get_defname()
	{
		return defname;
	}
};

#endif

/* end of file */