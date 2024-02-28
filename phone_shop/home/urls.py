from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.registration, name='registration'),
    path('login', authViews.LoginView.as_view(template_name='home/login.html'), name="login"),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('db/', include('db.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 