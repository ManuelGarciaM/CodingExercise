## Part 1 Api

This servers a simple endpoint at /api/. 
It currently only has the location of my favorite restaurant.

### Demo
A running demo can be found deployed on http://ce-env.fxrhvmyt8y.us-west-2.elasticbeanstalk.com/api/

##### Deployment details
I chose to use Elastic Beanstalk because it simplifies deployments and can integrate many useful AWS services.
After initializing Elastic Beanstalk using the Elastic Beanstalk CLI with `eb init` and setting up paths and virtualenv configurations, future updates can be pushed with  `eb deploy`.

### Running the code 
Git Clone the code and cd into cloned directory.

The code can be run by first creating a virtual environment `virtualenv -p python3 venv` and activating it with `source venv/bin/activate`. Then install all the requirements with `pip install -r requirements.txt`. The environment variables for settings and the secret_key also need to be set with `export DJANGO_SETTINGS_MODULE=CodingExercise.settings` and `export SECRET_KEY=<KEY>` replacing <Key> with the key of your choice. 

The server can be run with `python manage.py runserver`

The api endpoint can then be found at http://localhost:8000/api/. Note that static files will not be loaded unless `python manage.py collectstatic` is also run.

The tests can be run with `python manage.py test api`

Note that `python manage.py test` will throw an import error because of a python test from the second part of the test. I  included the code here so I wouldn't have to manage a bunch of repos. It can be safely moved out of this directory without impacting the rest api. 

If trying to deploy this configuration onto Elastic Beanstalk, the 'SECRET_KEY' variable needs to be set in either .ebextensions/django.config or in the Elastic Beanstalk interface.

## Part 1.2: Webpage
Located in single_page_app folder

Hosted on AWS S3 http://coding-exercise-fs.s3-website-us-west-2.amazonaws.com/

## Part 2: Code challenges
Located in Part 2 folder

First part can be tested by `python printer.py`

First part can be tested by `python test_printer.py`

Both parts can run using python 2 or 3.

#### SQL part
Located in Part 2 folder in query.sql.
