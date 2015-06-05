# WeSave
A crowdsourcing platform for health care resource allocation 
by Hannah Go, Jessica Pabico

1. Ensure python version is 2.7.6 
   $ python --version

2. Installing a Database System, PostgreSQL
   $ sudo apt-get install postgresql postgresql-contrib

3. Installing pip and easy_install
   $ sudo apt-get install python-setuptools

4. Installing a virtual environment
   $ sudo easy_install virtualenv

5. Creating and setting up the virtual environment
   $ virtualenv --no-site-packages django-user
   $ source django-user/bin/activate
   $ cd django-user

6. Installing the Django framework
   $ pip install Django==1.7.5

7. Install dependencies of psycopg2
   $ sudo apt-get build-dep python-psycopg2

8. Install psycopg2
    $ pip install psycopg2

9. Install git
    $ sudo apt-get install git

10. Setup git
    $ git config --global user.name "Your Name"
    $ git config --global user.email youremail@example.com

11. Clone Wesave repo from git
    $ git clone https://github.com/hvgo1/WeSave.git

12. Change directory
    $ cd WeSave/mysite

13. Install needed python packages 
    $ pip install django-registration-redux
    $ pip install django-countries
    $ pip install pillow

14. Create the PostgreSQL Database and User
    $ sudo su - postgres
        postgres@ubuntu:~$ psql
            postgres=# CREATE DATABASE wesavedb;
            postgres=# CREATE USER wesave WITH PASSWORD 'wesave';
            postgres=# GRANT ALL PRIVILEGES ON DATABASE wesavedb TO wesave;
            postgres=# \q
        postgres@ubuntu:~$ exit

15. Create the tables
    $ python manage.py migrate

16. Create superuser
    $ python manage.py createsuperuser

17. Make migrations
    $ python manage.py makemigrations
Hannah Go
Jessica Pabico
