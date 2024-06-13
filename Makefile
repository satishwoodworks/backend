# Put it first so that "make" without argument is like "make help".
help:
	@echo "Hello"

.PHONY: help

# Test Commands ===========================================
# You can set these variables from the command line, and also from the environment
TESTSDIR 	?= tests
PYTESTOPTS  ?= --cov-report term --cov=server

test:
	@pytest $(TESTSDIR) $(PYTESTOPTS)