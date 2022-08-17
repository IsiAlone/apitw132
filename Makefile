.PHONY: help clean
.DEFAULT_GOAL := help

# AutoDoc
define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef

export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


.PHONY: install
install: ## install requirements and project in editable mode
	pip install -r requirements_dev.txt

.PHONY: lint 
lint: ## pass the tests and flake8 to the code
	flake8 funcion

.PHONY: docs-serve
docs-serve: ## generate documentation with mkdocs (docs-serve)
	pip install -r requirements_doc.txt
	mkdocs serve -a localhost:8001

.PHONY: docs-build
docs-build: ## generate documentation with mkdocs (docs-build)
	pip install -r requirements_doc.txt
	mkdocs build