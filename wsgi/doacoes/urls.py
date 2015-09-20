from django.conf.urls import include, url
from doacoes import views

urlpatterns = [
	url(r'^(?P<sigla_unidade>.+)/$', views.formulario, name="formulario"),
	url('', views.escolher_unidade, name="escolher_unidade"),
]
