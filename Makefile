VENV_NAME?=everydayCoding
SOURCE=. $(VENV_NAME)/bin/activate &&

.PHONY: lint
lint: ## format all code
	${SOURCE} isort ./problems/*.py
	${SOURCE} black ./problems/*.py

.PHONY: install
install: # install developer requirements
	${SOURCE} pip3 install --upgrade pip
	${SOURCE} pip3 install -r requirements.txt

.PHONY: venv
venv: ## Create a virtualenv
	python3 -m venv $(VENV_NAME)

.PHONY: activate
activate: ## Activate a virtualenv
	source $(VENV_NAME)/bin/activate
