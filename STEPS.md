# Steps

## installation
``` 
pip3 install djangorestframework
```

## Create a new instance
```
django-admin startproject Rest 
```

## Migrate
``` 
python3 manage.py migrate
```

## Make migrations
``` 
python3 manage.py makemigrations
python3 manage.py migrate
```

## Create a new app
```
python3 manager.py startapp [name] 
```

## Create super user
``` 
python3 manage.py createsuperuser
```

## Add modules to ./settings.py -> INSTALLED_APPS
```
'rest_framework',
'rest_framework.authtoken',
[your modules]
------------------------
python3 manage.py makemigrations
python3 manage.py migrate
```

## Register Modules into admin
``` 
from django.contrib import admin
from .models import [your module]

# Register your models here.

admin.site.register([your module])
```

## Create serializers file
```
apibasics or folder -> touch serializers.py
 ```

## Validate & create article from sell
```
python3 manage.py shell
------------------------
from api_basics.models import Article
from api_basics.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
------------------------
a = Article(title = 'Article Title', author = 'test author', email = 'test@test.com')
a.save()
------------------------
a = Article(title = 'Article Title 2', author = 'test author', email = 'test2@test.com')
a.save()
------------------------
serializer = ArticleSerializer(a)
serializer.data
------------------------
content = JSONRenderer().render(serializer.data)
content
------------------------
serializer = ArticleSerializer(Article.objects.all(), many=True)
serializer.data
------------------------
serializer = ArticleSerializer()
print(repr(serializer))
```
## Add Views to api_basics/views
``` 
Add views to api_basics/views
```

## Create a URL'S file to api_basics/urls
``` 
- add url's file to api_basics/urls
- on main urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('api_basics.urls'))
]

- @csrf_exempt to aviod the token validation
from django.views.decorators.csrf import csrf_exempt

```
