from django.urls import path
from . import views


app_name = 'Learn'

urlpatterns = [
 path('', views.index, name = 'index'),
 path('about/', views.about, name = 'about'),
 path('contact/', views.contact, name = 'contact'),
 path('skills/', views.skills, name = 'skills'),
 path('layout/', views.layout, name = 'layout'),
 path('signup/', views.registerPage, name = 'register'),
 path('login/',views.loginPage,name='login'),
 path('logout/', views.logoutUser, name = 'logout'),
 path('layout1/', views.layout1, name = 'layout1'),
 path('dashboard/',views.dashboard,name = 'dashboard'),
 path('explore_skills/',views.explore_skills,name='explore_skills'),
 path('my_skills/',views.my_skills,name='my_skills'),
 path('upload_skill/',views.upload_skill,name='upload_skill'),
 path('requests/',views.requests,name='requests'),
 path('analytics/',views.analytics,name='analytics'),
 path('newsletter/',views.newsletters,name='newsletter')
]