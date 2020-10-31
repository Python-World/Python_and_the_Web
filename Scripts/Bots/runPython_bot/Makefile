hi:
	@echo hi

requirements:
	rm -rf venv
	python3.8 -m venv venv
	. venv/bin/activate && python3.8 -m pip install -r requirements.txt -U
	clear

start:
	. venv/bin/activate && python3.8 start.py