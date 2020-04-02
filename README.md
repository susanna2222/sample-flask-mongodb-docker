# mhm-api

### setup virtual environments
(https://realpython.com/python-virtual-environments-a-primer/)

```
pip install virtualenv
```

### Create a new virtual environment inside the directory
```
# Python 3
python3 -m venv env
```

### choose environment
```
source config/development
or
source config/production
```

### set up your shell to use the environment’s Python executable and its site-packages by default
```
# activate it
source env/bin/activate

# decativate
deactivate
```
