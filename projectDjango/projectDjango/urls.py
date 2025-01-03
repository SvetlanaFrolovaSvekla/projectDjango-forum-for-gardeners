from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('users/', include('users.urls', namespace="users")),
                  path('discussions/', include('discussions.urls')),
                  path('news/', include('news.urls')),
                  path('accounts/', include("django.contrib.auth.urls")),
                  path('i18n/', set_language, name='set_language'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Подключение встроенных маршрутов для смены языка
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
