from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('predictions/', views.predictions, name='dashboard-predictions'),

    # path('blog/<int:id>/', views.show, name='blog-show'),
    # path('blog/create/', views.create, name='blog-create'),
    # path('blog/<int:id>/update/', views.update, name='blog-update'),
    # path('blog/<int:post_id>/comment/<int:comment_id>/update/', views.update_comment, name='update-comment'),
    
]
