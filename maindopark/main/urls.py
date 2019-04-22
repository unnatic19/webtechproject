from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('aboutus_new/', views.aboutus_new, name='aboutus_new'),
    path('features_new/', views.features_new, name='features_new'),
    path('landing/', views.landing, name='landing'),
    path('maps/', views.maps, name='maps'),
    path('',views.profile_new,name='profile_new'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('details/', views.results, name='results')
    
]
