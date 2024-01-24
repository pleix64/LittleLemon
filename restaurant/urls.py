from django.urls import path, include
from . import views

from rest_framework import routers
from restaurant import views

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemListView.as_view()),
    path('menu/<int:pk>', views.MenuItemDetailView.as_view()),
    path('booking/', include(router.urls)),
]