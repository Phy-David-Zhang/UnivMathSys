# Makefile of Universal Mathematics System

# Copyright (C) 2016 Zhang Chang-kai\
# Contact via: phy.zhangck@gmail.com\
# General Public License version 3.0

mprom = UnivMathSys
mdir = UnivMath/Formal
msrc = $(mdir)/main.cc

tprom = UnivTest
tdir = UnivMath/Test
tsrc = $(tdir)/test.cc

extdir = Extensions
extname = PreAlgebra

libdir = $(foreach dir,$(extname),\
         $(extdir)/$(dir))

libobj = $(patsubst %.cc,%.o,\
		 $(foreach dir,$(libdir),\
         $(wildcard $(dir)/*.cc)))

arcdir = Library
libarc = $(foreach name,$(extname),\
         $(arcdir)/$(name).a)

cc = g++
cflags = -I.
std = -std=c++11

default:
	$(cc) -o $(mprom) -w $(msrc) -I. $(std)

testrun:
	$(cc) -o $(tprom) -w $(tsrc) -I. $(std)

clcprom:
	rm $(mprom) $(tprom)

library: $(libobj) $(libarc)

$(arcdir)/%.a: $(extdir)/%/
	ar rcs $@ $<*.o

$(libobj): %.o: %.cc %.hh
	$(cc) -o $@ -c $< -I. $(std)

clclib:
	rm $(libobj) $(libarc)

# end of makefile
