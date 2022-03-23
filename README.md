# mqtt_app app

This app was bootstrapped with [Imagine.ai](https://imagine.ai) 💛
> Imagine.ai is an app starter on steroids! 

1- python -m venv env
2- env\Scripts\activate
3- pip install -r requreiments.txt
4- python manage.py makemigrations
5- python manage.py migrate
6- python manage.py runserver
7- open new terminal
  7.1 -  env\Scripts\activate
  7.2 - cd mqtt_server
  7.3 - python subscribe2django.py
8- open new terminal
  8.1 -  env\Scripts\activate
  8.2 - cd mqtt_server
  8.3 - python publish_payload2django.py



### Make API calls against the server

1. Go to [http://localhost:8000/swagger](http://localhost:8000/swagger) to see Swagger documentation for API endpoints.
2. Run the APIs by clicking the "Try it now" button on the Swagger page.

### Run Django admin dashboard

1. Setup a password to login to the Django admin dashboard.

```
make adminuser password=<choose-a-secure-password>
```

2. Go to [http://localhost:8000/admin](http://localhost:8000/admin) and login to the dashboard using username `admin` and the password you chose in step 1 above.

### Learn More

1. Learn more about: 
  - the [Django architecture choices](https://imagine.ai/docs/architecture-django) used.
  - the [best practices](https://imagine.ai/docs/best-practices) followed.

2. Imagine is in beta - here are the [known issues](https://imagine.ai/docs/known_issues) that we are working to fix.
