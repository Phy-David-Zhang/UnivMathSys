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
#include "Initialization/symbol.h"
#include "Initialization/initio.h"
#include "Initialization/logic.h"
#include "Initialization/standard.h"

// import math terms
#include "UnivMath/term.h"

// Set Theory
#include "SetTheory/config.cc"

// main test function
int main(void)
{
	cout<<"Compile Success"<<endl;
	return 0;
}