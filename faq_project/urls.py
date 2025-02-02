from django.contrib import admin
from django.urls import path, include
from faq.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faq/', include('faq.urls')),
    path('', home),  # Root URL mapping to the home view
]

