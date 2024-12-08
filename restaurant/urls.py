from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Root URL for homepage
    path('menu/', views.MenuItemView.as_view(), name='menu-list'),  # Add name='menu-list'
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
]