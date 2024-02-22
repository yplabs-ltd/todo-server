# todo-server


## 실행방법

### Production

``` sh
cd ./todo-server
pipenv shell
gunicorn -b :8000 app.wsgi
```
