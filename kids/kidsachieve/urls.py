from django.urls import path
from .views import *

urlpatterns = [
    path('', ChildList.as_view(), name='index_kidsachieve_url'),
    path('child_create/', ChildCreate.as_view(), name='child_create_url'),
    path('work_create/', WorkCreate.as_view(), name='work_create_url'),
    path('achievement_create/', AchievementCreate.as_view(), name='achievement_create_url'),

]