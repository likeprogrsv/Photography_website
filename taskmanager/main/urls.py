from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
    path('about', views.about, name='about'),
    path('photos', views.photos, name='photos'),
    path('photography/<int:photo_id>', views.photography, name='photography'),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
