/**************************************

	Main Compilation File
	Compile with
		g++ -w main.cpp -std=c++11
	Successful compilation provides
	  validity confirmation

**************************************/

#include <iostream>

using namespace std;

// initialization file
#include "Initialization/symbol.h"
#include "Initialization/initio.h"
#include "Initialization/logic.h"
#include "Initialization/standard.h"

// import math terms
#include "UnivMath/term.h"

// Set Theory
#include "SetTheory/config.cc"

// Smart UMS
#include "SmartUMS/config.cc"

// main test function
int main(void)
{
	SmartSet A;
	shared_ptr<PredicateForSet> newprop(new PredicateForSet);
	newprop->LetSymbol("\\lambda"); newprop->LetSet(&A);
	A.LetSmartProp(newprop); A.GetSmartElmnt()->LetSymbol("z");
	SmartSet B(A);
	SmartSet C = A;
	cout<<A.Formulation().GetSymbol()<<endl;
	cout<<B.Formulation().GetSymbol()<<endl;
	cout<<C.Formulation().GetSymbol()<<endl;
	Class D;
	D.GetObject()->LetSymbol("y");
	cout<<D.ClassForm().GetSymbol()<<endl;
	cout<<"Compile Success"<<endl;
	return 0;
}