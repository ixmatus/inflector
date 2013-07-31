all: install

install:
	pip install

upload:
	python setup.py sdist register upload
