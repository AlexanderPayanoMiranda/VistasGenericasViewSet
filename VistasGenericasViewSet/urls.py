from django.contrib import admin
from django.urls import path, include
from GViews.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('GViews.urls')),
    path('', index, name='index')
]
