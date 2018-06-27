from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login

from . import views

app_name='test_project'
urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    url(r'^album/', views.album, name='album'),
    url(r'^(?P<cromo_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pagina_id>[0-9]+)/pagina/$',views.pagina, name='pagina'),

]