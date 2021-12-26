from django.urls import path
from .views import *

urlpatterns = [
    path('', ChildList.as_view(), name='index_kidsachieve_url'),
    path('child_create/', ChildCreate.as_view(), name='child_create_url'),
    path('cwork_create/', work_create, name='work_create_url'),
    path('achievement_create/', achievement_create, name='achievement_create_url'),

]