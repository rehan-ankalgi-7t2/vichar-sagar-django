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

## Deploy on vercel 🚀

Deploying a **Django app** on **Vercel** requires some configuration because Vercel is primarily designed for frontend frameworks like Next.js, but it can also handle backend applications. To deploy a Django app on Vercel, you’ll use Vercel's **serverless functions** to serve the app and the **ASGI** interface, which allows for Django to be deployed in a serverless environment.

Here’s a step-by-step guide:

### 1. **Set Up the Django Project Locally**

If you don’t have a Django project, you can create one:

```bash
django-admin startproject myproject
cd myproject
```

### 2. **Install Required Dependencies**

Make sure your project uses **Django 3.1** or higher, which supports **ASGI** out of the box. You will also need **ASGI** and **uvicorn** for handling the serverless environment.

Install the required dependencies in your `requirements.txt` file:

```bash
asgiref==3.2.10
Django==3.1.7
uvicorn==0.13.4
```

If you don't have `requirements.txt`, you can generate it:

```bash
pip freeze > requirements.txt
```

### 3. **Configure Django for ASGI**

Modify `myproject/asgi.py` to ensure it's compatible with Vercel’s serverless functions.

```python
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
```

### 4. **Create Vercel Configuration**

#### Step 4.1: Create a `vercel.json` file

This file will help Vercel understand how to deploy your Django app. In the root of your project directory, create a `vercel.json` file.

```json
{
  "version": 2,
  "builds": [
    {
      "src": "myproject/asgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "myproject/asgi.py"
    }
  ]
}
```

#### Step 4.2: Setup Serverless Function

Create a `api/` directory in your project root and move your Django app inside it. The `asgi.py` file will be used to serve your app as a serverless function.

Project structure should look like this:

```
/myproject
   /myproject
   __init__.py
   asgi.py
   settings.py
   urls.py
   wsgi.py
/requirements.txt
/vercel.json
```

### 5. **Configure Django for Static Files**

Since Vercel is optimized for static files, you need to configure Django to collect static files before deployment.

In your `settings.py`, configure static files and add `whitenoise` for serving them in production:

```python
# settings.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add WhiteNoise to middleware to serve static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise added here
    ...
]

# Tell Django to use the staticfiles storage with WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### Collect Static Files

Run the following command to collect static files:

```bash
python manage.py collectstatic
```

### 6. **Deploy to Vercel**

#### Step 6.1: Install Vercel CLI

To deploy your app, install the **Vercel CLI**:

```bash
npm i -g vercel
```

#### Step 6.2: Log in to Vercel

If you don't already have a Vercel account, create one. Then log in to Vercel:

```bash
vercel login
```

#### Step 6.3: Deploy Your Django App

In your project directory, run:

```bash
vercel
```

The command will prompt you to select some options like project name and whether you want to link it to a Git repository.

Once the process is done, your Django app will be deployed on Vercel.

### 7. **Configure Environment Variables**

After deployment, you will need to configure environment variables (such as `DATABASE_URL`, `SECRET_KEY`, etc.) for your Django app in the Vercel dashboard.

To do this:
1. Go to your Vercel project dashboard.
2. Click on **Settings**.
3. Scroll down to **Environment Variables** and add any variables your app requires (like your `SECRET_KEY` and database connection).

### 8. **Set Up a Database**

Since Vercel deployments are stateless, you’ll need to use an external database (e.g., PostgreSQL, MongoDB, etc.) for storing data. You can use services like **Heroku Postgres**, **AWS RDS**, **MongoDB Atlas**, or any other cloud-based database provider.

1. Add your external database URL to your `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}
```

2. Run migrations:

```bash
python manage.py migrate
```

### 9. **Final Testing**

After deployment, test the app by visiting the Vercel-provided URL. Your Django app should now be live and running on Vercel.

### Summary:
- Set up Django with ASGI and Vercel.
- Use Vercel’s serverless functions and configure the app with a `vercel.json`.
- Ensure static files are handled by WhiteNoise and configure the Django app.
- Deploy the app using Vercel CLI.
- Set up environment variables and an external database.

This will deploy your Django app on Vercel, leveraging serverless functions to serve your app.