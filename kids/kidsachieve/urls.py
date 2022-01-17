from django.urls import path
from .views import *



urlpatterns = [
    path('', ChildList.as_view(), name='index_kidsachieve_url'),
    path('child_create/', ChildCreate.as_view(), name='child_create_url'),
    path('child_detail/<str:slug>/', ChildDetail.as_view(), name='child_detail_url'),
    path('child_update/<str:slug>/', ChildUpdate.as_view(), name='child_update_url'),
    path('child_delete/<str:slug>/', ChildDelete.as_view(), name='child_delete_url'),

    path('work_create/', WorkCreate.as_view(), name='work_create_url'),
    path('work_detail/<str:slug>/', WorkDetail.as_view(), name='work_detail_url'),
    path('work_update/<str:slug>/', WorkUpdate.as_view(), name='work_update_url'),
    path('work_delete/<str:slug>/', WorkDelete.as_view(), name='work_delete_url'),
    path('works_list/', WorksList.as_view(), name='works_list_url'),

    path('achievement_create/', AchievementCreate.as_view(), name='achievement_create_url'),
    path('achievement_update/<str:slug>/', AchievementUpdate.as_view(), name='achievement_update_url'),
    path('achievement_delete/<str:slug>/', AchievementDelete.as_view(), name='achievement_delete_url'),

    path('child_achievements_list/<str:slug>/', ChildAchievementsList.as_view(), name='child_achievements_list_url')



]