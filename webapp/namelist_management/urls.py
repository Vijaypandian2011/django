from django.urls import path
from . import views

urlpatterns = [
    path('', views.NameListView.as_view(), name='name_list'),
    path('new/', views.NameCreateView.as_view(), name='name_new'),
    path('edit/<int:pk>/', views.NameUpdateView.as_view(), name='name_edit'),
    path('delete/<int:pk>/', views.NameDeleteView.as_view(), name='name_delete'),
]
