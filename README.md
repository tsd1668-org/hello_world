# hello_world
This is a demo project that displays customized hello world message

## Problem Statement
1. A user's record consists of 2 fields - Name and Date of Birth
2. **PUT /hello/{name}/** - This method is to perform an update on the user record.
> When a user with the specified name is found, an update will be performed. If the update operation is successful, an empty response with status code `201` will be returned.
> 
> When a user with the specified name is not found, an instance / record will be created. An empty response with status code `201` will be returned.
3. **GET /hello/{name}/** - This method is to retrieve the greeting message for a user.
> When a user's birthday is today, the message returned will be **Hello {name}! Happy birthday**
> 
> When a user's birthday is 5 days away, the message returned will be **Hello {name}! Your birthday is in 5 days**
> 
> Otherwise, the message returned will be **Hello {name}!**

## Pre-requisites
1. Virtual environment is installed (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
2. Python 3+

## How to run
1. Activate virtual environment
> To activate a virtual environment in Linux
```bash
python -m venv {project_name}
cd {project_name}
source bin/activate
```
> To activate a virtual environment in Mac
```bash
virtualenv {project_name}
cd {project_name}
source bin/activate
```
2. Install the required Python libraries with the following command
```bash
pip install -r requirements.txt
```
3. If it is the first time running, run the database migration using the following command
```bash
python manage.py makemigrations
python manage.py migrate
```
4. Run the application with Gunicorn using the following command.
```bash
gunicorn -b 0.0.0.0:{port} hello_world.wsgi:application
```

## Making API call
1. If you're running it in your localhost, add the following entry to your */etc/hosts* file
```bash
echo "127.0.0.1 mylab.test"
```
> (Note that the Django application has been configured to allow only mylab.test.
> To change this, edit the line in *hello_world/settings.py* containing the following
```
ALLOWED_HOSTS = ['mylab.test'])
```
2. You are ready to make the API call using your favorite HTTP client like curl or Postman. I used curl and the following shows the sample outputs. Note that for the example shown next, port `8000` is where the Django application is configured to listen on.
> Birthday is before current
```bash
$ curl mylab.test:8000/hello/john/ -XPUT -d '{"name": "john", "dob": "2001-01-01"}'
201
$ curl mylab.test:8000/hello/john/ 
{"data":"Hello john!"}
```
> Birthday is after current
```bash
$ curl mylab.test:8000/hello/john/ -XPUT -d '{"name": "john", "dob": "2001-11-11"}'
201
$ curl mylab.test:8000/hello/john/ 
{"data":"Hello john!"}
```
> Birthday is 5 days away
```bash
$ curl mylab.test:8000/hello/john/ -XPUT -d '{"name": "john", "dob": "2001-05-11"}'
201
$ curl mylab.test:8000/hello/john/ 
{"data":"Hello john! Your birthday is in 5 days”}
```
> Birthday is today
```bash
$ curl mylab.test:8000/hello/john/ -XPUT -d '{"name": "john", "dob": "2001-05-06"}'
201
$ curl mylab.test:8000/hello/john/ 
{"data":"Happy birthday, john!"}
```