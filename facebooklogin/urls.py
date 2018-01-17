from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.indexView,name='home'),
    path('Events/',views.eventMenu,name='event_menu'),
    path('Team/',views.team,name='team'),
    path('About/',views.about,name='about'),
    path('Events/Cultural/',views.cultural_events,name='cult_event'),
    path('Events/Managerial/',views.managerial_events,name='manag_event'),
    path('Events/Technical/',views.tech_events,name='tech_event'),
    path('Events/<str:eventName>/', views.eventTeamView, name='register_event'),
    path('Events/<str:eventname>/Update/', views.updateUserEvents, name='update_user'),
    path('Profile/',views.profile,name='profile'),
    path('Profile/removeEvents',views.removeEvents),

]
