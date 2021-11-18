# BooksDjangoAPI
This is a Django project in which we will implement a REST API that calls an external API service to get information about books. Additionally, we will implement a simple CRUD (Create, Read, Update, Delete) API with a local database. The external API that will be used here is the Ice And Fire API. This API requires no sign up/authentication.

### Clone the repository 
```
git clone https://github.com/MadhurBansal123/BooksDjangoAPI.git
```

### Setup virtual environment for project
```
cd <project path>
virtualenv -p python venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run database migrations 
```
python manage.py makemigrations
python manage.py migrate
```

### Run server
```
python manage.py runserver
```

### Local API endpoints
| Endpoint        |   URL                                          |
| ----------------| -----------------------------------------------|
| External books  | `http://127.0.0.1:8080/api/external-books`     |
| Books           | `http://127.0.0.1:8080/api/v1/books`           |


### Production API endpoints
| Endpoint        |   URL                                                           |
| ----------------| ----------------------------------------------------------------|
| External books  | `https://books-django-api.herokuapp.com/api/external-books`     |
| Books           | `https://books-django-api.herokuapp.com/api/v1/books`           |

### Postman Collection Import Link
https://www.getpostman.com/collections/92d38c61f3d8bea0c71a