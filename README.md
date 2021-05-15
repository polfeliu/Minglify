
# Models
https://docs.djangoproject.com/en/3.2/intro/tutorial02/

##Migrate models to database
```shell script
python manage.py makemigrations vue_app
python manage.py sqlmigrate vue_app 0001
python manage.py migrate
```

## Create django superuser
```shell script
python manage.py createsuperuser
```

##Shell
```shell script
python manage.py shell
```

```python
from vue_app.models import Post
Post.objects.all()
```

# URL patterns and views
https://docs.djangoproject.com/en/3.2/intro/tutorial03/

# Forms 
https://docs.djangoproject.com/en/3.2/topics/forms/

# Vue
https://betterprogramming.pub/vue-django-using-vue-files-and-the-vue-cli-d6dd8c9145eb

Install nodejs!

````shell script
npm install -g @vue/cli

cd vueapp
npm run serve
````

python manage.py collectstatic

