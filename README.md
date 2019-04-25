# bab_django_montmartre
Django project template for futures Boite à Bidules websites

## Features
- [X] Splitted settings
- [X] Default French settings
- [X] Twitter's bootstrap4
- [X] django-sitetree
- [ ] django-allauth
- [ ] Apache2 site's template
- [ ] Cookiecutter integration

## Dépendances
* django-bootstrap4
* django-sitetree
* django-allauth

## Installation
* make project directory

* create a virtual environment inside it

```
virtualenv .venv -p python3
```

* install django

```
pip install django
```

* create a project using this template

```
django-admin createproject <project-name> . --template=https://github.com/boite-a-bidules-fr/bab_django_montmartre/archive/master.zip
```
* install dependencies
```
pip install -r requirements.txt
```
