from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='posts'),
    path('<int:post_id>/', views.post_page, name='post_page'),

    path('comment/<int:post_id>/post', views.comment_create, name='comment_create'),
    path('comment/<int:comment_id>/delete', views.comment_delete, name='comment_delete'),

    path('', include('django.contrib.auth.urls'))
]
