venv_path := ~/.venv/mqtt_app
bin_path := ${venv_path}/bin
all:
	@echo "Available commands: \n\
		make installdeps : to install virtualenv and other dependent packages\n\
		make createmigrations: generate the migration files for defined models \n\
		make install : to install virtualenv, other dependent packages, and create migrations \n\
		make migrate : creates tables in database \n\
		make adminuser : creates a superuser to access the django admin \n\
		make dev : runs django development server \n\
		make run : run the django application \n\
		make shell : activate the virtualenv with all required packages available in the environment \n\
 	"

installdeps:
	python3 -m pip install virtualenv
	python3 -m venv ${venv_path}
	@echo ${bin_path}
	${bin_path}/pip3 install -r requirements.txt
	${bin_path}/pip3 install -r requirements_dev.txt

createmigrations:
	${bin_path}/python3 manage.py makemigrations

install: installdeps createmigrations

migrate:
	${bin_path}/python3 manage.py migrate

dev:
	${bin_path}/python3 manage.py runserver

run:
	${bin_path}/python3 manage.py runserver

shell:
	@echo 'To activate the venv use source ~/.venv/mqtt_app/bin/activate . Use deactivate to exit'

adminuser:
	test $(password) || (echo '>> password is not set. (e.g password=mysecretpassword)'; exit 1)
	@echo 'creating Django admin user'
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
	User.objects.create_superuser('admin', '', '$(password)')" \
	| ${bin_path}/python3 manage.py shell
	@echo 'Username: admin , Password: $(password)'
