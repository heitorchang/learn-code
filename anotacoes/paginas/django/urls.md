# URLs in Django

Suppose you have a project named "supercool". There is an "accounts" app in this project.

## supercool/supercool/urls.py

```
from django.conf.urls import include, url
from accounts import urls as accounts_urls
from lists import views as list_views

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^accounts/', include(accounts_urls)),
]
```

## supercool/accounts/urls.py

```
from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import logout

app_name = 'accounts'

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email, name='send_login_email'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
```