freeze:
	pip freeze > requirements.txt
back:
	python3.7 run.py
front:
	cd frontend; npm run serve