____
## To run application on local machine:
1. Clone the repository:
```git clone https://github.com/Kirastel/Shortener.git && cd Shortener```


2. Create a virtual environment:
```python3 -m venv venv```

3. Activate the virtual environment:
```source venv/bin/activate```

4. Install all required dependencies:
```pip install -r requirements.txt```


5. Apply the migrations:
```python manage.py migrate```

6. Create superuser:
```python manage.py createsuperuser```

7. Run server:
```python manage.py runserver```

8. From now local version is available at ```http://localhost:8000```
____
