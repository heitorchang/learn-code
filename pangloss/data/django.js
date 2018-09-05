// Use text-mode

var data = [
/*
  {
    topic: 'TOPIC',
    title: 'CARD TITLE',
    reference: 'REFERENCE SOURCE',
    description: 'DESCRIPTION',
    code: `
CODE
CODE    
    `
  },
*/

  { // begin new topic
    topic: 'Git',
    title: '.gitignore',
    reference: '',
    description: `Ignore Emacs, Python, SQLite, Virtualenv, and settings`,
    code: `
# Emacs
*~
\\#*\\#

# Python
__pycache__/
*.py[cod]
*$py.class

# virtualenv
venv/
ENV/

# Django
*.log
db.sqlite3

# uploaded multimedia
media/

# and any sensitive data
# hide SECRET_KEY in settings.py
    `
  },

  { // begin new topic
    topic: 'Databases',
    title: 'MySQL clients',
    reference: 'https://docs.djangoproject.com/en/1.11/ref/databases/',
    description: `
Django 2.0 asks for
<ul>
      <li>mysqlclient</li>
</ul>
<br>
Other clients
<ul>
      <li>MySQLdb</li>
      <li>MySQL Connector (Oracle)</li>
      </ul>      
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Databases',
    title: 'MySQL configuration',
    reference: 'https://docs.djangoproject.com/en/1.11/ref/databases/',
    description: `
If <code>host</code> is unspecified, it connects to a MySQL database on localhost.
    `,
    code: `
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/mysql.cnf',
        },
    }
}


# mysql.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8    
    `
  },

  { // begin new topic
    topic: 'Project',
    title: 'New project',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial01/',
    description: `Use virtualenv if needed`,
    code: `
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate

pip install Django

django-admin startproject PROJECTNAME

cd PROJECTNAME

# Create .gitignore as described in Git section

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
    `
  },

  { // begin new topic
    topic: 'Project',
    title: 'New app',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial01/ https://docs.djangoproject.com/en/1.11/intro/tutorial02/',
    description: `A project is like an environment, while an app does something concrete, like a blog, or a poll.<br><br>
    
    After creating an app, it must be added to settings.py
    `,
    code: `
python manage.py startapp APPNAME


# settings.py

# ...
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    # ...
]
    `
  },


  { // begin new topic
    topic: 'Blog Tutorial',
    title: '1. Create new app',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial01/',
    description: `Use virtualenv if needed.`,
    code: `
django-admin startproject project
cd project

python manage.py startapp blog

# project/settings.py

# ...
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    # ...
]
`
  },


  { // begin new topic
    topic: 'Blog Tutorial',
    title: '2. Define app\'s URLs',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial01/',
    description: `Two urls.py need to be edited. One for the app, and the other for the project. The project\'s urls.py includes the app\'s.`,
    code: `
# blog/urls.py

from django.conf.urls import url

from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


# project/urls.py

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]
    `
  },

  { // begin new topic
    topic: 'Blog Tutorial',
    title: '3. Models',
    reference: 'https://docs.djangoproject.com/en/1.11/topics/db/queries/',
    description: `A foreign key is a reference to an instance of another object (model).
    `,
    code: `
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    authors = models.ManyToManyField(Author)
    rating = models.IntegerField()
    `
  },

  { // begin new topic
    topic: 'Blog Tutorial',
    title: '4. Admin',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial02/',
    description: ``,
    code: `
# blog/admin.py

from django.contrib import admin

from . import models

admin.site.register(models.Blog)
admin.site.register(models.Author)
admin.site.register(models.Entry)
    `
  },

  { // begin new topic
    topic: 'Blog Tutorial',
    title: '5. Return HttpResponse in view',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial03/',
    description: `For very simple output, HttpResponse is more straightforward than render.`,
    code: `
# blog/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Blog index")
    

# Then run:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
    `
  },

  { // begin new topic
    topic: 'Official Tutorial',
    title: 'Part 1 (Django 1.11)',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial01/',
    description: `
A basic poll application.

<ul>
<li>Creating a project and Polls app</li>
<li>HttpResponse View</li>
<li>urls.py</li>
</ul>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Official Tutorial',
    title: 'Part 2',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial02/',
    description: `
Database, model, and Admin

<ul>
<li>Question, Choice models</li>
<li>Installing app in settings.py</li>
<li>Migrating</li>
<li>Shell</li>
<li>__str__ method in model</li>
<li>Registering models in the admin site</li>
</ul>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Official Tutorial',
    title: 'Part 3',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial03/',
    description: `
Views

<ul>
<li>Views taking an argument and corresponding urls</li>
<li>Templates</li>
<li>render() shortcut</li>
<li>get_object_or_404</li>
<li>{% url %} template tag</li>
<li>app_name = "polls" in urls.py</li>
</ul>

    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Official Tutorial',
    title: 'Part 4',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial04/',
    description: `
Form processing and generic views

<ul>
<li>Simple form</li>
<li>Save votes in views.py</li>
<li>HttpResponseRedirect after successful POST</li>
<li>Generic views</li>
<li>pk in urls</li>
</ul>

    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Official Tutorial',
    title: 'Part 5',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial05/',
    description: `
Automated testing

<ul>
<li>Question.was_published_recently() bug</li>
<li>Run tests with python manage.py test polls</li>
<li>Test a view</li>
<li>Test a DetailView</li>
</ul>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Official Tutorial',
    title: 'Part 6',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial06/',
    description: `
<ul>
<li>Collect static files into a single location</li>
</ul>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Official Tutorial',
    title: 'Part 7',
    reference: 'https://docs.djangoproject.com/en/1.11/intro/tutorial07/',
    description: `
Customizing the Admin site

<ul>
<li>Reorder fields in forms</li>
<li>Add related objects</li>
<li>Multiple inline Choices for a Question</li>
<li>Display more columns for Questions</li>
<li>Date filter</li>
<li>Search</li>
<li>Customizing project's templates</li>
<li>Customizing app's templates</li>
<li>Customizing admin index page</li>
</ul>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Static files',
    title: 'settings.py',
    reference: '',
    description: `At the end of settings.py, add`,
    code: `
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
  
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    
    `
  },

  { // begin new topic
    topic: 'Static files',
    title: 'urls.py',
    reference: '',
    description: `In PROJECT/urls.py, add`,
    code: `
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path(...),
  path(...),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    `
  },


  { // begin new topic
    topic: 'Model fields',
    title: 'String-based fields should not use null',
    reference: '',
    description: `Avoid using null on string-based fields such as CharField and TextField.
      <br><br>
    Exception: if a CharField has unique=True and blank=True set, then null=True is required to avoid constraint violations.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Model fields',
    title: 'ImageField files',
    reference: 'https://docs.djangoproject.com/en/2.0/ref/models/fields/',
    description: `Define the directory where the files for an ImageField will be saved. The directory will be created under MEDIA_ROOT.`,
    code: `
class Product:
    photo = ImageField(upload_to='products/')
    
    `
  },


  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },
  
];
