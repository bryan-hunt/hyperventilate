
.PHONY: all
all: html pdf

.PHONY: html
html: data
	$(MAKE) -C documentation html

.PHONY: pdf
pdf: data
	$(MAKE) -C documentation latexpdf
	
.PHONY: data
data:
	$(MAKE) -C examples/doxygen all
	$(MAKE) -C examples/tinyxml all
	$(MAKE) -C examples/specific all

.PHONY: distclean
distclean: clean
	$(MAKE) -C documentation clean

.PHONY: clean
clean:
	$(MAKE) -C examples/doxygen $@
	$(MAKE) -C examples/tinyxml $@
	$(MAKE) -C examples/specific $@

.PHONY: test
test:
	pytest

.PHONY: dev-test
dev-test:
	pytest

.PHONY: flake8
flake8:
	flake8 breathe

.PHONY: black
black:
	black --check .

.PHONY: type-check
type-check:
	mypy --warn-redundant-casts --warn-unused-ignores breathe tests
