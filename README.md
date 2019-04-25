# bab_django_montmartre
Django project template for futures Boite à Bidules websites.
It will be soon used with bab apps...

## TODO list
- [X] Splitted settings
- [X] Default French settings
- [X] Twitter's bootstrap4
- [X] django-sitetree
- [ ] django-allauth
- [ ] Core application
- [ ] Apache2 site's template
- [ ] Cookiecutter integration

## Dependencies
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
