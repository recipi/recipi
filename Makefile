.PHONY: clean deps develop docs clean-build lint test coverage coverage-html tox migrate runserver
PYTEST_OPTS :=
COVER := recipi
APP := src/

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "develop - install all packages required for development"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "coverage - generate test coverage report"
	@echo "coverage-html - generate test coverage report, html output"
	@echo "tox - Run all tests in a tox container"


clean: clean-build clean-pyc


deps:
	@echo "--> Installing python dependencies"
	pip install --upgrade pip setuptools wheel
	pip install --use-wheel -e .
	pip install --use-wheel "file://`pwd`#egg=recipi[tests]"
	pip install --use-wheel "file://`pwd`#egg=recipi[postgresql]"
	pip install --use-wheel "file://`pwd`#egg=recipi[redis]"
	pip install --use-wheel --upgrade -r requirements/base.txt
	@echo ""


develop: deps
	@echo "--> Installing npm dependencies"
	if test -z "$$TRAVIS"; then pip install "nodeenv<=0.12.1" && nodeenv -p; fi; \

	# Install nodejs dependencies
	@npm install --python=python2

	# Extract CLDR from babel source installation
	@python extras/import_cldr.py


docs: clean-build
	pip install --use-wheel "file://`pwd`#egg=recipi[docs]"
	sphinx-apidoc --force -o docs/source/modules/ src/recipi src/recipi/migrations src/recipi/tests src/recipi/settings.py
	$(MAKE) -C docs clean
	$(MAKE) -C docs html


clean-build:
	@rm -fr build/ src/build
	@rm -fr dist/ src/dist
	@rm -fr *.egg-info src/*.egg-info
	@rm -fr htmlcov/
	$(MAKE) -C docs clean


lint:
	flake8 recipi --ignore='E122,E124,E125,E126,E128,E501,F403' --exclude="**/migrations/**"


test:
	@py.test ${PYTEST_OPTS} ${APP}


coverage:
	py.test --cov=${COVER} --cov-report=term-missing ${PYTEST_OPTS} ${APP}


coverage-html:
	py.test --cov=${COVER} --cov-report=html ${PYTEST_OPTS} ${APP}


tox:
	@tox


i18n:
	@python manage.py babel makemessages -d django -l de
	@python manage.py babel compilemessages -d django -l de
	@python manage.py babel makemessages -d djangojs -l de
	@python manage.py babel compilemessages -d djangojs -l de
	@python manage.py compilejsi18n -d djangojs -l de
