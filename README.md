# Vichar Sagar 🌊

## About Project
>A Haven for Thoughtful Musings

> Welcome to Vichar Sagar, a digital haven where ideas flow freely and thoughts find their expression. Inspired by the inquisitive and philosophical spirit of Taarak Mehta from the beloved Indian sitcom, this blog is a testament to the power of intellectual discourse and the beauty of human contemplation.

Just as Taarak Mehta brought laughter and wisdom into the lives of millions, Vichar Sagar aims to spark curiosity, ignite conversations, and foster a deeper understanding of the world around us. Here, you'll find a diverse range of articles exploring topics from philosophy and literature to current affairs and personal reflections.

Join us on this intellectual journey as we delve into the depths of human thought, challenge conventional wisdom, and celebrate the power of ideas. Whether you're a seasoned thinker or just beginning to explore the world of philosophy, Vichar Sagar offers a space for everyone to share their perspectives and connect with like-minded individuals.

### About Taarak Mehta

![Taarak Mehta's Portrait](https://m.economictimes.com/thumb/msid-91614750,width-1200,height-900,resizemode-4,imgsize-33516/sailesh-lodha.jpg)

Taarak Mehta, the man behind Vichar Sagar, is a passionate writer and thinker deeply influenced by the iconic character from the popular Indian sitcom. With a keen eye for detail and a love for intellectual pursuits, Taarak Mehta brings his unique perspective to the blog, offering insightful commentary and thought-provoking discussions.

Let's embark on this intellectual adventure together!

## Project Setup

1. Create Virtual Environment

```python
python -m venv .venv
```

2. install  `Django`

```python
python -m pip install Django
```

3. create a new django project

```python
django-admin startproject mysite
```

4. Setup static and media folders to store static files and assets

```python
import os
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

5. steup templates folder

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # change this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

6. Setup templates

```python
config
- config
- templates
- - base.html
```

```python
// base.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>
        {% block title %} Vichar Sagar {% endblock %}
    </title> 
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

serve this template using views and url

```python
# config/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello, name="hello") # here...
]
```

```python
# config/views.py
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'base.html')
```

7. Create a new App

```python
python manage.py startapp app
```

register the app in the projects `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vicharsagar', # like so
    'tailwind',
    'theme'
]
```

8. install `Pillow` package to support `ImageField()` in the models

```python
python -m pip install Pillow
```

---

## django-tailwind setup

1. provide `npm.cmd` installation path

```python
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
NPM_BIN_PATH = "D:/rehan-dev-stuff/node-installation/npm.cmd"
```

2. Install `django-tailwind` package using pip, we’ll be installing another side package along side for hot reload.

```python
python -m pip install 'django-tailwind[reload]'
```

3. include tailwind in the `INSTALLED_APPS` 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vicharsagar',
    'tailwind'
]
```

4. run command to initialize tailwind and install the tailwind npm package

```python
python manage.py tailwind init
```

```bash
// output  
  [1/1] app_name (theme): 
Tailwind application 'theme' has been successfully created. Please add 'theme' to INSTALLED_APPS in settings.py, then run the following command to install Tailwind CSS dependencies: `python manage.py tailwind install`
```

5. include the generated `theme` app in `INSTALLED_APPS` in [`settings.py`](http://settings.py) and run the below command

```bash
python manage.py tailwind install
```

6. start tailwind reload mode

```bash
python manage.py tailwind start
```