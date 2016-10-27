# Makefile of Universal Mathematics System

# Copyright (C) 2016 Zhang Chang-kai\
# Contact via: phy.zhangck@gmail.com\
# General Public License version 3.0

cc = g++
prom = UnivMathSys
src = UnivMath/main.cc
cflags = -I.
std = -std=c++11

UnivMathSys_Default: 
	$(cc) -o $(prom) -w $(src) -I. $(std)
