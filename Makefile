TEST = python -m pytest
TEST_ARGS = --cov-report=xml -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8

.PHONY: all
all: check-style check-type run-test run-test-coverage clean

.PHONY: check-type
check-type:
	$(TYPE_CHECK) A0/hello
	$(TYPE_CHECK) A0-OOP/hello
	$(TYPE_CHECK) A1/cold
	$(TYPE_CHECK) A1-OOP/cold

.PHONY: check-style
check-style:
	$(STYLE_CHECK) A0/hello
	$(STYLE_CHECK) A0-OOP/hello
	$(STYLE_CHECK) A1/cold
	$(STYLE_CHECK) A1-OOP/cold

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) A0/hello/tests
	$(TEST) $(TEST_ARGS) A0-OOP/hello/tests
	$(TEST) $(TEST_ARGS) A1/cold/tests
	$(TEST) $(TEST_ARGS) A1-OOP/cold/tests

.PHONY: run-test-coverage
run-test-coverage:
	$(TEST) --cov-report=html --cov-report=term --cov-report=annotate --cov=A0/hello A0/hello
	$(TEST) --cov-report=html --cov-report=term --cov-report=annotate --cov=A0-OOP/hello A0-OOP/hello
	$(TEST) --cov-report=html --cov-report=term --cov-report=annotate --cov=A1/cold A1/cold
	$(TEST) --cov-report=html --cov-report=term --cov-report=annotate --cov=A1-OOP/cold A1-OOP/cold

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 
	