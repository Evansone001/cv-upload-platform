from re import template
from django.conf import settings
from django.urls import include, path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from . import views as uploader_views


urlpatterns = [
    path('', views.home,  name="home"),
    #path('cv-upload/', views.upload_data, name='cv-upload'),
    #path('fileupload/', uploader_views.UploadView.as_view(), name='fileupload'),
    path('profile/',views.profile, name='profile')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
