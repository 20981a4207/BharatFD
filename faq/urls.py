from django.urls import path, include
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet

router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns = [
    path('api/faqs', views.FAQViewSet.as_view({'get': 'list'})),  # Make sure this is correct
]
