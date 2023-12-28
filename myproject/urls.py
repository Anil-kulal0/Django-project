
from django.contrib import admin
from django.urls import path, include
# from myapp.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]
