# digital.learning.lab

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The digital.learning.lab is a online platform and understands itself as competence centre for teaching in the digital age. School teachers will find suggestions and inspiration here for further developing their lessons, taking into account the competencies for a digitalised living and working environment.

## 🛳 Container Setup 
1. Create an `.env` file from `sample.env`
2. Run `docker-compose up` to setup project
3. Run `docker-compose run --rm web python manage.py migrate`

## 🦸 Superuser Creation
1. Open Docker CLI of **webplattform_web_1**
2. Run `python manage.py createsuperuser`
3. Type in new credentials
