# RWTH Digital Learning Lab

The digital.learning.lab is a online platform and understands itself as competence centre for teaching in the digital age. School teachers will find suggestions and inspiration here for further developing their lessons, taking into account the competencies for a digitalised living and working environment.

## 🔐 Content-Management-System

- https://dll.mll.lbz.rwth-aachen.de/admin
- https://dll.mll.lbz.rwth-aachen.de/cms

## 🛳 Container Setup (SSH)
```
sudo cp sample.env .env
```
```
sudo docker-compose up -d
```
```
sudo docker-compose run --rm web python manage.py migrate
```

## 🦸 Superuser Creation (SSH)
```
sudo docker exec -it medialab-webplattform_web_1 /bin/bash
```
```
python manage.py createsuperuser
```
