# Setting Up Django for Success

This is the result of my really long article on setting up a new Django project.

Article: [https://jilles.me/setting-up-django-for-success/](https://jilles.me/setting-up-django-for-success/)

___

The article is ever-evolving. Feel free to suggest improvements in GitHub issues. 

## What's missing?

### Database: SQLite WAL mode
SQLite will suffice for most of the starter project. Especially with journal: WAL mode enabled.
I have not yet added this to the article.

### Django Template Components:
Tailwind is really great in environments where you can declare components. Instead of <button class="..." /> you'd
create a single <Button primary /> component. I might incorporate

1. django-components: https://github.com/django-components/django-components
2. django-template-partials: https://github.com/carltongibson/django-template-partials

I am learning towards 1.

### Asynchronous Tasks: Celery
Any real world project is likely going to need asynchronous task handling. In Django I think Celery
is a great good solution. Setting it up might become part of the "for success" article.
