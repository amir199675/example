from django.urls import path ,re_path
from . import views


app_name = 'rest_framework'
urlpatterns = [
	path('',views.index),
	re_path(r'^book/get/$', views.BookApiView.as_view(),name = 'apiarealist'),
	re_path(r'^auth/get/$', views.AuthApiView.as_view(),name = 'apiarealist'),
]