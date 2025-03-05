# Django (Web Framework)

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Overview

Built by experienced developers, Django takes care of much of the hassle of web development, enabling developers to focus on writing their app without reinventing the wheel.

### Key Features

- **ORM (Object-Relational Mapping)**: Database abstraction
- **Admin Interface**: Automatic admin interface
- **URL Routing**: Clean, elegant URL scheme
- **Template System**: Dynamic HTML generation
- **Forms**: Form creation and validation
- **Authentication**: User authentication system
- **Security**: Built-in security features

## History

- **2003**: Started at Lawrence Journal-World
- **2005**: Released publicly under BSD license
- **2008**: Django Software Foundation formed
- **2020**: Django 3.0 with ASGI support

## Basic Structure

    # urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]

    # models.py
    from django.db import models

    class Article(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        pub_date = models.DateTimeField('date published')

    # views.py
    from django.shortcuts import render
    from .models import Article

    def index(request):
        latest_articles = Article.objects.order_by('-pub_date')[:5]
        return render(request, 'articles/index.html', {
            'latest_articles': latest_articles
        })

## Project Components

### Models
- Database layout
- Data relationships
- Data validation

### Views
- Request handling
- Business logic
- Template rendering

### Templates
- HTML files
- Template tags
- Template inheritance

### Forms
- Data validation
- HTML form generation
- CSRF protection

## Best Practices

### DRY (Don't Repeat Yourself)
- Use template inheritance
- Create reusable apps

### Security
- Use CSRF tokens
- Validate user input
- Escape output

### Performance
- Database optimization
- Caching
- Lazy loading

## See Also
- [Python](/wiki/Python)
- [Frontend](/wiki/Frontend)
- [PostgreSQL](/wiki/PostgreSQL)