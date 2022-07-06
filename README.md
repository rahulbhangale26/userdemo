# userdemo

## System Requirements
1. Python3
2. Nodev16.15.1
3. Django 3.2.14
4. Django Rest Framework

## Setup App and Run

* Clone the repo: git clone https://github.com/rahulbhangale26/userdemo.git
* Create a database demo on postgresql server. We use other engines, Configure following settings accordingly.
* Navigate to userdemo/userdemo/settings.php and update database credentials 
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demo',
        'USER': 'username',
        'PASSWORD': 'username',
        'HOST': '127.0.01',
        'PORT': '5433',
    }
}
* Naviage to userdemo/ and open command prompt there
* Execute migration command: python manage.py migrate
* Start the Server: python manage.py runserver
* Navigate to userdemo/user-list-ui/
* Install node modules: npm install
* Execute: npm start
* Open http://localhost:8000/api/pull_users/1000 - This will pull the users and store into database
* Open http://localhost:3000 - This will open the interface which will pull the user lists from the database.
. 
