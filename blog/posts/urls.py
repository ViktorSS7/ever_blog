from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('<int:post_id>/', views.post_page, name='post_page'),

    path('comment/<int:post_id>/post', views.comment_create, name='comment_create')
]
