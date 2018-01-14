from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    url(r'^api/$', schema_view),
    url(r'^admin/', include(admin.site.urls)),
]
