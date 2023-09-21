from django.urls import path
from . import views

# urlpatterns = [
#     path('brightBoostApp/', views.brightBoostApp, name='brightBoostApp'),
# ]

urlpatterns = [
    path ('home/', views.home,  name='home'),
    path('add_session/', views.add_session, name='add_session'),
    path('timetable/', views.display_timetable, name='display_timetable'),
     path('sessions_list/', views.sessions_list, name='sessions_list'),
   
]

