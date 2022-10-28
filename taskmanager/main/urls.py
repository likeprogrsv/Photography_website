from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('photography/<int:photo_id>', views.photography, name='photography')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
