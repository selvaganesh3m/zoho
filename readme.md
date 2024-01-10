# Manufacturing App (Zoho)

### Techstack Used 
  1. **Backend Programing Language** : Python
  1. **Framework** : Django
  1. **Project** : Manufacturing App

## Steps to run project

1. Create Virtual Environment and activate 
    - [Virtual Environment](https://github.com/selvaganesh3m/Documents/blob/main/virtualenv.md)

1. Go to project install requirements from `requiremnts.txt` file
    - `pip install -r requirements.txt`

1. Before starting project run below command
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`

1. Create superuser using below command 
    - `python3 manage.py createsuperuser`

1. Go to `admin/` and use superuser credentials to login

1. Use given `.json` file (if required) `products.json`, `warehouse.json`. 
   - `python3 manage.py loaddata warehouse.json`
   - `python3 manage.py loaddata products.josn`

**Note**: For Further doubt or queries contact: 
   - Phone: +91 8489283456
   - Email: selvaganesh3m@gmail.com


