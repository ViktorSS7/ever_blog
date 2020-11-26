from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('<int:post_id>/', views.post_page, name='post_page')
]
