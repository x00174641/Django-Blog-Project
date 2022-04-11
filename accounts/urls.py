from django.urls import path 
from .views import signupView, signinView,signoutView

urlpatterns = [
    path('get-started/', signupView, name='get_started'),
    path('login/', signinView, name='login'),
    path('logout/', signoutView, name='signout'),
]