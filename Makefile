UnivMathSys_Default: 
	g++ -o UnivMathSys -w UnivMath/main.cc -I. -std=c++11
test:
	g++ -o UnivMathSys -w UnivMath/test.cc -I. -std=c++11
