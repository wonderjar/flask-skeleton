bin := ./venv/bin
pip := $(bin)/pip
flask := $(bin)/flask
gunicorn := $(bin)/gunicorn
python := $(bin)/python
virtualenv := "$(shell { command -v virtualenv ; } 2>/dev/null)"

clean:
	rm -rf env *.egg *.egg-info
	rm -rf ./venv
	find . -name \*.pyc -delete

env:
	@echo "make venv by virtualenv"
	$(virtualenv) venv -p python3
	$(pip) install -r requirements.txt

drop_db:
	FLASK_APP=app.py $(flask) drop-db

create_db:
	FLASK_APP=app.py $(flask) create-db

recreate_db:
	FLASK_APP=app.py FLASK_DEBUG=true $(flask) recreate-db

run_dev:
	FLASK_ENV=development FLASK_APP=app.py $(flask) run

rung_dev:
	FLASK_ENV=development $(gunicorn) -w 4 -b 0.0.0.0:5000 app:app

run_prod:
	FLASK_ENV=production FLASK_APP=app.py FLASK_DEBUG=false $(flask) run
