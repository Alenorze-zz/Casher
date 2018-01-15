from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from accounts.routes import routes as accounts_routes

#Swagger
schema_view = get_swagger_view(title='MonsterCash API')

#DRF Routing
router = routers.DefaultRouter()

routes = accounts_routes
for route in routes:
    router.register(route[0], route[1])



urlpatterns = [
    url(r'^docs/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^get_auth_token/$', obtain_auth_token, name='get_auth_token'),
    url(r'^api/', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
