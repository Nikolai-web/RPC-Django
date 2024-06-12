from django.contrib import admin
from django.urls import path
from main_app.views import JSONRPCView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', JSONRPCView.as_view(), name='jsonrpc')
]
