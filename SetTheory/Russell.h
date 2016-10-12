/* This is to test whether the system identifies
   Russell class, which means providing error 
   message when defining Russell class as a set. */

	class PfRussell: public Predicate
	{
		Class *ClassC;
	public:
		PfRussell()
			{ClassC = NULL;}
		void LetClass(Class* NewClass)
			{ClassC = NewClass;}
		bool Condition(IndepVar &Input)
		{
			bool result;
			result = !(Input.GetRpsnt() == 
				ClassC->GetObject().GetRpsnt());
			LetSymbol(Input.GetSymbol() + 
				"\\notin " + ClassC->GetSymbol());
			return result;
		}
	};

class Russell: virtual public MathDef, public Set
{
public:
	Russell(){PropOfSet(); 
		ChkEligibility();}
	void PropOfSet()
	{
		Class *Temp = new Class;
		Temp->LetObject(this->GetObject());
		LetClass(*Temp);
		PfRussell *psifR = new PfRussell;
		psifR->LetClass(GetClass());
		GetClass()->LetProperty(psifR);
	}
	Predicate Formulation()
	{
		Predicate Form;
		Form.LetSymbol("\\{" + 
			GetObject().GetSymbol() + "\\mid " + 
			GetClass()->GetProperty()
				->GetSymbol() + "\\}");
		Form.LetTruthValue(ChkEligibility());
		return Form;
	}
};