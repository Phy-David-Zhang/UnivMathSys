
# Makefile of Universal Mathematics System

# Copyright (C) 2016 Zhang Chang-kai\
# Contact via: phy.zhangck@gmail.com\
# General Public License version 3.0

python = python3
cmps = zip
target = UnivMathSys-Python.zip
pack = Package

msrc = Technology

top = TopModuleInit
sub = SubModuleInit

stat = __main__.py
init = __init__.py

main = main.py
test = test.py
link = link.py

sdir = Elementary\
 	   Foundation\
	   Structure\
	   Technology

initfile = $(foreach dir, $(sdir),\
		   $(dir)/$(init))

default:
	@echo Building Directory Tree
	@for dir in $(sdir); do\
		cp $(msrc)/$(sub)/$$dir.$(init) $$dir;\
		mv $$dir/$$dir.$(init) $$dir/$(init);\
		done
	@cp $(msrc)/$(top)/$(stat) $(stat)
	@cp $(msrc)/$(top)/$(init) $(init)
	@echo Generating Package
	@$(cmps) -qr $(pack)/$(target) $(sdir)
	@$(cmps) -q $(pack)/$(target) $(stat) $(init)
	@$(cmps) -q $(pack)/$(target) $(msrc)/$(main)\
				$(msrc)/$(test) $(msrc)/$(link)
	@echo Cleaning Directory
	@rm -rf $(initfile)
	@rm -rf $(stat) $(init)
	@echo Package Generation Completed

testrun:
	@echo Running Tests
	@$(python) $(pack)/$(target) test
