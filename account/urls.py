from django.urls import path
from . import views

urlpatterns = [
    path('', views.import_accounts, name='import_accounts'),
    path('accounts/', views.list_accounts, name='list_accounts'),
    path('transfer/', views.transfer_funds, name='transfer_funds'),
]