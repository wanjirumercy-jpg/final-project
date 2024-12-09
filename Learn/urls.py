from django.urls import path
from . import views


app_name = 'Learn'

urlpatterns = [
 path('', views.index, name = 'index'),
 path('about/', views.about, name = 'about'),
 path('contact/', views.contact, name = 'contact'),
 
 path('layout/', views.layout, name = 'layout'),
 path('signup/', views.registerPage, name = 'register'),
 path('login/',views.loginPage,name='login'),
 path('logout/', views.logoutUser, name = 'logout'),
 path('layout1/', views.layout1, name = 'layout1'),
 path('dashboard/',views.dashboard,name = 'dashboard'),
 path('explore_skills/',views.explore_skills,name='explore_skills'),
 path('my_skills/',views.my_skills,name='my_skills'),
 path('upload_skill/',views.upload_skill,name='upload_skill'),
 path('request_skill/',views.request_skill,name='request_skill'),
 path('view_skill_requests/', views.view_skill_requests, name='view_skill_requests'),
 path('newsletter/',views.newsletters,name='newsletter'),
 path('home/',views.home,name='home'),
#  path('add_feedback/',views.add_feedback,name='add_feedback'),
path('add_feedback/<int:request_id>/', views.add_feedback, name='add_feedback'),
path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
path('account/settings/', views.account_settings, name='account_settings'),
path('help/', views.help, name='help'),

]