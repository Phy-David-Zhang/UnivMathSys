/* Basic mathematical logic */

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#ifndef Initialization_Logic_h
#define Initialization_Logic_h

#include <cstring>
#include <string>
#include <iostream>

using std::string;
using std::cout;

// Universal Quantification
class UnivQuan
{
	// information
	string Concept = "for all";
	string Symbol = "\\forall";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get symbol
	static string GetDefSymbol()
		{return SymUnivQuan;}
	// operation
	static Predicate OpUnivQuan(IndepVar *Input,
		Predicate *psi)
	{
		Predicate univ_psi;
		univ_psi.LetSymbol
			(SymUnivQuan + " " + Input->GetSymbol()
				+ " \\," + psi->GetSymbol());
		univ_psi.LetTruthValue
			(psi->Condition(Input));
		return univ_psi;
	}
};

// Existential Quantification
class ExistQuan
{
	// information
	string Concept = "there exists";
	string Symbol = "\\exists";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get symbol
	static string GetDefSymbol()
		{return SymExistQuan;}
	// operation
	static Predicate OpExistQuan(IndepVar *Input,
		Predicate *psi)
	{
		Predicate exist_psi;
		psi->LetTruthValue
			(!psi->GetTruthValue());
		exist_psi.LetSymbol
			(SymExistQuan + " " + Input->GetSymbol()
				+ " \\," + psi->GetSymbol());
		exist_psi.LetTruthValue
			(!psi->Condition(Input));
		return exist_psi;
	}
};

// Operation Nagation
class Negation
{
	// information
	string Concept = "Negation";
	string Symbol = "\\neg";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get symbol
	static string GetDefSymbol()
		{return SymNegation;}
	// operation
	static Predicate OpNegation(Predicate &psi)
	{
		Predicate neg_psi;
		neg_psi.LetSymbol
			(SymNegation + " " + psi.GetSymbol());
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
	string Symbol = "\\vee";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get symbol
	static string GetDefSymbol()
		{return SymDisjunction;}
	// operation
	static Predicate OpDisjunction(Predicate &psi, 
		Predicate &varphi)
	{
		Predicate psi_vee_varphi;
		psi_vee_varphi.LetSymbol
			(psi.GetSymbol() + " " + SymDisjunction
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
	string Symbol = "\\wedge";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get symbol
	static string GetDefSymbol()
		{return SymConjunction;}
	// operation
	static Predicate OpConjunction(Predicate &psi, 
		Predicate &varphi)
	{
		Predicate psi_wedge_varphi;
		psi_wedge_varphi.LetSymbol
			(psi.GetSymbol() + " " + SymConjunction
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
	string Symbol = "\\rightarrow";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get symbol
	static string GetDefSymbol()
		{return SymImplication;}
	// operation
	static Predicate OpImplication(Predicate &psi, 
		Predicate &varphi)
	{
		Predicate psi_rightarrow_varphi;
		psi_rightarrow_varphi.LetSymbol
			(psi.GetSymbol() + " " + SymImplication
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
	string Symbol = "\\Rightarrow";
	// methods
public:
	// get info
	string GetConcept(){return Concept;}
	string GetSymbol(){return Symbol;}
	// get symbol
	static string GetDefSymbol()
		{return SymInference;}
	// operation
	static Predicate OpInference(Predicate &psi, 
		Predicate &varphi)
	{
		Predicate psi_Rightarrow_varphi;
		psi_Rightarrow_varphi.LetSymbol
			(psi.GetSymbol() + " " + SymInference
				+ " " + varphi.GetSymbol());
		psi_Rightarrow_varphi.LetTruthValue
			(!psi.GetTruthValue() || 
				varphi.GetTruthValue());
		if (psi.GetTruthValue()==true && 
			varphi.GetTruthValue()==false)
				{cout<<"Inference Error!"<<endl;}
		return psi_Rightarrow_varphi;
	}
};

#endif

/* end of file */