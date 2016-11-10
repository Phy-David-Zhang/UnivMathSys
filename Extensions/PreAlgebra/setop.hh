/* Operation of Set */

#ifndef Extensions_PreAlgebra_SetOp_h
#define Extensions_PreAlgebra_SetOp_h

#include <cstring>
#include <string>

#include "Extensions/General/classic.hh"

using std::string;

// define property of union set
class PredicateForUnion: public Predicate
{
	Set *Left, *Rght;
public:
	PredicateForUnion(Set *NewLeft, Set *NewRght);
	bool Condition(IndepVar *Input);
};

class Union: virtual public MathOp
{
public:
	Union();
	string GetDefSymbol(){return GetSymbol();}
	Predicate OpUnion(Set *Left, Set *Rght);
	Set* UnionOf(Set *Left, Set *Rght);
};

class PredicateForIntersection: public Predicate
{
	Set *Left, *Rght;
public:
	PredicateForIntersection(Set *NewLeft, Set *NewRght);
	bool Condition(IndepVar *Input);
};

class Intersection: virtual public MathOp
{
public:
	Intersection();
	string GetDefSymbol(){return GetSymbol();}
	Predicate OpIntersection(Set *Left, Set *Rght);
	Set* IntersectionOf(Set *Left, Set *Rght);
};

class PredicateForComplement: public Predicate
{
	Set *Univ, *Target;
public:
	PredicateForComplement(Set *NewUniv, Set *NewTarget);
	bool Condition(IndepVar *Input);
};

class Complement: virtual public MathOp
{
public:
	Complement();
	string GetDefSymbol(){return GetSymbol();}
	Predicate OpComplement(Set *Left, Set *Rght);
	Set* ComplementOf(Set *Left, Set *Rght);
};

#endif

/* end of file */
