# Makefile of Universal Mathematics System

# Copyright (C) 2016 Zhang Chang-kai\
# Contact via: phy.zhangck@gmail.com\
# General Public License version 3.0

mprom = UnivMathSys
msrc = UnivMath/main.cc

tprom = UnivTest
tsrc = UnivMath/test.cc

extdir = Extensions
extname = PreAlgebra

lhdir = $(extdir)/$(extname)/Header
lsdir = $(extdir)/$(extname)/Source
lodir = $(extdir)/$(extname)/Object

obj = $(subst Source,Object,\
      $(patsubst %.cc,%.o,\
	  $(wildcard $(lsdir)/*.cc)))

cc = g++
cflags = -I.
std = -std=c++11

default:
	$(cc) -o $(mprom) -w $(msrc) -I. $(std)

testrun:
	$(cc) -o $(tprom) -w $(tsrc) -I. $(std)

library: $(obj)

$(lodir)/%.o: $(lsdir)/%.cc $(lhdir)/%.hh
	$(cc) -o $@ -c $< -I. $(std)
