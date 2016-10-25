/**************************************

	Main Compilation File
	Compile with
		g++ -w main.cpp -std=c++11
	Successful compilation provides
	  validity confirmation

**************************************/

	/* Copyright (C) 2016 Zhang Chang-kai */
	/* Contact via: phy.zhangck@gmail.com */
	/* General Public License version 3.0 */

#include <iostream>

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

// main test function
int main(void)
{
	cout<<"Compile Success"<<endl;
	return 0;
}