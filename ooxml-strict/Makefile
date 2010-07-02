RM=rm -rf
PYXB_ROOT=../pyxb
PYTHON=PYTHONPATH=$(PYXB_ROOT) python
TMP=tmp

ALL:generate

clean:
	$(RM) dml pml wml sml props

download:
	@echo "Getting Pyxb"
	if test -d $(PYXB_ROOT) ; then \
		cd $(PYXB_ROOT) && git pull; \
	else \
		cd .. && git clone git://gitorious.org/pyxb/pyxb.git pyxb; \
		cd pyxb && git checkout -b ooxml-example origin/ooxml-example; \
	fi

bindings: download dml pml wml sml props

dml: dml-main.xsd
	@echo `pwd`
	./genbindings.sh $< dml dmldiagram dmlcompat dmlpicture dmllockedcanvas dmlchart

pml: pml.xsd
	@echo `pwd`
	./genbindings.sh $< pml pmldiagram pmllockedcanvas pmlchart pmlpicture pmlcompat msocompat

wml: wml.xsd
	@echo `pwd`
	./genbindings.sh $< wml wmldiagram wmlchart wmlcompat wmllockedcanvas wmlpicture

sml: sml.xsd
	@echo `pwd`
	./genbindings.sh $< sml smldiagram smlchart smlpicture smlcompat smllockedcanvas 

props: shared-documentPropertiesExtended.xsd
	@echo `pwd`
	./genbindings.sh $< props

$(TMP):
	@mkdir -p $@

generate: bindings $(TMP) samples test-wml test-sml test-pml

#
# The real test definitions are coming below
#

SAMPLE_PYS=dumpsample.py \
		   demo.py \
		   xls_sample.py \
		   demo_refmode.py \
		   helloworld.py

SAMPLE_TEMPLATES=Lorem-ipsum.docx \
				 test-refmode.xlsx \
				 hello-world.docx

WML_PYS=wml_tests.py \
		wml_tests/testcases_para.py

WML_TEMPLATES=wml_tests/templates/test-paras.docx

SML_PYS=

SML_TEMPLATES=sml_tests/templates/test-sst.xlsx

PML_PYS=dumpsample.py \
		pptxpatterns.py

PML_TEMPLATES=title-and-subtitle-formatted.pptx

samples: $(SAMPLE_PYS) $(SAMPLE_TEMPLATES)
	@echo "Generating samples"
	$(PYTHON) dumpsample.py demo Lorem-ipsum.docx $(TMP)
	$(PYTHON) xls_sample.py demo_refmode test-refmode.xlsx $(TMP)
	$(PYTHON) dumpsample.py helloworld hello-world.docx $(TMP)

test-wml: $(WML_PYS) $(WML_TEMPLATES)
	@echo "Generating WML tests"
	$(PYTHON) wml_tests.py wml_tests.testcases_para $(TMP)

test-sml: $(SML_PYS) $(SML_TEMPLATES)
	@echo "Generating SML tests"

test-pml: $(PML_PYS) $(PML_TEMPLATES)
	@echo "Generating PML tests"
	$(PYTHON) dumpsample.py pptxpatterns title-and-subtitle-formatted.pptx $(TMP)

