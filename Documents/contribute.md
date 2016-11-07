<!-- Contribution Guideline for UnivMathSys -->

  <!-- Copyright (C) 2016 Zhang Chang-kai -->
  <!-- Contact via: phy.zhangck@gmail.com -->
  <!-- CC-BY-SA 4.0 International License -->

## How to Contribute

This is the guideline for public collaboration of Universal Mathematics System.

#### Structure of Universal Mathematics System

The Universal Mathematics System has eight basic directory, with *UnivMath* containing entrance, *Initialization* and *SetTheory* containing basic mathematical concepts up to fundamental set theory, *Features* containing advanced functions, *Documents* and *Package* providing supports as well as *Extension* and *Library* containing extended functions of the system.

#### Maintenance of Kernel and Extension

The project Universal Mathematics System is divided into a kernel and numerous extensions. Term *extension* refers to any data in directory *Extension* and *Library*, and term *kernel* refers to the rest data.

The original author, Zhang Chang-kai, is and will be the only copyright holder and maintainer of the kernel of Universal Mathematics System. Contribution may be suggested, but modification can only be made by the general maintainer, Zhang Chang-kai, only.

#### Public Contribution and Responsibility

Contributions can be made through pull request. Please note that contributions on kernel files will not be accepted according to terms in the above section.

By default, the author of an extension file will be the maintainer of this file. The maintainer has the responsibility to respond to any related issues raised. The general maintainer has the right to cancel the maintainer identity of certain contributor if irresponsible conducts are found.

#### Guideline of Extension and Coding Style

An extension file of Universal Mathematics System should contain the following blocks to work: appropriate description of the file and copyright claim, full header files of the kernel, and a clear end of file comment. A complete extension should have at least a .hh header file and a .cc implementation file, and dependencies should be clearly stated if it is based not only on the kernel.

**In case of overlap work, contributors are strongly recommended to contact the general maintainer before start of any contributions.**

Generally, the project follows the Google C++ Style Guide. Follow the existed code for other styles not suggested.

#### Updates of This Guideline

The general maintainer may apply changes to this guideline, and not all contributors will be notified in time. Thus, contributors are suggested to keep an eye on the updates of the guideline to follow the latest terms. The general maintainer reserves the right of final explanation of this guideline.
