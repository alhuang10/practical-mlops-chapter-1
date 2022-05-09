install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=C hello_world.py

test:
	pytest -v test_hello_world.py
