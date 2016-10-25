/**************************************

	Main Test File
	Compile with
		g++ -w main.cpp -std=c++11
	Successful compilation provides
	  validity confirmation

**************************************/

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#include <iostream>
#include <cstring>
#include <string>
#include <memory>

using namespace std;

// initialization file
#include "Initialization/symbol.hh"
#include "Initialization/initio.hh"
#include "Initialization/logic.hh"
#include "Initialization/standard.hh"

// import math terms
#include "UnivMath/term.hh"

// Set Theory
#include "SetTheory/config.cc"

// Smart UMS
#include "SmartUMS/config.cc"

void Test_Initialization_Symbol_Symbol()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Symbol"<<endl;
	Symbol Sym;
	cout<<Sym.GetConcept()<<"  "
		<<Sym.GetSymbolSet()<<endl;
	cout<<endl;
}

void Test_Initialization_Initio_IndepVar()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of IndepVar"<<endl;
	string TestString = "Being Represented";
	cout<<"  Original Settings"<<endl<<"    ";
	IndepVar* TestIndepVar = new IndepVar;
	string *TempRpsnt = static_cast<string*>(TestIndepVar->GetRpsnt());
	cout<<TestIndepVar->GetConcept()<<"  "
		<<TestIndepVar->GetSymbol()<<"  "
		<<*TempRpsnt<<endl;
	cout<<endl<<" Modified Settings"<<endl<<"    ";
	TestIndepVar->LetSymbol("\\varphi");
	TestIndepVar->LetRpsnt(&TestString);
	TempRpsnt = static_cast<string*>(TestIndepVar->GetRpsnt());
	cout<<TestIndepVar->GetConcept()<<"  "
		<<TestIndepVar->GetSymbol()<<"  "
		<<*TempRpsnt<<endl;
	cout<<endl;
	delete TestIndepVar;
}

void Test_Initialization_Initio_Predicate()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Predicate"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Predicate *TestPredicate = new Predicate;
	cout<<TestPredicate->GetConcept()<<"  "
		<<TestPredicate->GetSymbol()<<"  "
		<<TestPredicate->GetTruthValue()<<endl;
	cout<<endl<<"  Modified Settings"<<endl<<"    ";
	TestPredicate->LetSymbol("\\varphi");
	TestPredicate->LetTruthValue(true);
	cout<<TestPredicate->GetConcept()<<"  "
		<<TestPredicate->GetSymbol()<<"  "
		<<TestPredicate->GetTruthValue()<<endl;
	cout<<endl;
	delete TestPredicate;
}

void Test_Initialization_Initio_Class()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Class"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Class *TestClass = new Class;
	Predicate *TestPredicate = new Predicate;
	TestPredicate->LetSymbol("\\lambda");
	IndepVar *TestIndepVar = new IndepVar;
	TestIndepVar->LetSymbol("y");
	cout<<TestClass->GetConcept()<<"  "
		<<TestClass->GetSymbol()<<"  "
		<<TestClass->GetObject()->GetSymbol()<<"  "
		<<TestClass->GetProperty()->GetSymbol()<<endl;
	cout<<"    ";
	cout<<TestClass->ClassForm().GetSymbol()<<"  "
		<<TestClass->ClassForm().GetTruthValue()<<endl;
	cout<<endl<<"  Modified Settings"<<endl<<"    ";
	TestClass->LetSymbol("A");
	TestClass->LetObject(TestIndepVar);
	TestClass->LetProperty(TestPredicate);
	cout<<TestClass->GetConcept()<<"  "
		<<TestClass->GetSymbol()<<"  "
		<<TestClass->GetObject()->GetSymbol()<<"  "
		<<TestClass->GetProperty()->GetSymbol()<<endl;
		cout<<"    ";
	cout<<TestClass->ClassForm().GetSymbol()<<"  "
		<<TestClass->ClassForm().GetTruthValue()<<endl;
	cout<<endl;
	delete TestClass;
}

void Test_Initialization_Initio_Object()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Object"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Object *TestObject = new Object;
	Class *TestClass = new Class;
	TestClass->LetSymbol("X");
	TestClass->GetProperty()->LetSymbol("\\lambda");
	cout<<TestObject->GetConcept()<<"  "
		<<TestObject->GetSymbol()<<endl;
	cout<<"    ";
	cout<<TestObject->GetClass()->ClassForm().GetSymbol()<<endl;
	cout<<endl<<"  Modified Settings"<<endl<<"    ";
	TestObject->LetSymbol("a");
	TestObject->LetClass(TestClass);
	cout<<TestObject->GetConcept()<<"  "
		<<TestObject->GetSymbol()<<endl;
	cout<<"    ";
	cout<<TestObject->GetClass()->ClassForm().GetSymbol()<<endl;
	cout<<endl;
	delete TestObject;
}

void Test_Initialization_Initio_BelongTo()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of BelongTo"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	BelongTo in;
	cout<<in.GetConcept()<<"  "
		<<in.GetSymbol()<<endl;
	cout<<endl;
}

void Test_Initialization_Logic_UnivQuan()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of UnivQuan"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	UnivQuan forall;
	IndepVar* TestIndepVar = new IndepVar;
	Predicate *TestPredicate = new Predicate;
	cout<<forall.GetConcept()<<"  "
		<<forall.GetSymbol()<<"  "
		<<forall.GetDefSymbol()<<endl;
	cout<<"    ";
	cout<<forall.OpUnivQuan(TestIndepVar, TestPredicate).GetSymbol()<<"  "
		<<forall.OpUnivQuan(TestIndepVar, TestPredicate).GetTruthValue()<<endl;
	delete TestIndepVar; delete TestPredicate;
	cout<<endl;
}

void Test_Initialization_Logic_ExistQuan()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of ExistQuan"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	ExistQuan exists;
	IndepVar* TestIndepVar = new IndepVar;
	Predicate *TestPredicate = new Predicate;
	cout<<exists.GetConcept()<<"  "
		<<exists.GetSymbol()<<"  "
		<<exists.GetDefSymbol()<<endl;
	cout<<"    ";
	cout<<exists.OpExistQuan(TestIndepVar, TestPredicate).GetSymbol()<<"  "
		<<exists.OpExistQuan(TestIndepVar, TestPredicate).GetTruthValue()<<endl;
	delete TestIndepVar; delete TestPredicate;
	cout<<endl;
}

void Test_Initialization_Logic_Negation()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Negation"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Negation neg;
	Predicate *TestPredicate = new Predicate;
	cout<<neg.GetConcept()<<"  "
		<<neg.GetSymbol()<<"  "
		<<neg.GetDefSymbol()<<endl;
	cout<<"    ";
	cout<<neg.OpNegation(*TestPredicate).GetSymbol()<<"  "
		<<neg.OpNegation(*TestPredicate).GetTruthValue()<<endl;
	delete TestPredicate;
	cout<<endl;
}

void Test_Initialization_Logic_Disjunction()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Disjunction"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Disjunction vee;
	Predicate *TestPredicateLeft = new Predicate;
	Predicate *TestPredicateRght = new Predicate;
	TestPredicateRght->LetTruthValue(true);
	cout<<vee.GetConcept()<<"  "
		<<vee.GetSymbol()<<"  "
		<<vee.GetDefSymbol()<<endl;
	cout<<"    ";
	cout<<vee.OpDisjunction(*TestPredicateLeft, *TestPredicateRght)
				.GetSymbol()<<"  "
		<<vee.OpDisjunction(*TestPredicateLeft, *TestPredicateRght)
				.GetTruthValue()<<endl;
	delete TestPredicateLeft; delete TestPredicateRght;
	cout<<endl;
}

void Test_Initialization_Logic_Conjunction()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Conjunction"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Conjunction wedge;
	Predicate *TestPredicateLeft = new Predicate;
	Predicate *TestPredicateRght = new Predicate;
	TestPredicateRght->LetTruthValue(true);
	cout<<wedge.GetConcept()<<"  "
		<<wedge.GetSymbol()<<"  "
		<<wedge.GetDefSymbol()<<endl;
	cout<<"    ";
	cout<<wedge.OpConjunction(*TestPredicateLeft, *TestPredicateRght)
				.GetSymbol()<<"  "
		<<wedge.OpConjunction(*TestPredicateLeft, *TestPredicateRght)
				.GetTruthValue()<<endl;
	delete TestPredicateLeft; delete TestPredicateRght;
	cout<<endl;
}

void Test_Initialization_Logic_Implication()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Implication"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Implication rghtarr;
	Predicate *TestPredicateLeft = new Predicate;
	Predicate *TestPredicateRght = new Predicate;
	TestPredicateRght->LetTruthValue(true);
	cout<<rghtarr.GetConcept()<<"  "
		<<rghtarr.GetSymbol()<<"  "
		<<rghtarr.GetDefSymbol()<<endl;
	cout<<"    ";
	cout<<rghtarr.OpImplication(*TestPredicateLeft, *TestPredicateRght)
				.GetSymbol()<<"  "
		<<rghtarr.OpImplication(*TestPredicateLeft, *TestPredicateRght)
				.GetTruthValue()<<endl;
	delete TestPredicateLeft; delete TestPredicateRght;
	cout<<endl;
}

void Test_Initialization_Logic_Inference()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Inference"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Inference RghtArr;
	Predicate *TestPredicateLeft = new Predicate;
	Predicate *TestPredicateRght = new Predicate;
	TestPredicateRght->LetTruthValue(true);
	cout<<RghtArr.GetConcept()<<"  "
		<<RghtArr.GetSymbol()<<"  "
		<<RghtArr.GetDefSymbol()<<endl;
	cout<<"    ";
	cout<<RghtArr.OpInference(*TestPredicateLeft, *TestPredicateRght)
				.GetSymbol()<<"  "
		<<RghtArr.OpInference(*TestPredicateLeft, *TestPredicateRght)
				.GetTruthValue()<<endl;
	delete TestPredicateLeft; delete TestPredicateRght;
	cout<<endl;
}

void Test_SetTheory_Support_Subclass()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Subclass"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Subclass *TestSubclass = new Subclass;
	Class *TestFatherClass = new Class;
	TestSubclass->LetClass(*TestFatherClass);
	cout<<"    "<<TestSubclass->GetDefinition()<<endl;
	cout<<"    "<<TestSubclass->Formulation().GetSymbol()<<"  "
		<<TestSubclass->Formulation().GetTruthValue()<<endl;
	delete TestSubclass; delete TestFatherClass;
	cout<<endl;
}

void Test_SetTheory_Basic_Set()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Set"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Set *TestSet = new Set;
	IndepVar *TestElement = new IndepVar;
	TestElement->LetSymbol("a");
	Predicate *TestPredicate = new Predicate;
	TestPredicate->LetSymbol("\\lambda");
	cout<<TestSet->GetBase()<<"  "
		<<TestSet->GetDefinition()<<" "
		<<TestSet->GetSetSymbol()<<"  "
		<<TestSet->GetDefSymbol()<<"  "
		<<TestSet->GetSmartElement()->GetSymbol()<<"  "
		<<TestSet->GetSmartProperty()->GetSymbol()<<" "
		<<TestSet->GetStatus()->GetSymbol()<<"  "
		<<TestSet->GetStatus()->GetTruthValue()<<endl<<"    "
		<<TestSet->Formulation().GetSymbol()<<"  "
		<<TestSet->Formulation().GetTruthValue()<<endl;
	cout<<endl<<"  Modified Settings"<<endl<<"    ";
	TestSet->LetSetSymbol("A"); TestSet->LetDefSymbol("Def");
	TestSet->LetSetProp(TestPredicate);
	TestSet->LetElement(TestElement);
	cout<<TestSet->GetSetSymbol()<<"  "
		<<TestSet->GetDefSymbol()<<"  "
		<<TestSet->GetSmartElement()->GetSymbol()<<"  "
		<<TestSet->GetSmartProperty()->GetSymbol()<<" "
		<<TestSet->GetStatus()->GetSymbol()<<"  "
		<<TestSet->GetStatus()->GetTruthValue()<<endl<<"    "
		<<TestSet->Formulation().GetSymbol()<<"  "
		<<TestSet->Formulation().GetTruthValue()<<endl;
	delete TestSet;
	cout<<endl;
}

void Test_SetTheory_Basic_Element()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Element"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Element *TestElement = new Element;
	Set *TestSet = new Set;
	TestSet->LetSetSymbol("S");
	TestSet->GetSetProp()->LetSymbol("\\lambda");
	cout<<TestElement->GetDefinition()<<"  "
		<<TestElement->GetSymbol()<<endl;
	cout<<"    ";
	cout<<TestElement->GetSet()->Formulation().GetSymbol()<<endl;
	cout<<endl<<"  Modified Settings"<<endl<<"    ";
	TestElement->LetSymbol("a");
	TestElement->LetSet(TestSet);
	cout<<TestElement->GetDefinition()<<"  "
		<<TestElement->GetSymbol()<<endl;
	cout<<"    ";
	cout<<TestElement->GetSet()->Formulation().GetSymbol()<<endl;
	cout<<endl;
	delete TestElement;
}

void Test_SetTheory_Basic_SetBelongTo()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of SetBelongTo"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	SetBelongTo in;
	cout<<in.GetOperation()<<"  "
		<<in.GetDefSymbol()<<"  "
		<<in.GetProperty()<<endl;
	cout<<endl;
}

void Test_SetTheory_Basic_SetContain()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of SetContain"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	SetContain subset;
	Set *TempSetLeft = new Set;
	Set *TempSetRght = new Set;
	TempSetRght->LetSetSymbol("Y");
	cout<<subset.GetOperation()<<"  "
		<<subset.GetSymbol()<<"  "
		<<subset.GetProperty()<<endl;
	cout<<SetContain::OpForm(TempSetLeft, TempSetRght).GetSymbol()<<"  "
		<<SetContain::OpForm(TempSetLeft, TempSetRght).GetTruthValue()<<endl;
	delete TempSetLeft; delete TempSetRght;
	cout<<endl;
}

void Test_SetTheory_Basic_Subset()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Subset"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Subset *TestSubset = new Subset;
	Set *TestFatherSet = new Set;
	TestFatherSet->LetSetSymbol("E");
	TestSubset->LetSet(TestFatherSet);
	cout<<"    "<<TestSubset->GetDefinition()<<endl;
	cout<<"    "<<TestSubset->Formulation().GetSymbol()<<"  "
		<<TestSubset->Formulation().GetTruthValue()<<endl;
	delete TestSubset;
	cout<<endl;
}

void Test_SetTheory_Basic_SetEqual()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of SetEqual"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	SetEqual subset;
	Set *TempSetLeft = new Set;
	Set *TempSetRght = new Set;
	TempSetRght->LetSetSymbol("Y");
	cout<<subset.GetOperation()<<"  "
		<<subset.GetSymbol()<<"  "
		<<subset.GetProperty()<<endl;
	cout<<SetEqual::OpForm(TempSetLeft, TempSetRght).GetSymbol()<<"  "
		<<SetEqual::OpForm(TempSetLeft, TempSetRght).GetTruthValue()<<endl;
	cout<<SetEqual::OpForm(TempSetLeft, TempSetLeft).GetSymbol()<<"  "
		<<SetEqual::OpForm(TempSetLeft, TempSetLeft).GetTruthValue()<<endl;
	delete TempSetLeft; delete TempSetRght;
	cout<<endl;
}

void Test_SetTheory_Basic_EmptySet()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of EmptySet"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	EmptySet *TestEmptySet = new EmptySet;
	cout<<"    "<<TestEmptySet->GetDefinition()<<endl;
	cout<<"    "<<TestEmptySet->Formulation().GetSymbol()<<"  "
		<<TestEmptySet->Formulation().GetTruthValue()<<endl;
	delete TestEmptySet;
	cout<<endl;
}

void Test_SetTheory_Russell_Russell()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of Russell Class"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	Russell *TestRussell = new Russell;
	cout<<"    "<<TestRussell->GetDefinition()<<endl;
	cout<<"    "<<TestRussell->Formulation().GetSymbol()<<"  "
		<<TestRussell->Formulation().GetTruthValue()<<endl;
	delete TestRussell;
	cout<<endl;
}

void Test_SmartUMS_SmartSet_SmartSet()
{
	cout<<"------------------------------"<<endl;
	cout<<"Test of SmartSet"<<endl;
	cout<<"  Original Settings"<<endl<<"    ";
	SmartSet *TestSmartSetA = new SmartSet;
	shared_ptr<PredicateForSet> newprop(new PredicateForSet);
	newprop->LetSymbol("\\lambda"); newprop->LetSet(TestSmartSetA);
	TestSmartSetA->LetSmartProp(newprop);
	TestSmartSetA->GetSmartElmnt()->LetSymbol("y");
	cout<<"    "<<TestSmartSetA->GetDefinition()<<endl;
	cout<<"    "<<TestSmartSetA->Formulation().GetSymbol()<<"  "
		<<TestSmartSetA->Formulation().GetTruthValue()<<endl;
	SmartSet TestSmartSetB(*TestSmartSetA);
	shared_ptr<IndepVar> newelmnt(new IndepVar);
	newelmnt->LetSymbol("\\gamma");
	TestSmartSetB.LetSmartElmnt(newelmnt);
	cout<<"    "<<TestSmartSetB.Formulation().GetSymbol()<<"  "
		<<TestSmartSetB.Formulation().GetTruthValue()<<endl;
	SmartSet TestSmartSetC = TestSmartSetB;
	cout<<"    "<<TestSmartSetC.Formulation().GetSymbol()<<"  "
		<<TestSmartSetC.Formulation().GetTruthValue()<<endl;
	delete TestSmartSetA;
	cout<<endl;
}

// main test function
int main(void)
{
	// print guidance
	cout<<"This is the test file of Universal Mathematics System"<<endl
		<<"Copyright (C) 2016 Zhang Chang-kai"<<endl
		<<"Contact via: phy.zhangck@gmail.com"<<endl
		<<"General Public License version 3.0"<<endl;
	cout<<endl<<"    Test Begin"<<endl<<endl;
	// test from initialization/symbol
	Test_Initialization_Symbol_Symbol();
	// test from initialization/initio
	Test_Initialization_Initio_IndepVar();
	Test_Initialization_Initio_Predicate();
	Test_Initialization_Initio_Class();
	Test_Initialization_Initio_Object();
	Test_Initialization_Initio_BelongTo();
	// test from initialization/logic
	Test_Initialization_Logic_UnivQuan();
	Test_Initialization_Logic_ExistQuan();
	Test_Initialization_Logic_Negation();
	Test_Initialization_Logic_Disjunction();
	Test_Initialization_Logic_Conjunction();
	Test_Initialization_Logic_Implication();
	Test_Initialization_Logic_Inference();
	// test from settheory/support
	Test_SetTheory_Support_Subclass();
	// test form settheory/basic
	Test_SetTheory_Basic_Set();
	Test_SetTheory_Basic_Element();
	Test_SetTheory_Basic_SetBelongTo();
	Test_SetTheory_Basic_SetContain();
	Test_SetTheory_Basic_Subset();
	Test_SetTheory_Basic_SetEqual();
	Test_SetTheory_Basic_EmptySet();
	// test from settheory/Russell
	Test_SetTheory_Russell_Russell();
	// test from smartums/smartset
	Test_SmartUMS_SmartSet_SmartSet();
	cout<<"------------------------------";
	cout<<endl<<"    Test End"<<endl<<endl;
	cout<<"Compile Success"<<endl;
	return 0;
}
