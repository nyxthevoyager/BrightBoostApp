from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

# urlpatterns = [
#     path('brightBoostApp/', views.brightBoostApp, name='brightBoostApp'),
# ]

urlpatterns = [
    path ('home/', views.home,  name='home'),
    path('add_session/', views.add_session, name='add_session'),
    path('timetable/', views.display_timetable, name='display_timetable'),
     path('sessions_list/', views.sessions_list, name='sessions_list'),
   
] 
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

