develop: setup-git
	pip install "file://`pwd`#egg=careers[dev]"
	pip install -e .
	pip install -r test_requirements.txt

setup-git:
	git config branch.autosetuprebase always
	cd .git/hooks && ln -sf ../../hooks/* ./

lint-python:
	@echo "Linting Python files"
	PYFLAKES_NODOCTEST=1 flake8 careers
	@echo ""

pandoc:
	pandoc --from=markdown --to=rst --output=README.rst README.md

release:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*
