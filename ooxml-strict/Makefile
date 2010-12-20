RM=rm -rf
PYXB_ROOT=../pyxb
PYTHON=@PYTHONPATH=$(PYXB_ROOT) python
TOUCH=@touch
ECHO=@echo
TMP=tmp

ALL:generate

clean:
	$(RM) dml pml wml sml props

download:
	$(ECHO) "Getting Pyxb"
	if test -d $(PYXB_ROOT) ; then \
		cd $(PYXB_ROOT) && git pull; \
	else \
		cd .. && git clone git://gitorious.org/pyxb/pyxb.git pyxb; \
		cd pyxb && git checkout -b ooxml-example origin/ooxml-example; \
	fi

bindings: download dml pml wml sml props

dml: dml-main.xsd
	$(ECHO) `pwd`
	./genbindings.sh $< dml dmldiagram dmlcompat dmlpicture dmllockedcanvas dmlchart

pml: pml.xsd
	$(ECHO) `pwd`
	./genbindings.sh $< pml pmldiagram pmllockedcanvas pmlchart pmlpicture pmlcompat msocompat

wml: wml.xsd
	$(ECHO) `pwd`
	./genbindings.sh $< wml wmldiagram wmlchart wmlcompat wmllockedcanvas wmldrawing wmlpicture

sml: sml.xsd
	$(ECHO) `pwd`
	./genbindings.sh $< sml smldiagram smlchart smlpicture smlcompat smllockedcanvas

props: shared-documentPropertiesExtended.xsd
	$(ECHO) `pwd`
	./genbindings.sh $< props

$(TMP):
	@mkdir -p $@

generate: bindings $(TMP) samples test-wml test-pml test-calc

#
# The real test definitions are coming below
#

PML_PYS=dumpsample.py \
		pptxpatterns.py

PML_TEMPLATES=title-and-subtitle-formatted.pptx

#
# Misc initial sample tests
#

SAMPLES_TESTS=Lorem-ipsum \
			  xls_sample \
			  hello-world

samples: $(SAMPLES_TESTS)
	$(ECHO) "Generated samples"

Lorem-ipsum: $(TMP)/Lorem-ipsum
$(TMP)/Lorem-ipsum: dumpsample.py demo.py Lorem-ipsum.docx
	$(PYTHON) dumpsample.py demo Lorem-ipsum.docx $(TMP)
	$(TOUCH) $@

xls_sample: $(TMP)/xls_sample
$(TMP)/xls_sample: dumpsample.py demo_refmode.py test-refmode.xlsx
	$(PYTHON) xls_sample.py demo_refmode test-refmode.xlsx $(TMP)
	$(TOUCH) $@

hello-world: $(TMP)/hello-world
$(TMP)/hello-world: dumpsample.py helloworld.py hello-world.docx
	$(PYTHON) dumpsample.py helloworld hello-world.docx $(TMP)
	$(TOUCH) $@

#
# Writer tests
#
WRITER_TESTS=parapr

WRITER=writer
WRITER_TEMPLATES=$(WRITER)/templates

test-wml: $(WRITER_TESTS)
	$(ECHO) "Generated WML tests"

parapr: $(TMP)/parapr
$(TMP)/parapr: $(WRITER).py $(WRITER)/parapr.py $(WRITER_TEMPLATES)/parapr.docx
	$(PYTHON) $(WRITER).py $(WRITER).parapr $(TMP)
	$(TOUCH) $@

#
# Impress tests
#
IMPRESS_TESTS=title-and-subtitle-formatted \
			  placeholders \
			  background_solid \
			  textbox_align \
			  textbox_color \

IMPRESS=impress

test-pml: $(IMPRESS_TESTS)
	$(ECHO) "Generated PML tests"

title-and-subtitle-formatted: $(TMP)/title-and-subtitle-formatted
$(TMP)/title-and-subtitle-formatted: dumpsample.py pptxpatterns.py title-and-subtitle-formatted.pptx
	$(ECHO) "Generating title-and-subtitle-formatted"
	$(PYTHON) dumpsample.py pptxpatterns title-and-subtitle-formatted.pptx $(TMP)
	$(TOUCH) $@

placeholders: $(TMP)/placeholders
$(TMP)/placeholders: $(IMPRESS).py $(IMPRESS)/placeholders.py $(IMPRESS)/placeholders.pptx
	$(ECHO) "Generating placeholders"
	$(PYTHON) $(IMPRESS).py $(IMPRESS).placeholders $(TMP)
	$(TOUCH) $@

background_solid: $(TMP)/background_solid
$(TMP)/background_solid: $(IMPRESS).py $(IMPRESS)/background_solid.py $(IMPRESS)/background_solid.pptx
	$(ECHO) "Generating background_solid"
	$(PYTHON) $(IMPRESS).py $(IMPRESS).background_solid $(TMP)
	$(TOUCH) $@

textbox_align: $(TMP)/textbox_align
$(TMP)/textbox_align: $(IMPRESS).py $(IMPRESS)/textbox_align.py $(IMPRESS)/textbox_align.pptx
	$(ECHO) "Generating textbox_align"
	$(PYTHON) $(IMPRESS).py $(IMPRESS).textbox_align $(TMP)
	$(TOUCH) $@

textbox_color: $(TMP)/textbox_color
$(TMP)/textbox_color: $(IMPRESS).py $(IMPRESS)/textbox_color.py $(IMPRESS)/textbox_color.pptx
	$(ECHO) "Generating textbox_color"
	$(PYTHON) $(IMPRESS).py $(IMPRESS).textbox_color $(TMP)
	$(TOUCH) $@

#
# Calc tests
#
CALC_TESTS=bookviews \
		   breaks \
		   calcpr \
		   col \
		   commentpr \
		   comments \
		   datavalidation \
		   definednames \
		   inputcells \
		   pagesetuppr \
		   pagesetup-a4 \
		   printoptions \
		   scenario \
		   selection \
		   sheetpr \
		   sheetview \
		   workbookpr \
		   # FIXME These scripts aren't working
		   # pagesetup-custom-size

CALC=calc
CALC_TEMPLATES=$(CALC)/templates

test-calc: $(CALC_TESTS)
	$(ECHO) "Generated Calc tests"

bookviews: $(TMP)/bookviews
$(TMP)/bookviews: $(CALC)/bookviews.py $(CALC_TEMPLATES)/bookviews.xlsx $(CALC).py
	$(ECHO) "Generating bookviews"
	$(PYTHON) $(CALC).py $(CALC).bookviews $(CALC_TEMPLATES)/bookviews.xlsx $(TMP)
	$(TOUCH) $@

breaks: $(TMP)/breaks
$(TMP)/breaks: $(CALC)/breaks.py $(CALC_TEMPLATES)/breaks.xlsx $(CALC).py
	$(ECHO) "Generating breaks"
	$(PYTHON) $(CALC).py $(CALC).breaks $(CALC_TEMPLATES)/breaks.xlsx $(TMP)
	$(TOUCH) $@

calcpr: $(TMP)/calcpr
$(TMP)/calcpr: $(CALC)/calcpr.py $(CALC_TEMPLATES)/calcpr.xlsx $(CALC).py
	$(ECHO) "Generating calcpr"
	$(PYTHON) $(CALC).py $(CALC).calcpr $(CALC_TEMPLATES)/calcpr.xlsx $(TMP)
	$(TOUCH) $@

col: $(TMP)/col
$(TMP)/col: $(CALC)/col.py $(CALC_TEMPLATES)/col.xlsx $(CALC).py
	$(ECHO) "Generating col"
	$(PYTHON) $(CALC).py $(CALC).col $(CALC_TEMPLATES)/col.xlsx $(TMP)
	$(TOUCH) $@

commentpr: $(TMP)/commentpr
$(TMP)/commentpr: $(CALC)/commentpr.py $(CALC_TEMPLATES)/commentpr.xlsx $(CALC).py
	$(ECHO) "Generating commentpr"
	$(PYTHON) $(CALC).py $(CALC).commentpr $(CALC_TEMPLATES)/commentpr.xlsx $(TMP)
	$(TOUCH) $@

comments: $(TMP)/comments
$(TMP)/comments: $(CALC)/comments.py $(CALC_TEMPLATES)/comments.xlsx $(CALC).py
	$(ECHO) "Generating comments"
	$(PYTHON) $(CALC).py $(CALC).comments $(CALC_TEMPLATES)/comments.xlsx $(TMP)
	$(TOUCH) $@

datavalidation: $(TMP)/datavalidation
$(TMP)/datavalidation: $(CALC)/datavalidation.py $(CALC_TEMPLATES)/datavalidation.xlsx $(CALC).py
	$(ECHO) "Generating datavalidation"
	$(PYTHON) $(CALC).py $(CALC).datavalidation $(CALC_TEMPLATES)/datavalidation.xlsx $(TMP)
	$(TOUCH) $@

definednames: $(TMP)/definednames
$(TMP)/definednames: $(CALC)/definednames.py $(CALC_TEMPLATES)/definednames.xlsx $(CALC).py
	$(ECHO) "Generating definednames"
	$(PYTHON) $(CALC).py $(CALC).definednames $(CALC_TEMPLATES)/definednames.xlsx $(TMP)
	$(TOUCH) $@

inputcells: $(TMP)/inputcells
$(TMP)/inputcells: $(CALC)/inputcells.py $(CALC_TEMPLATES)/inputcells.xlsx $(CALC).py
	$(ECHO) "Generating inputcells"
	$(PYTHON) $(CALC).py $(CALC).inputcells $(CALC_TEMPLATES)/inputcells.xlsx $(TMP)
	$(TOUCH) $@

pagesetuppr: $(TMP)/pagesetuppr
$(TMP)/pagesetuppr: $(CALC)/pagesetuppr.py $(CALC_TEMPLATES)/pagesetuppr.xlsx $(CALC).py
	$(ECHO) "Generating pagesetuppr"
	$(PYTHON) $(CALC).py $(CALC).pagesetuppr $(CALC_TEMPLATES)/pagesetuppr.xlsx $(TMP)
	$(TOUCH) $@

pagesetup-a4: $(TMP)/pagesetup-a4
$(TMP)/pagesetup-a4: $(CALC)/pagesetup.py $(CALC_TEMPLATES)/page-setup-a4.xlsx $(CALC).py
	$(ECHO) "Generating pagesetup-a4"
	$(PYTHON) $(CALC).py $(CALC).pagesetup $(CALC_TEMPLATES)/page-setup-a4.xlsx $(TMP)
	$(TOUCH) $@

pagesetup-custom-size: $(TMP)/pagesetup-custom-size
$(TMP)/pagesetup-custom-size: $(CALC)/pagesetup.py $(CALC_TEMPLATES)/page-setup-custom-size.xlsx $(CALC).py
	$(ECHO) "Generating pagesetup-custom-size"
	$(PYTHON) $(CALC).py $(CALC).pagesetup $(CALC_TEMPLATES)/page-setup-custom-size.xlsx $(TMP)
	$(TOUCH) $@

printoptions: $(TMP)/printoptions
$(TMP)/printoptions: $(CALC)/printoptions.py $(CALC_TEMPLATES)/printoptions.xlsx $(CALC).py
	$(ECHO) "Generating printoptions"
	$(PYTHON) $(CALC).py $(CALC).printoptions $(CALC_TEMPLATES)/printoptions.xlsx $(TMP)
	$(TOUCH) $@

scenario: $(TMP)/scenario
$(TMP)/scenario: $(CALC)/scenario.py $(CALC_TEMPLATES)/scenario.xlsx $(CALC).py
	$(ECHO) "Generating scenario"
	$(PYTHON) $(CALC).py $(CALC).scenario $(CALC_TEMPLATES)/scenario.xlsx $(TMP)
	$(TOUCH) $@

selection: $(TMP)/selection
$(TMP)/selection: $(CALC)/selection.py $(CALC_TEMPLATES)/selection.xlsx $(CALC).py
	$(ECHO) "Generating selection"
	$(PYTHON) $(CALC).py $(CALC).selection $(CALC_TEMPLATES)/selection.xlsx $(TMP)
	$(TOUCH) $@

sheetpr: $(TMP)/sheetpr
$(TMP)/sheetpr: $(CALC)/sheetpr.py $(CALC_TEMPLATES)/sheetpr.xlsx $(CALC).py
	$(ECHO) "Generating sheetpr"
	$(PYTHON) $(CALC).py $(CALC).sheetpr $(CALC_TEMPLATES)/sheetpr.xlsx $(TMP)
	$(TOUCH) $@

sheetview: $(TMP)/sheetview
$(TMP)/sheetview: $(CALC)/sheetview.py $(CALC_TEMPLATES)/sheetview.xlsx $(CALC).py
	$(ECHO) "Generating sheetview"
	$(PYTHON) $(CALC).py $(CALC).sheetview $(CALC_TEMPLATES)/sheetview.xlsx $(TMP)
	$(TOUCH) $@

workbookpr: $(TMP)/workbookpr
$(TMP)/workbookpr: $(CALC)/workbookpr.py $(CALC_TEMPLATES)/workbookpr.xlsx $(CALC).py
	$(ECHO) "Generating workbookpr"
	$(PYTHON) $(CALC).py $(CALC).workbookpr $(CALC_TEMPLATES)/workbookpr.xlsx $(TMP)
	$(TOUCH) $@
