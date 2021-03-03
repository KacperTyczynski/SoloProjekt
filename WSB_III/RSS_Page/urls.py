from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home),
    path('zaplecze/', views.zaplecze),
    path('RSS/', TemplateView.as_view(template_name="RSS.html"),
                   name='RSS'),
]
