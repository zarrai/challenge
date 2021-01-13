# Challenge

Its uses Django 3.0 and Scrapy 2.0

### Installation

Create a virtual env and activate it.

Clone the project
<pre>
git clone https://github.com/zarrai/challenge.git
</pre>

Create a Postgres Database.



Install Dependencies.
<pre>
pip install requirements.txt
</pre>

Run migrations with the command below

<pre>
python manage.py migrate
</pre>

Create a superuser to access to the admin page, run the command to register.
<pre>
python manage.py createsuperuser
</pre>

To crawl properties with the command below

<pre>
python manage.py crawl
</pre>

To view the crawled properties, run the server
<pre>
python manage.py runserver
</pre>

Visit `127.0.0.1/admin` and login with the superuser account credentials, created earlier. Properties can also be added / removed from here

To view dashboard
Visit `127.0.0.1` after starting the server.
