from django.conf.urls import url

from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

]
