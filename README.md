<p align='center'>
<img width="200" src="static/images/iste.png" alt="ISTE KA LOGO">
</p>
<h1 align='center'>PRODYOGIKI'23</h1>
This website is using django backend. All you need to do is to go through https://docs.djangoproject.com/ so that you get the basic knowledge that how things are working in django.

## Steps to follow :pencil2::

1. First of all install Django:

For any system:
```console
  python -m pip install Django
```
For ArchLinux:
```bash
sudo pacman -S python-django
```

2. Clone the repository:

```bash
git clone https://github.com/istenith/join.istenith.com.git
```

3. Change the directory to prody-2023 using:

```bash
cd join.istenith.com
```

4. Create a virtual environment:

```bash
pip install virtualenv
virtualenv venv
```

5. Activate the virtual environment

```bash
source venv/bin/activate
```

6. Now install all the packages which are being used in this project:

```bash
pip install -r requirements.txt
```

7. Migrate all the database 
```bash
python manage.py migrate
```

8. Now run the development server:

```bash
python manage.py runserver
```
