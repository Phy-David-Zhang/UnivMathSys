/* Operations of Set */

#include <cstring>
#include <string>

#include "Extensions/PreAlgebra/setop.hh"

using std::string;

// symbol of union
static const string SymUnion = "\\cup";
static const string SymIntersection = "\\cap";
static const string SymComplement = "\\complement";

/* Predicate for Union */

// constructor
PredicateForUnion::PredicateForUnion(Set *NewLeft, Set *NewRght)
    {Left = NewLeft; Rght = NewRght;}

// condition
bool PredicateForUnion::Condition(IndepVar *Input)
{
    Predicate LeftArg
        = SetBelongTo::OpBelongTo(Input, Left);
    Predicate RghtArg
        = SetBelongTo::OpBelongTo(Input, Rght);
    return Disjunction::OpDisjunction(
        LeftArg, RghtArg).GetTruthValue();
}

/* Operation Union */

// constructor
Union::Union()
    {MathOp::Operation = "union";
        MathOp::Symbol = "\\cup";}

// union of set
Set* UnionOf(Set *Left, Set *Rght)
{
    PredicateForUnion *TempProp
        = new PredicateForUnion(Left, Rght);
    Set *UnionSet = new Set;
    UnionSet->LetSetProp(TempProp);
    return UnionSet;
}

// union form
Predicate Union::OpUnion(Set *Left, Set *Rght)
{
    Predicate union_of_set;
    union_of_set.LetSymbol(Left->GetSetSymbol() +
        SymUnion + Rght->GetSetSymbol());
    union_of_set.LetTruthValue(true);
    return union_of_set;
}

/* Predicate for Intersection */

// constructor
PredicateForIntersection::PredicateForIntersection(Set *NewLeft, Set *NewRght)
    {Left = NewLeft; Rght = NewRght;}

// condition
bool PredicateForIntersection::Condition(IndepVar *Input)
{
    Predicate LeftArg
        = SetBelongTo::OpBelongTo(Input, Left);
    Predicate RghtArg
        = SetBelongTo::OpBelongTo(Input, Rght);
    return Conjunction::OpConjunction(
        LeftArg, RghtArg).GetTruthValue();
}

/* Operation Intersection */

// constructor
Intersection::Intersection()
    {MathOp::Operation = "intersection";
        MathOp::Symbol = "\\cup";}

// intersection of set
Set* IntersectionOf(Set *Left, Set *Rght)
{
    PredicateForIntersection *TempProp
        = new PredicateForIntersection(Left, Rght);
    Set *IntersectionSet = new Set;
    IntersectionSet->LetSetProp(TempProp);
    return IntersectionSet;
}

// intersection form
Predicate Intersection::OpIntersection(Set *Left, Set *Rght)
{
    Predicate intersection_of_set;
    intersection_of_set.LetSymbol(Left->GetSetSymbol() +
        SymIntersection + Rght->GetSetSymbol());
    intersection_of_set.LetTruthValue(true);
    return intersection_of_set;
}

/* Predicate for Complement */

// constructor
PredicateForComplement::PredicateForComplement(Set *NewUniv, Set *NewTarget)
    {Univ = NewUniv; Target = NewTarget;}

// condition
bool PredicateForComplement::Condition(IndepVar *Input)
{
    Predicate LeftArg
        = SetBelongTo::OpBelongTo(Input, Univ);
    Predicate RghtArg
        = SetBelongTo::OpBelongTo(Input, Target);
    RghtArg = Negation::OpNegation(RghtArg);
    return Conjunction::OpConjunction(LeftArg,
        RghtArg).GetTruthValue();
}

/* Operation Complement */

// constructor
Complement::Complement()
    {MathOp::Operation = "complement";
        MathOp::Symbol = "\\cup";}

// complement of set
Set* ComplementOf(Set *Univ, Set *Target)
{
    PredicateForComplement *TempProp
        = new PredicateForComplement(Univ, Target);
    Set *ComplementSet = new Set;
    ComplementSet->LetSetProp(TempProp);
    return ComplementSet;
}

// complement form
Predicate Complement::OpComplement(Set *Left, Set *Rght)
{
    Predicate complement_of_set;
    complement_of_set.LetSymbol(Left->GetSetSymbol() +
        SymComplement + Rght->GetSetSymbol());
    complement_of_set.LetTruthValue(true);
    return complement_of_set;
}
