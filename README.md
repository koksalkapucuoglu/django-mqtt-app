# mqtt_app app

## Tech Stack

**Core Tech:** Python

**Backend Service:** Django, Django Rest Framework, MQTT

**Database:** SQLite

**Documentation:** Swagger

## Features

- Integrate Mqtt publising and subscribing system
- Device and Broker management
- Supports pagination system 

## Run Locally

Clone the project

```bash
  git clone https://github.com/koksalkapucuoglu/django-mqtt-app.git
```

Go to the project directory

```bash
  cd django-mqtt-app
```

Create python env

```bash
  python -m venv env
```

Activate enviroment

```bash
  source env/Scripts/activate
```

or

```bash
  env\Scripts\activate
```

Install requirements

```bash
  pip install -r requirements.txt
```

Detect django model changes

```bash
  python manage.py makemigrations
```

Apply django model changes

```bash
  python manage.py migrate
```

Run django project

```bash
  python manage.py runserver
```

![App Screenshot 1](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot 2](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Add New Record Mqtt Device 

Run django project

```bash
  python manage.py runserver
```

Open new terminal and activate enviroment

```bash
  env/Scripts/activate
```

Navigate mqtt_server directory

```bash
  cd mqtt_server
```

Run subscribe2django script

```bash
  python subscribe2django.py
```

Open new terminal and activate enviroment

```bash
  env/Scripts/activate
```

Navigate mqtt_server directory

```bash
  cd mqtt_server
```

Run publish_payload2django script

```bash
  python publish_payload2django.py
```

![App Screenshot 3](https://via.placeholder.com/468x300?text=App+Screenshot+Here)



## Make API calls against the server

1. Go to [http://localhost:8000/api/swagger](http://localhost:8000/api/swagger) to see Swagger documentation for API endpoints.
2. Run the APIs by clicking the "Try it now" button on the Swagger page.

