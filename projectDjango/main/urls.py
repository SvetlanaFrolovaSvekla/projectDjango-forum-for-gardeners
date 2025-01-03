from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import profile_view, RegisterView

urlpatterns = [
    # cache_page(60 * 15)(views.about)
    path('', views.index, name='home'),  # Кэш на 15 минут
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('profile', profile_view, name="profile"),
    path('register', RegisterView.as_view(), name="register"),
    path('tag/<int:tag_id>/', views.news_by_tag, name='news_by_tag'),  # Новый путь для фильтрации
    path('tag_discussions/<int:tag_id>/', views.discussions_by_tag, name='discussions_by_tag'),  # Новый путь для фильтрации
]
