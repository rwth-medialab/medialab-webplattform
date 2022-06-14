# digital.learning.lab

The digital.learning.lab is a online platform and understands itself as competence centre for teaching in the digital age. School teachers will find suggestions and inspiration here for further developing their lessons, taking into account the competencies for a digitalised living and working environment.

## 🛳 Container Setup 
```
cp sample.env .env
```
```
docker-compose up -d
```
```
docker-compose run --rm web python manage.py migrate
```

## 🦸 Superuser Creation
```
docker exec --tty medialab-webplattform_web_1 python manage.py createsuperuser
```
