from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussions_home, name='discussions_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.DiscussionsDetailView.as_view(), name='discussions_detail'),
    path('<int:pk>/update', views.DiscussionsUpdateView.as_view(), name='discussions_update'),
    path('<int:pk>/delete', views.DiscussionsDeleteView.as_view(), name='discussions_delete'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='discussions_comment'),  # Новый маршрут
]
