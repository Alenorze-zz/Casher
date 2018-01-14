from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    url(r'^api/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('accounts.api.urls', namespace='api-auth')),
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')),
    url(r'^api/status/', include('status.api.urls', namespace='api-status')),
]
